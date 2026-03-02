# BGP_8.8.8.8 Validation Report
Generated: 2026-03-02 01:19:15.561871

## SP1-PE1
Router: SP1-PE1
Command: show ip bgp 8.8.8.8
```
BGP routing table entry for 8.8.8.8/32, version 84
Paths: (2 available, best #1, table Default-IP-Routing-Table)
  Not advertised to any peer
  64900
    10.0.1.1 (metric 20) from 2.2.2.2 (2.2.2.2)
      Origin IGP, metric 0, localpref 100, valid, internal, best
  64900
    10.0.1.1 (metric 20) from 4.4.4.4 (4.4.4.4)
      Origin IGP, metric 0, localpref 100, valid, internal
      Originator: 2.2.2.2, Cluster list: 4.4.4.4
```

## SP1-PE5
Router: SP1-PE5
Command: show ip bgp 8.8.8.8
```
BGP routing table entry for 8.8.8.8/32, version 33
Paths: (2 available, best #2, table Default-IP-Routing-Table)
  Not advertised to any peer
  64900
    10.0.1.1 (metric 30) from 4.4.4.4 (4.4.4.4)
      Origin IGP, metric 0, localpref 100, valid, internal
      Originator: 2.2.2.2, Cluster list: 4.4.4.4
  64900
    10.0.1.1 (metric 30) from 2.2.2.2 (2.2.2.2)
      Origin IGP, metric 0, localpref 100, valid, internal, best
```

