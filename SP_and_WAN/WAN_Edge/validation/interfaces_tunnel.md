CustomerA1# show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            15.15.1.2       YES NVRAM  up                    up      
FastEthernet0/1            11.1.1.1        YES NVRAM  up                    up      
FastEthernet1/0            192.168.1.2     YES NVRAM  up                    up      
FastEthernet2/0            unassigned      YES NVRAM  administratively down down    
Loopback0                  1.1.1.1         YES NVRAM  up                    up      

CustomerA2# show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            15.15.2.2       YES NVRAM  up                    up      
FastEthernet0/1            11.1.1.5        YES NVRAM  up                    up      
FastEthernet1/0            192.168.2.2     YES NVRAM  up                    up      
FastEthernet2/0            unassigned      YES NVRAM  administratively down down    
Loopback0                  2.2.2.2         YES NVRAM  up                    up      

CustomerA3# show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            11.1.1.2        YES NVRAM  up                    up      
FastEthernet0/1            20.0.0.10       YES NVRAM  up                    up      
FastEthernet1/0            192.168.1.3     YES NVRAM  up                    up      
FastEthernet2/0            unassigned      YES NVRAM  administratively down down    
NVI0                       11.1.1.2        YES unset  up                    up      
Loopback0                  3.3.3.3         YES NVRAM  up                    up      
Tunnel0                    40.0.0.1        YES NVRAM  up                    up      

CustomerA3# show crypto ipsec sa

interface: Tunnel0
    Crypto map tag: Tunnel0-head-0, local addr 20.0.0.10

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (20.0.0.10/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (20.0.0.14/255.255.255.255/47/0)
   current_peer 20.0.0.14 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 1239, #pkts encrypt: 1239, #pkts digest: 1239
    #pkts decaps: 1055, #pkts decrypt: 1055, #pkts verify: 1055
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 0, #recv errors 0

     local crypto endpt.: 20.0.0.10, remote crypto endpt.: 20.0.0.14
     path mtu 1500, ip mtu 1500, ip mtu idb FastEthernet0/1
     current outbound spi: 0x197DDAB3(427678387)

     inbound esp sas:
      spi: 0xCDDFAA19(3453987353)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 7, flow_id: SW:7, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4481853/2628)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0x197DDAB3(427678387)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 8, flow_id: SW:8, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4481850/2628)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE

     outbound ah sas:

     outbound pcp sas:

CustomerA3# show tunnel interface Tunnel0

 TUNNEL: Tunnel0
   Mode:GRE/IP, Destination 20.0.0.14, Source 20.0.0.10

CustomerA4# show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            11.1.1.6        YES NVRAM  up                    up      
FastEthernet0/1            20.0.0.14       YES NVRAM  up                    up      
FastEthernet1/0            192.168.2.3     YES NVRAM  up                    up      
FastEthernet2/0            unassigned      YES NVRAM  administratively down down    
NVI0                       11.1.1.6        YES unset  up                    up      
Loopback0                  4.4.4.4         YES NVRAM  up                    up      
Tunnel0                    40.0.0.2        YES NVRAM  up                    up      

CustomerA4# show crypto ipsec sa

interface: Tunnel0
    Crypto map tag: Tunnel0-head-0, local addr 20.0.0.14

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (20.0.0.14/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (20.0.0.10/255.255.255.255/47/0)
   current_peer 20.0.0.10 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 112, #pkts encrypt: 112, #pkts digest: 112
    #pkts decaps: 129, #pkts decrypt: 129, #pkts verify: 129
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 0, #recv errors 0

     local crypto endpt.: 20.0.0.14, remote crypto endpt.: 20.0.0.10
     path mtu 1500, ip mtu 1500, ip mtu idb FastEthernet0/1
     current outbound spi: 0xCDDFAA19(3453987353)

     inbound esp sas:
      spi: 0x197DDAB3(427678387)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 1, flow_id: SW:1, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4452871/2623)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0xCDDFAA19(3453987353)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 2, flow_id: SW:2, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4452874/2623)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE

     outbound ah sas:

     outbound pcp sas:

CustomerA4# show tunnel interface Tunnel0

 TUNNEL: Tunnel0
   Mode:GRE/IP, Destination 20.0.0.10, Source 20.0.0.14

