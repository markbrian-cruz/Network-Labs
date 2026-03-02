# BGP_IPv4_Summary Validation Report
Generated: 2026-03-02 13:15:17.048814

SP1-PE1#show ip bgp summary
```
BGP router identifier 1.1.1.1, local AS number 65000
BGP table version is 48, main routing table version 48
26 network entries using 3120 bytes of memory
51 path entries using 2652 bytes of memory
20/5 BGP path/bestpath attribute entries using 2480 bytes of memory
6 BGP rrinfo entries using 144 bytes of memory
7 BGP AS-PATH entries using 168 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 2 (at peak 2) using 64 bytes of memory
BGP using 8676 total bytes of memory
BGP activity 56/0 prefixes, 112/2 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
2.2.2.2         4 65000     341     328       48    0    0 05:16:15       24
4.4.4.4         4 65000     341     327       48    0    0 05:16:19       24
```

SP1-BR2#show ip bgp summary
```
BGP router identifier 2.2.2.2, local AS number 65000
BGP table version is 39, main routing table version 39
26 network entries using 3120 bytes of memory
64 path entries using 3328 bytes of memory
19/7 BGP path/bestpath attribute entries using 2356 bytes of memory
3 BGP rrinfo entries using 72 bytes of memory
10 BGP AS-PATH entries using 256 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 3 (at peak 5) using 96 bytes of memory
BGP using 9276 total bytes of memory
BGP activity 56/0 prefixes, 110/8 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
1.1.1.1         4 65000     329     342       39    0    0 05:17:17        3
3.3.3.3         4 65000     328     331       39    0    0 05:17:12       16
4.4.4.4         4 65000     333     330       39    0    0 05:17:17       11
5.5.5.5         4 65000     328     342       39    0    0 05:17:12        3
10.0.1.1        4 64900     328     328       39    0    0 05:17:30       13
20.0.1.1        4 64800     328     328       39    0    0 05:17:53       13
```

SP1-BR3#show ip bgp summary
```
BGP router identifier 3.3.3.3, local AS number 65000
BGP table version is 49, main routing table version 49
26 network entries using 3120 bytes of memory
76 path entries using 3952 bytes of memory
14/7 BGP path/bestpath attribute entries using 1736 bytes of memory
6 BGP rrinfo entries using 144 bytes of memory
6 BGP AS-PATH entries using 160 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 2 (at peak 3) using 64 bytes of memory
BGP using 9176 total bytes of memory
BGP activity 26/0 prefixes, 78/2 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
2.2.2.2         4 65000     331     328       49    0    0 05:17:21       22
4.4.4.4         4 65000     333     328       49    0    0 05:17:24       23
10.0.1.5        4 64900     325     330       49    0    0 05:17:43       13
20.0.1.5        4 64800     327     330       49    0    0 05:17:57       13
```

SP1-RR4#show ip bgp summary
```
BGP router identifier 4.4.4.4, local AS number 65000
BGP table version is 43, main routing table version 43
26 network entries using 3120 bytes of memory
49 path entries using 2548 bytes of memory
11/5 BGP path/bestpath attribute entries using 1364 bytes of memory
3 BGP rrinfo entries using 72 bytes of memory
7 BGP AS-PATH entries using 168 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 1 (at peak 2) using 32 bytes of memory
BGP using 7352 total bytes of memory
BGP activity 56/0 prefixes, 90/3 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
1.1.1.1         4 65000     328     342       43    0    0 05:17:37        3
2.2.2.2         4 65000     330     333       43    0    0 05:17:33       23
3.3.3.3         4 65000     328     333       43    0    0 05:17:31       16
5.5.5.5         4 65000     327     342       43    0    0 05:17:30        3
```

SP1-PE5#show ip bgp summary
```
BGP router identifier 5.5.5.5, local AS number 65000
BGP table version is 47, main routing table version 47
26 network entries using 3120 bytes of memory
52 path entries using 2704 bytes of memory
20/5 BGP path/bestpath attribute entries using 2480 bytes of memory
6 BGP rrinfo entries using 144 bytes of memory
7 BGP AS-PATH entries using 168 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 2 (at peak 2) using 64 bytes of memory
BGP using 8728 total bytes of memory
BGP activity 56/0 prefixes, 129/2 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
2.2.2.2         4 65000     342     328       47    0    0 05:17:43       25
4.4.4.4         4 65000     342     327       47    0    0 05:17:44       24
```

