# VRF_Traceroute Validation Report
Generated: 2026-03-02 01:03:04.193990

## SP1-PE1
Router: SP1-PE1
Command: traceroute vrf CUST_A 15.15.2.1
```

Type escape sequence to abort.
Tracing the route to 15.15.2.1

  1 10.0.0.7 [MPLS: Labels 26/0/27 Exp 0] 344 msec
    10.0.0.1 [MPLS: Labels 18/0/27 Exp 0] 60 msec
    10.0.0.7 [MPLS: Labels 26/0/27 Exp 0] 92 msec
  2 10.0.0.3 [MPLS: Labels 16/0/27 Exp 0] 56 msec
    15.15.2.1 80 msec
    10.0.0.3 [MPLS: Labels 16/0/27 Exp 0] 60 msec
```

## SP1-PE1
Router: SP1-PE1
Command: traceroute vrf CUST_B 15.15.2.1
```

Type escape sequence to abort.
Tracing the route to 15.15.2.1

  1 10.0.0.7 [MPLS: Labels 26/0/33 Exp 0] 324 msec
    10.0.0.1 [MPLS: Labels 18/0/33 Exp 0] 64 msec
    10.0.0.7 [MPLS: Labels 26/0/33 Exp 0] 60 msec
  2 10.0.0.3 [MPLS: Labels 16/0/33 Exp 0] 88 msec
    15.15.2.1 56 msec
    10.0.0.3 [MPLS: Labels 16/0/33 Exp 0] 92 msec
```

## SP1-PE5
Router: SP1-PE5
Command: traceroute vrf CUST_A 15.15.1.1
```

Type escape sequence to abort.
Tracing the route to 15.15.1.1

  1 10.0.0.8 [MPLS: Labels 25/0/28 Exp 0] 348 msec
    10.0.0.4 [MPLS: Labels 18/0/28 Exp 0] 60 msec
    10.0.0.8 [MPLS: Labels 25/0/28 Exp 0] 72 msec
  2 10.0.0.2 [MPLS: Labels 16/0/28 Exp 0] 64 msec
    15.15.1.1 80 msec
    10.0.0.2 [MPLS: Labels 16/0/28 Exp 0] 100 msec
```

## SP1-PE5
Router: SP1-PE5
Command: traceroute vrf CUST_B 15.15.1.1
```

Type escape sequence to abort.
Tracing the route to 15.15.1.1

  1 10.0.0.8 [MPLS: Labels 25/0/29 Exp 0] 308 msec
    10.0.0.4 [MPLS: Labels 18/0/29 Exp 0] 52 msec
    10.0.0.8 [MPLS: Labels 25/0/29 Exp 0] 60 msec
  2 10.0.0.2 [MPLS: Labels 16/0/29 Exp 0] 84 msec
    15.15.1.1 56 msec
    10.0.0.2 [MPLS: Labels 16/0/29 Exp 0] 60 msec
```

