# BGP_IPv4_Summary Validation Report
Generated: 2026-03-02 01:40:17.601445

```
SP1-PE1#show ip bgp summary
BGP router identifier 1.1.1.1, local AS number 65000
BGP table version is 86, main routing table version 86
22 network entries using 2640 bytes of memory
43 path entries using 2236 bytes of memory
10/4 BGP path/bestpath attribute entries using 1240 bytes of memory
6 BGP rrinfo entries using 144 bytes of memory
3 BGP AS-PATH entries using 72 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 2 (at peak 3) using 64 bytes of memory
BGP using 6444 total bytes of memory
BGP activity 31/0 prefixes, 110/50 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
2.2.2.2         4 65000     151     133       86    0    0 01:32:24       20
4.4.4.4         4 65000     149     133       86    0    0 01:32:24       20
```

```
SP1-BR2#show ip bgp summary
BGP router identifier 2.2.2.2, local AS number 65000
BGP table version is 41, main routing table version 41
22 network entries using 2640 bytes of memory
52 path entries using 2704 bytes of memory
13/6 BGP path/bestpath attribute entries using 1612 bytes of memory
3 BGP rrinfo entries using 72 bytes of memory
5 BGP AS-PATH entries using 120 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 3 (at peak 6) using 96 bytes of memory
BGP using 7292 total bytes of memory
BGP activity 31/0 prefixes, 73/12 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
1.1.1.1         4 65000     133     151       41    0    0 01:32:57        3
3.3.3.3         4 65000     127     135       41    0    0 01:59:37       12
4.4.4.4         4 65000     135     133       41    0    0 01:59:35       11
5.5.5.5         4 65000     127     143       41    0    0 01:59:35        3
10.0.1.1        4 64900     132     133       41    0    0 02:00:08        9
20.0.1.1        4 64800     131     132       41    0    0 01:59:54        9
```

```
SP1-BR3#show ip bgp summary
BGP router identifier 3.3.3.3, local AS number 65000
BGP table version is 46, main routing table version 46
22 network entries using 2640 bytes of memory
60 path entries using 3120 bytes of memory
11/6 BGP path/bestpath attribute entries using 1364 bytes of memory
6 BGP rrinfo entries using 144 bytes of memory
4 BGP AS-PATH entries using 96 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 2 (at peak 2) using 64 bytes of memory
BGP using 7428 total bytes of memory
BGP activity 22/0 prefixes, 83/23 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
2.2.2.2         4 65000     135     127       46    0    0 01:59:46       18
4.4.4.4         4 65000     144     135       46    0    0 00:43:30       19
10.0.1.5        4 64900     130     131       46    0    0 02:00:18        9
20.0.1.5        4 64800     130     131       46    0    0 02:00:19        9
```

```
SP1-RR4#show ip bgp summary
BGP router identifier 4.4.4.4, local AS number 65000
BGP table version is 47, main routing table version 47
22 network entries using 2640 bytes of memory
41 path entries using 2132 bytes of memory
7/4 BGP path/bestpath attribute entries using 868 bytes of memory
3 BGP rrinfo entries using 72 bytes of memory
3 BGP AS-PATH entries using 72 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 1 (at peak 2) using 32 bytes of memory
BGP using 5864 total bytes of memory
BGP activity 31/0 prefixes, 72/22 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
1.1.1.1         4 65000     134     150       47    0    0 01:33:13        3
2.2.2.2         4 65000     133     135       47    0    0 01:59:52       19
3.3.3.3         4 65000     135     144       47    0    0 00:43:37       12
5.5.5.5         4 65000     127     143       47    0    0 01:59:52        3
```

```
SP1-PE5#show ip bgp summary
BGP router identifier 5.5.5.5, local AS number 65000
BGP table version is 42, main routing table version 42
22 network entries using 2640 bytes of memory
44 path entries using 2288 bytes of memory
10/4 BGP path/bestpath attribute entries using 1240 bytes of memory
6 BGP rrinfo entries using 144 bytes of memory
3 BGP AS-PATH entries using 72 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
Bitfield cache entries: current 2 (at peak 3) using 64 bytes of memory
BGP using 6496 total bytes of memory
BGP activity 31/0 prefixes, 71/10 paths, scan interval 60 secs

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
2.2.2.2         4 65000     144     128       42    0    0 02:00:06       21
4.4.4.4         4 65000     144     128       42    0    0 02:00:07       20
```

