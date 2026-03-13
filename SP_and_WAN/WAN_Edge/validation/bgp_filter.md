CustomerA3
```
CustomerA3#sh ip bgp
BGP table version is 73, local router ID is 172.16.200.3
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 8.8.4.4/32       20.0.0.9                               0 64800 64900 i
*> 8.8.8.8/32       20.0.0.9                               0 64800 64900 i
*> 10.0.1.0/30      20.0.0.9                               0 64800 64900 i
*> 10.0.1.4/30      20.0.0.9                               0 64800 64900 i
r>i11.1.1.0/30      11.1.1.1                 0    100      0 i
*>i11.1.1.4/30      11.1.1.1                 0     50      0 65000 65000 i
*>i15.15.1.0/24     11.1.1.1                 0    100      0 i
*>i15.15.2.0/24     11.1.1.1                 0     50      0 65000 65000 i
*> 20.0.0.0/30      20.0.0.9                 0             0 64800 i
*  20.0.0.8/30      20.0.0.9                 0             0 64800 i
*>                  0.0.0.0                  0         32768 i
*> 20.0.0.12/30     20.0.0.9                               0 64800 i
*> 20.0.1.8/30      20.0.0.9                               0 64800 64900 i
*> 20.0.1.12/30     20.0.0.9                               0 64800 64900 i
r>i192.168.1.0      11.1.1.1                 0    100      0 ?
CustomerA3#sh ip bgp neighbors  20.0.0.9 advertised-routes
BGP table version is 73, local router ID is 172.16.200.3
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 20.0.0.8/30      0.0.0.0                  0         32768 i

Total number of prefixes 1
CustomerA3#
```

CustomerA4
```
CustomerA4#sh ip bgp
BGP table version is 69, local router ID is 172.16.200.4
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 8.8.4.4/32       20.0.0.13                              0 64800 64900 i
*> 8.8.8.8/32       20.0.0.13                              0 64800 64900 i
*> 10.0.1.0/30      20.0.0.13                              0 64800 64900 i
*> 10.0.1.4/30      20.0.0.13                              0 64800 64900 i
*>i11.1.1.0/30      11.1.1.5                 0     50      0 65000 65000 i
r>i11.1.1.4/30      11.1.1.5                 0    100      0 i
*>i15.15.1.0/24     11.1.1.5                 0     50      0 65000 65000 i
*>i15.15.2.0/24     11.1.1.5                 0    100      0 i
*> 20.0.0.0/30      20.0.0.13                0             0 64800 i
*> 20.0.0.8/30      20.0.0.13                              0 64800 i
*  20.0.0.12/30     20.0.0.13                0             0 64800 i
*>                  0.0.0.0                  0         32768 i
*> 20.0.1.8/30      20.0.0.13                              0 64800 64900 i
*> 20.0.1.12/30     20.0.0.13                              0 64800 64900 i
*>i192.168.1.0      11.1.1.5                 0    100      0 65000 65000 ?
CustomerA4#sh ip bgp neighbors 20.0.0.13 advertised-routes
BGP table version is 69, local router ID is 172.16.200.4
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 20.0.0.12/30     0.0.0.0                  0         32768 i

Total number of prefixes 1
CustomerA4#
```

CustomerA1
```
CustomerA1#sh ip bgp
BGP table version is 41, local router ID is 15.15.1.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
r>i0.0.0.0          11.1.1.2                 0    100      0 i
*>i8.8.4.4/32       11.1.1.2                 0    100      0 64800 64900 i
*>i8.8.8.8/32       11.1.1.2                 0    100      0 64800 64900 i
*>i10.0.1.0/30      11.1.1.2                 0    100      0 64800 64900 i
*>i10.0.1.4/30      11.1.1.2                 0    100      0 64800 64900 i
*> 11.1.1.0/30      0.0.0.0                  0         32768 i
*> 11.1.1.4/30      15.15.1.1                      50      0 65000 65000 i
*> 15.15.1.0/24     0.0.0.0                  0         32768 i
r> 15.15.2.0/24     15.15.1.1                      50      0 65000 65000 i
*>i20.0.0.0/30      11.1.1.2                 0    100      0 64800 i
*>i20.0.0.8/30      11.1.1.2                 0    100      0 i
*  20.0.0.12/30     15.15.1.1                      50      0 65000 65000 i
*>i                 11.1.1.2                 0    100      0 64800 i
*>i20.0.1.8/30      11.1.1.2                 0    100      0 64800 64900 i
*>i20.0.1.12/30     11.1.1.2                 0    100      0 64800 64900 i
*> 192.168.1.0      0.0.0.0                  0         32768 ?

CustomerA1#sh ip bgp neighbors 15.15.1.1 advertised-routes
BGP table version is 41, local router ID is 15.15.1.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
r>i0.0.0.0          11.1.1.2                 0    100      0 i
*>i8.8.4.4/32       11.1.1.2                 0    100      0 64800 64900 i
*>i8.8.8.8/32       11.1.1.2                 0    100      0 64800 64900 i
*>i10.0.1.0/30      11.1.1.2                 0    100      0 64800 64900 i
*>i10.0.1.4/30      11.1.1.2                 0    100      0 64800 64900 i
*> 11.1.1.0/30      0.0.0.0                  0         32768 i
*> 15.15.1.0/24     0.0.0.0                  0         32768 i
*>i20.0.0.0/30      11.1.1.2                 0    100      0 64800 i
*>i20.0.0.8/30      11.1.1.2                 0    100      0 i
*>i20.0.0.12/30     11.1.1.2                 0    100      0 64800 i
*>i20.0.1.8/30      11.1.1.2                 0    100      0 64800 64900 i
*>i20.0.1.12/30     11.1.1.2                 0    100      0 64800 64900 i
*> 192.168.1.0      0.0.0.0                  0         32768 ?

Total number of prefixes 13
CustomerA1#
```

