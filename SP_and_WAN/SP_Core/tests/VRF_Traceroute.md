# VRF_Traceroute Validation Report
Generated: 2026-03-02 13:15:17.049107

SP1-PE1 - CUST_A#traceroute vrf CUST_A 15.15.2.1
```

Type escape sequence to abort.
Tracing the route to 15.15.2.1

  1 10.0.0.7 [MPLS: Labels 25/0/28 Exp 0] 364 msec
    10.0.0.1 [MPLS: Labels 25/0/28 Exp 0] 52 msec
    10.0.0.7 [MPLS: Labels 25/0/28 Exp 0] 56 msec
  2 10.0.0.3 [MPLS: Labels 25/0/28 Exp 0] 100 msec
    15.15.2.1 [AS 64850] 68 msec
    10.0.0.3 [MPLS: Labels 25/0/28 Exp 0] 68 msec
```

SP1-PE1 - CUST_B#traceroute vrf CUST_B 15.15.2.1
```

Type escape sequence to abort.
Tracing the route to 15.15.2.1

  1 10.0.0.7 [MPLS: Labels 25/0/26 Exp 0] 344 msec
    10.0.0.1 [MPLS: Labels 25/0/26 Exp 0] 76 msec
    10.0.0.7 [MPLS: Labels 25/0/26 Exp 0] 52 msec
  2 10.0.0.3 [MPLS: Labels 25/0/26 Exp 0] 68 msec
    15.15.2.1 [AS 64850] 60 msec
    10.0.0.3 [MPLS: Labels 25/0/26 Exp 0] 56 msec
```

SP1-PE5 - CUST_A#traceroute vrf CUST_A 15.15.1.1
```

Type escape sequence to abort.
Tracing the route to 15.15.1.1

  1 10.0.0.8 [MPLS: Labels 28/0/27 Exp 0] 332 msec
    10.0.0.4 [MPLS: Labels 26/0/27 Exp 0] 56 msec
    10.0.0.8 [MPLS: Labels 28/0/27 Exp 0] 68 msec
  2 10.0.0.2 [MPLS: Labels 26/0/27 Exp 0] 84 msec
    15.15.1.1 [AS 64850] 68 msec
    10.0.0.2 [MPLS: Labels 26/0/27 Exp 0] 112 msec
```

SP1-PE5 - CUST_B#traceroute vrf CUST_B 15.15.1.1
```

Type escape sequence to abort.
Tracing the route to 15.15.1.1

  1 10.0.0.8 [MPLS: Labels 28/0/26 Exp 0] 332 msec
    10.0.0.4 [MPLS: Labels 26/0/26 Exp 0] 52 msec
    10.0.0.8 [MPLS: Labels 28/0/26 Exp 0] 52 msec
  2 10.0.0.2 [MPLS: Labels 26/0/26 Exp 0] 76 msec
    15.15.1.1 [AS 64850] 52 msec
    10.0.0.2 [MPLS: Labels 26/0/26 Exp 0] 72 msec
```

