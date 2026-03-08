# MPLS / VPN Path Verification

## CustomerA Normal Path

<details>
<summary>CustomerA1 → 15.15.2.2</summary>

```text
CustomerA1#traceroute 15.15.2.2

Type escape sequence to abort.
Tracing the route to 15.15.2.2

  1 15.15.1.1 32 msec 40 msec 12 msec
  2 10.0.0.7 [AS 65000] [MPLS: Labels 27/0/28 Exp 0] 64 msec 80 msec 76 msec
  3 15.15.2.1 60 msec 92 msec 88 msec
  4 15.15.2.2 68 msec 80 msec 120 msec
CustomerA1#
</details> <details> <summary>CustomerA2 → 15.15.1.2</summary>
CustomerA2#traceroute 15.15.1.2

Type escape sequence to abort.
Tracing the route to 15.15.1.2

  1 15.15.2.1 60 msec 28 msec 32 msec
  2 10.0.0.8 [AS 65000] [MPLS: Labels 17/0/27 Exp 0] 84 msec 68 msec 128 msec
  3 15.15.1.1 84 msec 100 msec 84 msec
  4 15.15.1.2 108 msec 116 msec 92 msec
CustomerA2#
</details>
CustomerB Normal Path
<details> <summary>CustomerB1 → 15.15.2.2</summary>
CustomerB1#traceroute 15.15.2.2

Type escape sequence to abort.
Tracing the route to 15.15.2.2

  1 15.15.1.1 92 msec 101 msec 24 msec
  2 10.0.0.7 100 msec 72 msec 40 msec
  3 15.15.2.1 [AS 65000] 52 msec 56 msec 64 msec
  4 15.15.2.2 [AS 65000] 108 msec 157 msec 136 msec
CustomerB1#
</details> <details> <summary>CustomerB2 → 15.15.1.2</summary>
CustomerB2#traceroute 15.15.1.2

Type escape sequence to abort.
Tracing the route to 15.15.1.2

  1 15.15.2.1 40 msec 88 msec 28 msec
  2 10.0.0.8 72 msec 72 msec 60 msec
  3 15.15.1.1 [AS 65000] 92 msec 109 msec 104 msec
  4 15.15.1.2 [AS 65000] 108 msec 124 msec 120 msec
CustomerB2#
</details>
Backup Path Verification
CustomerA Backup Path
<details> <summary>CustomerA1 → 15.15.2.2</summary>
CustomerA1#traceroute 15.15.2.2

Type escape sequence to abort.
Tracing the route to 15.15.2.2

  1 15.15.1.1 56 msec 12 msec 32 msec
  2 10.0.0.7 [AS 65000] [MPLS: Labels 24/0/28 Exp 0] 80 msec 140 msec 68 msec
  3 15.15.2.1 60 msec 88 msec 80 msec
  4 15.15.2.2 28 msec 104 msec 108 msec
CustomerA1#
</details> <details> <summary>CustomerA2 → 15.15.1.2</summary>
CustomerA2#traceroute 15.15.1.2

Type escape sequence to abort.
Tracing the route to 15.15.1.2

  1 15.15.2.1 40 msec 16 msec 4 msec
  2 10.0.0.8 [AS 65000] [MPLS: Labels 26/0/27 Exp 0] 88 msec 64 msec 76 msec
  3 15.15.1.1 116 msec 84 msec 112 msec
  4 15.15.1.2 120 msec 80 msec 144 msec
CustomerA2#
</details>
CustomerB Backup Path
<details> <summary>CustomerB1 → 15.15.2.2</summary>
CustomerB1#traceroute 15.15.2.2

Type escape sequence to abort.
Tracing the route to 15.15.2.2

  1 15.15.1.1 16 msec 28 msec 44 msec
  2  *  *  *
  3 10.0.0.3 104 msec 120 msec 96 msec
  4 15.15.2.1 [AS 65000] 153 msec 120 msec 128 msec
  5 15.15.2.2 [AS 65000] 148 msec 165 msec 144 msec
CustomerB1#
</details> <details> <summary>CustomerB2 → 15.15.1.2</summary>
CustomerB2#traceroute 15.15.1.2

Type escape sequence to abort.
Tracing the route to 15.15.1.2

  1 15.15.2.1 28 msec 16 msec 16 msec
  2 10.0.0.4 145 msec 128 msec 112 msec
  3 10.0.0.2 104 msec 124 msec 125 msec
  4 15.15.1.1 [AS 65000] 124 msec 120 msec 124 msec
  5 15.15.1.2 [AS 65000] 132 msec 137 msec 148 msec
CustomerB2#
</details>
<details> <summary>Notes, Observations, and Conclusion</summary>

Notes:

Both customers traverse different paths during normal operation

MPLS labels visible for CustomerA traffic

CustomerB path does not expose MPLS labels in traceroute

Observations:

Primary paths use different P routers within the MPLS core

Backup scenario simulated by stopping a node/link in GNS3

Backup path reroutes traffic through alternate core routers

One hop shows * * * due to non-responding TTL ICMP

Conclusion:

Primary circuits maintain path separation

Backup path successfully restores connectivity

MPLS core rerouting behaves as expected in failure scenarios

</details> ```