CustomerA2
```
CustomerA2#sh ip bgp
BGP table version is 62, local router ID is 172.16.200.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
r>i0.0.0.0          11.1.1.6                 0    100      0 i
*>i8.8.4.4/32       11.1.1.6                 0    100      0 64800 64900 i
*>i8.8.8.8/32       11.1.1.6                 0    100      0 64800 64900 i
*>i10.0.1.0/30      11.1.1.6                 0    100      0 64800 64900 i
*>i10.0.1.4/30      11.1.1.6                 0    100      0 64800 64900 i
*> 11.1.1.0/30      15.15.2.1                      50      0 65000 65000 i
*> 11.1.1.4/30      0.0.0.0                  0         32768 i
r> 15.15.1.0/24     15.15.2.1                      50      0 65000 65000 i
*> 15.15.2.0/24     0.0.0.0                  0         32768 i
*>i20.0.0.0/30      11.1.1.6                 0    100      0 64800 i
*>i20.0.0.8/30      11.1.1.6                 0    100      0 64800 i
*                   15.15.2.1                      50      0 65000 65000 i
*>i20.0.0.12/30     11.1.1.6                 0    100      0 i
*>i20.0.1.8/30      11.1.1.6                 0    100      0 64800 64900 i
*>i20.0.1.12/30     11.1.1.6                 0    100      0 64800 64900 i
*> 192.168.1.0      15.15.2.1                     100      0 65000 65000 ?

CustomerA2#sh ip bgp neighbors 15.15.2.1  advertised-routes
BGP table version is 62, local router ID is 172.16.200.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
r>i0.0.0.0          11.1.1.6                 0    100      0 i
*>i8.8.4.4/32       11.1.1.6                 0    100      0 64800 64900 i
*>i8.8.8.8/32       11.1.1.6                 0    100      0 64800 64900 i
*>i10.0.1.0/30      11.1.1.6                 0    100      0 64800 64900 i
*>i10.0.1.4/30      11.1.1.6                 0    100      0 64800 64900 i
*> 11.1.1.4/30      0.0.0.0                  0         32768 i
*> 15.15.2.0/24     0.0.0.0                  0         32768 i
*>i20.0.0.0/30      11.1.1.6                 0    100      0 64800 i
*>i20.0.0.8/30      11.1.1.6                 0    100      0 64800 i
*>i20.0.0.12/30     11.1.1.6                 0    100      0 i
*>i20.0.1.8/30      11.1.1.6                 0    100      0 64800 64900 i
*>i20.0.1.12/30     11.1.1.6                 0    100      0 64800 64900 i

Total number of prefixes 12
CustomerA2#

```

NOTES
```
-Prefix filtering verified. CustomerA3 and CustomerA4 only advertise the
 WAN interface prefixes to SP2 (20.0.0.8/30 and 20.0.0.12/30).

-Route-map for Local Preference is working. Internet routes learned from
 SP2 are preferred through the direct edge routers instead of transiting
 through the SP1 L3VPN path.

-RIB failures ('r') appear for some internal / connected networks. This is
 normal and occurs because BGP cannot install a route already present
 in the routing table.

-Resulting traffic behavior:
  A1 → A3 → SP2 → Internet
  A2 → A4 → SP2 → Internet

-SP1 L3VPN link is used for internal connectivity only and is not
 preferred as an Internet transit path.
```
