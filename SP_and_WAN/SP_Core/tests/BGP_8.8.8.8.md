# BGP_8.8.8.8 Validation Report
Generated: 2026-03-02 13:15:17.049215

SP1-BR2#show ip bgp 8.8.8.8
```
BGP routing table entry for 8.8.8.8/32, version 7
Paths: (3 available, best #3, table Default-IP-Routing-Table)
  Advertised to update-groups:
        1    2    3
  64900, (Received from a RR-client)
    10.0.1.5 (metric 20) from 3.3.3.3 (3.3.3.3)
      Origin IGP, metric 0, localpref 100, valid, internal
  64800 64900
    20.0.1.1 from 20.0.1.1 (6.6.6.6)
      Origin IGP, localpref 100, valid, external
  64900
    10.0.1.1 from 10.0.1.1 (8.8.8.8)
      Origin IGP, metric 0, localpref 100, valid, external, best
```

SP1-BR3#show ip bgp 8.8.8.8
```
BGP routing table entry for 8.8.8.8/32, version 40
Paths: (4 available, best #1, table Default-IP-Routing-Table)
  Advertised to update-groups:
        1    2
  64900
    10.0.1.5 from 10.0.1.5 (9.9.9.9)
      Origin IGP, localpref 100, valid, external, best
  64900
    10.0.1.1 (metric 20) from 4.4.4.4 (4.4.4.4)
      Origin IGP, metric 0, localpref 100, valid, internal
      Originator: 2.2.2.2, Cluster list: 4.4.4.4
  64900
    10.0.1.1 (metric 20) from 2.2.2.2 (2.2.2.2)
      Origin IGP, metric 0, localpref 100, valid, internal
  64800 64900
    20.0.1.5 from 20.0.1.5 (7.7.7.7)
      Origin IGP, localpref 100, valid, external
```

