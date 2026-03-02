# TE_Tunnel_10 Validation Report
Generated: 2026-03-02 01:40:17.601401

```
SP1-PE1#show mpls traffic-eng tunnels tunnel 10

Name: TO-R5-UPPER                         (Tunnel10) Destination: 5.5.5.5
  Status:
    Admin: up         Oper: up     Path: valid       Signalling: connected

    path option 1, type explicit PATH-UPPER-R1-R5 (Basis for Setup, path weight 30)
    path option 2, type explicit PATH-LOWER-R1-R5

  Config Parameters:
    Bandwidth: 1        kbps (Global)  Priority: 7  7   Affinity: 0x0/0xFFFF
    Metric Type: TE (default)
    AutoRoute:  enabled   LockDown: disabled  Loadshare: 1        bw-based
    auto-bw: disabled

  InLabel  :  - 
  OutLabel : FastEthernet0/0, 18
  RSVP Signalling Info:
       Src 1.1.1.1, Dst 5.5.5.5, Tun_Id 10, Tun_Instance 27
    RSVP Path Info:
      My Address: 10.0.0.0   
      Explicit Route: 10.0.0.1 10.0.0.2 10.0.0.3 10.0.0.4 
                      10.0.0.5 5.5.5.5 
      Record Route:  NONE
      Tspec: ave rate=1 kbits, burst=1000 bytes, peak rate=1 kbits
    RSVP Resv Info:
      Record Route:  NONE
      Fspec: ave rate=1 kbits, burst=1000 bytes, peak rate=1 kbits
  Shortest Unconstrained Path Info:
    Path Weight: 20 (TE)
    Explicit Route: 10.0.0.6 10.0.0.7 10.0.0.8 10.0.0.9 
                    5.5.5.5 
  History:
    Tunnel:
      Time since created: 2 hours
      Time since path change: 1 hours, 59 minutes
    Current LSP:
      Uptime: 1 hours, 59 minutes
```

```
SP1-PE5#show mpls traffic-eng tunnels tunnel 10

Name: TO-R1-UPPER                         (Tunnel10) Destination: 1.1.1.1
  Status:
    Admin: up         Oper: up     Path: valid       Signalling: connected

    path option 1, type explicit PATH-UPPER-R5-R1 (Basis for Setup, path weight 30)
    path option 2, type explicit PATH-LOWER-R5-R1

  Config Parameters:
    Bandwidth: 1        kbps (Global)  Priority: 7  7   Affinity: 0x0/0xFFFF
    Metric Type: TE (default)
    AutoRoute:  enabled   LockDown: disabled  Loadshare: 1        bw-based
    auto-bw: disabled

  InLabel  :  - 
  OutLabel : FastEthernet0/0, 18
  RSVP Signalling Info:
       Src 5.5.5.5, Dst 1.1.1.1, Tun_Id 10, Tun_Instance 25
    RSVP Path Info:
      My Address: 10.0.0.5   
      Explicit Route: 10.0.0.4 10.0.0.3 10.0.0.2 10.0.0.1 
                      10.0.0.0 1.1.1.1 
      Record Route:  NONE
      Tspec: ave rate=1 kbits, burst=1000 bytes, peak rate=1 kbits
    RSVP Resv Info:
      Record Route:  NONE
      Fspec: ave rate=1 kbits, burst=1000 bytes, peak rate=1 kbits
  Shortest Unconstrained Path Info:
    Path Weight: 20 (TE)
    Explicit Route: 10.0.0.9 10.0.0.8 10.0.0.7 10.0.0.6 
                    1.1.1.1 
  History:
    Tunnel:
      Time since created: 2 hours, 1 minutes
      Time since path change: 2 hours, 1 minutes
    Current LSP:
      Uptime: 2 hours, 1 minutes
```

