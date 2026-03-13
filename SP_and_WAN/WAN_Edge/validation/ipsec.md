CUSTOMERA3
```
CustomerA3#sh crypto isakmp sa
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id slot status
20.0.0.10       20.0.0.14       QM_IDLE           1001    0 ACTIVE

IPv6 Crypto ISAKMP SA

CustomerA3#sh crypto ipsec sa

interface: Tunnel0
    Crypto map tag: Tunnel0-head-0, local addr 20.0.0.10

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (20.0.0.10/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (20.0.0.14/255.255.255.255/47/0)
   current_peer 20.0.0.14 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 5826, #pkts encrypt: 5826, #pkts digest: 5826
    #pkts decaps: 5533, #pkts decrypt: 5533, #pkts verify: 5533
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 9, #recv errors 0

     local crypto endpt.: 20.0.0.10, remote crypto endpt.: 20.0.0.14
     path mtu 1500, ip mtu 1500, ip mtu idb FastEthernet0/1
     current outbound spi: 0x9D43B506(2638460166)

     inbound esp sas:
      spi: 0xC2CBE9C4(3268143556)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 25, flow_id: SW:25, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4513657/1744)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0x9D43B506(2638460166)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 26, flow_id: SW:26, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4513643/1744)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE

     outbound ah sas:

     outbound pcp sas:
CustomerA3#
```

CustomerA4
```
CustomerA4#sh crypto isakmp sa
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id slot status
20.0.0.10       20.0.0.14       QM_IDLE           1001    0 ACTIVE

IPv6 Crypto ISAKMP SA

CustomerA4#sh crypto ipsec sa

interface: Tunnel0
    Crypto map tag: Tunnel0-head-0, local addr 20.0.0.14

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (20.0.0.14/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (20.0.0.10/255.255.255.255/47/0)
   current_peer 20.0.0.10 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 5922, #pkts encrypt: 5922, #pkts digest: 5922
    #pkts decaps: 5935, #pkts decrypt: 5935, #pkts verify: 5935
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 7, #recv errors 0

     local crypto endpt.: 20.0.0.14, remote crypto endpt.: 20.0.0.10
     path mtu 1500, ip mtu 1500, ip mtu idb FastEthernet0/1
     current outbound spi: 0xC2CBE9C4(3268143556)

     inbound esp sas:
      spi: 0x9D43B506(2638460166)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 25, flow_id: SW:25, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4544651/1719)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0xC2CBE9C4(3268143556)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 26, flow_id: SW:26, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4544646/1719)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE

     outbound ah sas:

     outbound pcp sas:
CustomerA4#
```

NOTE
```
- IPSec tunnel is fully operational between 20.0.0.10 ↔ 20.0.0.14
- ISAKMP (Phase 1) and ESP (Phase 2) SAs are ACTIVE
- Tunnel MTU set to 1400 → maximum safe payload ~1360 bytes (see GRE test)
- Minor send errors observed, no impact on traffic
```


