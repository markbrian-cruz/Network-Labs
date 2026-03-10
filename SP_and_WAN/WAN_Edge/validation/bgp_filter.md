CustomerA3# show ip bgp neighbors SP2_IP_A3 advertised-routes
                                 ^
% Invalid input detected at '^' marker.


CustomerA3# show ip bgp summary
BGP router identifier 3.3.3.3, local AS number 64850
BGP table version is 43, main routing table version 43
27 network entries using 3240 bytes of memory
31 path entries using 1612 bytes of memory
13/8 BGP path/bestpath attribute entries using 1612 bytes of memory
4 BGP AS-PATH entries using 96 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 3 (at peak 3) using 92 bytes of memory
BGP using 6652 total bytes of memory
BGP activity 30/3 prefixes, 37/6 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
11.1.1.1        4 64850     182     181       43    0    0 02:47:20        8
20.0.0.9        4 64800     185     175       43    0    0 02:47:27       22

CustomerA4# show ip bgp neighbors SP2_IP_A4 advertised-routes
                                 ^
% Invalid input detected at '^' marker.


CustomerA4# show ip bgp summary
BGP router identifier 4.4.4.4, local AS number 64850
BGP table version is 30, main routing table version 30
27 network entries using 3240 bytes of memory
49 path entries using 2548 bytes of memory
16/7 BGP path/bestpath attribute entries using 1984 bytes of memory
7 BGP AS-PATH entries using 168 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 2 (at peak 2) using 64 bytes of memory
BGP using 8004 total bytes of memory
BGP activity 27/0 prefixes, 50/1 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
11.1.1.5        4 64850      28      22       30    0    0 00:17:06       26
20.0.0.13       4 64800      30      26       30    0    0 00:17:34       22

