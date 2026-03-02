# VRF_Traceroute Validation Report
Generated: 2026-03-02 01:40:17.601550

```
SP1-PE1#traceroute vrf CUST_A 15.15.2.1

Type escape sequence to abort.
Tracing the route to 15.15.2.1

  1 10.0.0.7 [MPLS: Labels 26/0/27 Exp 0] 328 msec
    10.0.0.1 [MPLS: Labels 18/0/27 Exp 0] 80 msec
    10.0.0.7 [MPLS: Labels 26/0/27 Exp 0] 72 msec
  2 10.0.0.3 [MPLS: Labels 16/0/27 Exp 0] 108 msec
    15.15.2.1 56 msec
    10.0.0.3 [MPLS: Labels 16/0/27 Exp 0] 112 msec
```

```
SP1-PE1#traceroute vrf CUST_B 15.15.2.1

Type escape sequence to abort.
Tracing the route to 15.15.2.1

  1 10.0.0.7 [MPLS: Labels 26/0/33 Exp 0] 364 msec
    10.0.0.1 [MPLS: Labels 18/0/33 Exp 0] 56 msec
    10.0.0.7 [MPLS: Labels 26/0/33 Exp 0] 88 msec
  2 10.0.0.3 [MPLS: Labels 16/0/33 Exp 0] 64 msec
    15.15.2.1 84 msec
    10.0.0.3 [MPLS: Labels 16/0/33 Exp 0] 72 msec
```

```
SP1-PE5#traceroute vrf CUST_A 15.15.1.1

Type escape sequence to abort.
Tracing the route to 15.15.1.1

  1 10.0.0.8 [MPLS: Labels 25/0/28 Exp 0] 316 msec
    10.0.0.4 [MPLS: Labels 18/0/28 Exp 0] 56 msec
    10.0.0.8 [MPLS: Labels 25/0/28 Exp 0] 72 msec
  2 10.0.0.2 [MPLS: Labels 16/0/28 Exp 0] 112 msec
    15.15.1.1 52 msec
    10.0.0.2 [MPLS: Labels 16/0/28 Exp 0] 40 msec
```

```
SP1-PE5#traceroute vrf CUST_B 15.15.1.1

Type escape sequence to abort.
Tracing the route to 15.15.1.1

  1 10.0.0.8 [MPLS: Labels 25/0/29 Exp 0] 304 msec
    10.0.0.4 [MPLS: Labels 18/0/29 Exp 0] 56 msec
    10.0.0.8 [MPLS: Labels 25/0/29 Exp 0] 72 msec
  2 10.0.0.2 [MPLS: Labels 16/0/29 Exp 0] 96 msec
    15.15.1.1 52 msec
    10.0.0.2 [MPLS: Labels 16/0/29 Exp 0] 100 msec
```

