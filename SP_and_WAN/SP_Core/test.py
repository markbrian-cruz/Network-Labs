#!/usr/bin/env python3
"""
SP Core Lab Validation Script (Cisco 3725 Compatible)
Outputs per-category Markdown files in validation/
"""

from netmiko import ConnectHandler
import yaml
import os
from datetime import datetime

# -----------------------------
# Load Credentials
# -----------------------------
with open("secrets.yml") as f:
    creds = yaml.safe_load(f)

USERNAME = creds["ansible_user"]
PASSWORD = creds["ansible_ssh_pass"]
ENABLE_PASS = creds["ansible_become_pass"]

# -----------------------------
# Router Inventory
# -----------------------------
routers = [
    {"name": "SP1-PE1", "host": "1.1.1.1", "role": "PE"},
    {"name": "SP1-BR2", "host": "2.2.2.2", "role": "BR"},
    {"name": "SP1-BR3", "host": "3.3.3.3", "role": "BR"},
    {"name": "SP1-RR4", "host": "4.4.4.4", "role": "RR"},
    {"name": "SP1-PE5", "host": "5.5.5.5", "role": "PE"},
]

# -----------------------------
# Create validation directory
# -----------------------------
os.makedirs("validation", exist_ok=True)

# -----------------------------
# Core Infrastructure Tests
# -----------------------------
core_tests = {
    "ISIS": "show isis adjacency",
    "MPLS_LDP": "show mpls ldp neighbor",
    "NTP_Status": "show ntp status",
    "NTP_Associations": "show ntp associations",
}

# -----------------------------
# MPLS TE Tunnels (PEs only)
# -----------------------------
te_tests = {
    "TE_Tunnel_10": "show mpls traffic-eng tunnels tunnel 10",
    "TE_Tunnel_20": "show mpls traffic-eng tunnels tunnel 20",
}

# -----------------------------
# BGP Tests
# -----------------------------
bgp_tests = {
    "BGP_IPv4_Summary": "show ip bgp summary",
}

# RR Specific VPNv4
rr_tests = {
    "BGP_VPNv4_Summary": "show ip bgp vpnv4 all summary",
}

# -----------------------------
# Overlapping VRF Validation (PEs only)
# -----------------------------
vrf_tests = {
    "SP1-PE1": [
        {"vrf": "CUST_A", "target": "15.15.2.1"},
        {"vrf": "CUST_B", "target": "15.15.2.1"},
    ],
    "SP1-PE5": [
        {"vrf": "CUST_A", "target": "15.15.1.1"},
        {"vrf": "CUST_B", "target": "15.15.1.1"},
    ],
}

# -----------------------------
# Dual ISP Validation (PEs only)
# -----------------------------
internet_tests = {
    "Internet_Ping": "ping 8.8.8.8 repeat 2",
    "BGP_8.8.8.8": "show ip bgp 8.8.8.8",
}

# -----------------------------
# Create Markdown files
# -----------------------------
sections = {}
sections.update(core_tests)
sections.update(te_tests)
sections.update(bgp_tests)
sections.update(rr_tests)
sections.update(internet_tests)
sections["VRF_Ping"] = None
sections["VRF_Traceroute"] = None
sections["VRF_Route_Table"] = None

md_files = {}
for section in sections:
    file = open(f"validation/{section}.md", "w")
    file.write(f"# {section} Validation Report\n")
    file.write(f"Generated: {datetime.now()}\n\n")
    md_files[section] = file

# -----------------------------
# Helper to write output with hostname + command
# -----------------------------
def write_output(file_handle, hostname, command, output):
    file_handle.write(f"## {hostname}\n")
    file_handle.write(f"Router: {hostname}\n")
    file_handle.write(f"Command: {command}\n")
    file_handle.write(f"```\n{output}\n```\n\n")

# -----------------------------
# Execution
# -----------------------------
for router in routers:
    print(f"[INFO] Connecting to {router['name']}")
    try:
        conn = ConnectHandler(
            device_type="cisco_ios",
            host=router["host"],
            username=USERNAME,
            password=PASSWORD,
            secret=ENABLE_PASS,
            global_delay_factor=2,   # slow 3725 fix
            timeout=120,             # modern Netmiko
            session_log=f"session_{router['name']}.log"
        )
        conn.enable()

        # Core infrastructure tests (all routers)
        for section, cmd in core_tests.items():
            output = conn.send_command(cmd)
            write_output(md_files[section], router["name"], cmd, output)

        # MPLS TE only for PEs (use send_command_timing for reliability)
        if router["role"] == "PE":
            for section, cmd in te_tests.items():
                output = conn.send_command_timing(cmd)
                write_output(md_files[section], router["name"], cmd, output)

        # BGP IPv4 summary (all routers)
        for section, cmd in bgp_tests.items():
            output = conn.send_command(cmd)
            write_output(md_files[section], router["name"], cmd, output)

        # RR VPNv4 check
        if router["role"] == "RR":
            for section, cmd in rr_tests.items():
                output = conn.send_command(cmd)
                write_output(md_files[section], router["name"], cmd, output)

        # VRF tests (PEs only)
        if router["name"] in vrf_tests:
            for vrf_entry in vrf_tests[router["name"]]:
                vrf = vrf_entry["vrf"]
                target = vrf_entry["target"]

                ping_cmd = f"ping vrf {vrf} {target} repeat 2"
                trace_cmd = f"traceroute vrf {vrf} {target}"
                route_cmd = f"show ip route vrf {vrf}"

                ping_output = conn.send_command_timing(ping_cmd)
                trace_output = conn.send_command_timing(trace_cmd)
                route_output = conn.send_command_timing(route_cmd)

                write_output(md_files["VRF_Ping"], router["name"], ping_cmd, ping_output)
                write_output(md_files["VRF_Traceroute"], router["name"], trace_cmd, trace_output)
                write_output(md_files["VRF_Route_Table"], router["name"], route_cmd, route_output)

        # Dual ISP / internet tests (PEs only)
        if router["role"] == "PE":
            for section, cmd in internet_tests.items():
                output = conn.send_command_timing(cmd)
                write_output(md_files[section], router["name"], cmd, output)

        conn.disconnect()
        print(f"[INFO] {router['name']} completed\n")

    except Exception as e:
        print(f"[ERROR] {router['name']} failed: {e}")
        for md in md_files.values():
            md.write(f"## {router['name']} ERROR\n```\n{e}\n```\n\n")

# Close all Markdown files
for file in md_files.values():
    file.close()

print("[INFO] All validation completed. Results saved in 'validation/' directory.")
