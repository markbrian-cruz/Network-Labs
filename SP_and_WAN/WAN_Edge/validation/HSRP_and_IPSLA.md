
CUSTOMERA3
```
CustomerA3#traceroute 192.168.2.1

Type escape sequence to abort.
Tracing the route to 192.168.2.1

  1 11.1.1.1 32 msec 28 msec 4 msec
  2 15.15.1.1 48 msec 24 msec 52 msec
  3 10.0.0.1 [AS 65000] [MPLS: Labels 26/0/55 Exp 0] 120 msec 116 msec 184 msec
  4 10.0.0.3 [AS 65000] [MPLS: Labels 26/0/55 Exp 0] 152 msec 156 msec 156 msec
  5 15.15.2.1 [AS 65000] [MPLS: Label 55 Exp 0] 132 msec 152 msec 152 msec
  6 15.15.2.2 [AS 65000] 152 msec 140 msec 164 msec
CustomerA3#
*Mar  1 03:55:16.339: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Standby -> Active
CustomerA3#sh standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    100 P Active  local           192.168.1.2     192.168.1.1
CustomerA3#traceroute 192.168.2.1

Type escape sequence to abort.
Tracing the route to 192.168.2.1

  1 11.1.1.1 24 msec 28 msec 32 msec
  2  *  *  *
  3  *  *  *
  4  *  *  *
  5  *  *  *
  6  *
    40.0.0.2 36 msec 76 msec
CustomerA3#traceroute 192.168.2.1

Type escape sequence to abort.
Tracing the route to 192.168.2.1

  1 40.0.0.2 84 msec 140 msec 116 msec
CustomerA3#
*Mar  1 03:59:22.363: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Active -> Speak
CustomerA3#
*Mar  1 03:59:32.363: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Speak -> Standby
CustomerA3#sh standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    100 P Standby 192.168.1.2     local           192.168.1.1
CustomerA3#traceroute 192.168.2.1

Type escape sequence to abort.
Tracing the route to 192.168.2.1

  1 40.0.0.2 100 msec 80 msec 88 msec
  2 192.168.2.2 92 msec 92 msec 128 msec
CustomerA3#sh standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    100 P Standby 192.168.1.2     local           192.168.1.1
CustomerA3#traceroute 192.168.2.1

Type escape sequence to abort.
Tracing the route to 192.168.2.1

  1 11.1.1.1 52 msec 40 msec 20 msec
  2 15.15.1.1 60 msec 48 msec 40 msec
  3 10.0.0.1 [AS 65000] [MPLS: Labels 26/0/55 Exp 0] 184 msec 144 msec 156 msec
  4 10.0.0.3 [AS 65000] [MPLS: Labels 21/0/55 Exp 0] 152 msec 132 msec 152 msec
  5 15.15.2.1 [AS 65000] [MPLS: Label 55 Exp 0] 140 msec 132 msec 136 msec
  6 15.15.2.2 [AS 65000] 136 msec 140 msec 152 msec
CustomerA3#
```

CUSTOMERA1
```


CustomerA1#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    110 P Active  local           192.168.1.3     192.168.1.1
CustomerA1#show track 1
Track 1
  Response Time Reporter 20 reachability
  Reachability is Up
    3 changes, last change 03:45:53
  Latest operation return code: OK
  Latest RTT (millisecs) 132
  Tracked by:
    HSRP FastEthernet1/0 1
CustomerA1#show ip sla statistics

Round Trip Time (RTT) for       Index 20
        Latest RTT: 132 milliseconds
Latest operation start time: *03:47:59.707 UTC Fri Mar 1 2002
Latest operation return code: OK
Number of successes: 287
Number of failures: 0
Operation time to live: Forever


CustomerA1#traceroute 192.168.2.1

Type escape sequence to abort.
Tracing the route to 192.168.2.1

  1 15.15.1.1 24 msec 40 msec 12 msec
  2 10.0.0.1 [AS 65000] [MPLS: Labels 26/0/55 Exp 0] 124 msec 128 msec 116 msec
  3 10.0.0.3 [AS 65000] [MPLS: Labels 26/0/55 Exp 0] 148 msec 128 msec 108 msec
  4 15.15.2.1 [MPLS: Label 55 Exp 0] 108 msec 120 msec 88 msec
  5 15.15.2.2 152 msec 156 msec 148 msec
CustomerA1#
*Mar  1 03:55:15.583: %TRACKING-5-STATE: 1 rtr 20 reachability Up->Down
CustomerA1#
*Mar  1 03:55:16.803: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Active -> Speak
CustomerA1#
*Mar  1 03:55:26.803: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Speak -> Standby
CustomerA1#
*Mar  1 03:57:12.947: %BGP-5-ADJCHANGE: neighbor 15.15.1.1 Down BGP Notification sent
CustomerA1#
*Mar  1 03:57:12.947: %BGP-3-NOTIFICATION: sent to neighbor 15.15.1.1 4/0 (hold time expired) 0 bytes
CustomerA1#traceroute 192.168.2.1

Type escape sequence to abort.
Tracing the route to 192.168.2.1

  1 192.168.1.3 72 msec 28 msec 44 msec
  2 40.0.0.2 96 msec 92 msec 104 msec
CustomerA1#
*Mar  1 03:59:20.627: %TRACKING-5-STATE: 1 rtr 20 reachability Down->Up
CustomerA1#
*Mar  1 03:59:22.787: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Standby -> Active
CustomerA1#
*Mar  1 03:59:38.679: %BGP-5-ADJCHANGE: neighbor 15.15.1.1 Up
CustomerA1#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    110 P Active  local           192.168.1.3     192.168.1.1
CustomerA1#show track 1
Track 1
  Response Time Reporter 20 reachability
  Reachability is Up
    5 changes, last change 00:01:54
  Latest operation return code: OK
  Latest RTT (millisecs) 136
  Tracked by:
    HSRP FastEthernet1/0 1
CustomerA1#show ip sla statistics

Round Trip Time (RTT) for       Index 20
        Latest RTT: 120 milliseconds
Latest operation start time: *04:01:19.707 UTC Fri Mar 1 2002
Latest operation return code: OK
Number of successes: 7
Number of failures: 0
Operation time to live: Forever


CustomerA1#traceroute 192.168.2.1

Type escape sequence to abort.
Tracing the route to 192.168.2.1

  1 15.15.1.1 28 msec 32 msec 40 msec
  2 10.0.0.1 [AS 65000] [MPLS: Labels 26/0/55 Exp 0] 112 msec 124 msec 168 msec
  3 10.0.0.3 [AS 65000] [MPLS: Labels 21/0/55 Exp 0] 120 msec 116 msec 72 msec
  4 15.15.2.1 [MPLS: Label 55 Exp 0] 124 msec 88 msec 104 msec
  5 15.15.2.2 84 msec 104 msec 104 msec
CustomerA1#
```

CUSTOMERA2
```


CustomerA2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    110 P Active  local           192.168.2.3     192.168.2.1
CustomerA2#show track 1
Track 1
  Response Time Reporter 20 reachability
  Reachability is Up
    3 changes, last change 03:51:35
  Latest operation return code: OK
  Latest RTT (millisecs) 112
  Tracked by:
    HSRP FastEthernet1/0 1
CustomerA2#show ip sla statistics

Round Trip Time (RTT) for       Index 20
        Latest RTT: 132 milliseconds
Latest operation start time: *03:53:39.155 UTC Fri Mar 1 2002
Latest operation return code: OK
Number of successes: 321
Number of failures: 0
Operation time to live: Forever


CustomerA2#traceroute
CustomerA2#traceroute 192.168.1.1

Type escape sequence to abort.
Tracing the route to 192.168.1.1

  1 15.15.2.1 20 msec 40 msec 16 msec
  2 10.0.0.4 [AS 65000] [MPLS: Labels 21/0/39 Exp 0] 144 msec 152 msec 136 msec
  3 10.0.0.2 [AS 65000] [MPLS: Labels 25/0/39 Exp 0] 104 msec 124 msec 136 msec
  4 15.15.1.1 [MPLS: Label 39 Exp 0] 100 msec 116 msec 52 msec
  5 15.15.1.2 168 msec 108 msec 116 msec
CustomerA2#
*Mar  1 03:55:18.767: %TRACKING-5-STATE: 1 rtr 20 reachability Up->Down
*Mar  1 03:55:19.395: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Active -> Speak
CustomerA2#
*Mar  1 03:55:29.395: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Speak -> Standby
CustomerA2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    90  P Standby 192.168.2.3     local           192.168.2.1
CustomerA2#show ip sla statistics

Round Trip Time (RTT) for       Index 20
        Latest RTT: NoConnection/Busy/Timeout
Latest operation start time: *03:57:09.155 UTC Fri Mar 1 2002
Latest operation return code: Timeout
Number of successes: 329
Number of failures: 13
Operation time to live: Forever


CustomerA2#show track 1
Track 1
  Response Time Reporter 20 reachability
  Reachability is Down
    4 changes, last change 00:02:10
  Latest operation return code: Timeout
  Tracked by:
    HSRP FastEthernet1/0 1
CustomerA2#traceroute 192.168.1.1

Type escape sequence to abort.
Tracing the route to 192.168.1.1

  1 192.168.2.3 56 msec 24 msec 28 msec
  2 40.0.0.1 88 msec 100 msec 80 msec
CustomerA2#
*Mar  1 03:59:13.823: %TRACKING-5-STATE: 1 rtr 20 reachability Down->Up
CustomerA2#
*Mar  1 03:59:16.343: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Standby -> Active
CustomerA2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    110 P Active  local           192.168.2.3     192.168.2.1
CustomerA2#show track 1
Track 1
  Response Time Reporter 20 reachability
  Reachability is Up
    5 changes, last change 00:02:28
  Latest operation return code: OK
  Latest RTT (millisecs) 112
  Tracked by:
    HSRP FastEthernet1/0 1
CustomerA2#show ip sla statistics

Round Trip Time (RTT) for       Index 20
        Latest RTT: 136 milliseconds
Latest operation start time: *04:01:39.155 UTC Fri Mar 1 2002
Latest operation return code: OK
Number of successes: 9
Number of failures: 0
Operation time to live: Forever


CustomerA2#traceroute 192.168.1.1

Type escape sequence to abort.
Tracing the route to 192.168.1.1

  1 15.15.2.1 40 msec 28 msec 16 msec
  2 10.0.0.8 [AS 65000] [MPLS: Labels 17/0/48 Exp 0] 100 msec 88 msec 92 msec
  3 15.15.1.1 [MPLS: Label 48 Exp 0] 124 msec 80 msec 80 msec
  4 15.15.1.2 140 msec 104 msec 116 msec
CustomerA2#
```

CUSTOMERA4
```
CustomerA4#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    100 P Standby 192.168.2.2     local           192.168.2.1
CustomerA4#traceroute 192.168.1.1

Type escape sequence to abort.
Tracing the route to 192.168.1.1

  1 11.1.1.5 16 msec 52 msec 52 msec
  2 15.15.2.1 76 msec 72 msec 44 msec
  3 10.0.0.8 [AS 65000] [MPLS: Labels 27/0/39 Exp 0] 140 msec 88 msec 116 msec
  4 15.15.1.1 [AS 65000] [MPLS: Label 39 Exp 0] 96 msec 60 msec 104 msec
  5 15.15.1.2 [AS 65000] 128 msec 120 msec 128 msec
CustomerA4#
*Mar  1 03:55:23.871: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Standby -> Active
CustomerA4#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    100 P Active  local           192.168.2.2     192.168.2.1
CustomerA4#traceroute 192.168.1.1

Type escape sequence to abort.
Tracing the route to 192.168.1.1

  1 40.0.0.1 80 msec 92 msec 56 msec
CustomerA4#
*Mar  1 03:59:20.899: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Active -> Speak
CustomerA4#
*Mar  1 03:59:30.899: %HSRP-5-STATECHANGE: FastEthernet1/0 Grp 1 state Speak -> Standby
CustomerA4#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa1/0       1    100 P Standby 192.168.2.2     local           192.168.2.1
CustomerA4#traceroute 192.168.1.1

Type escape sequence to abort.
Tracing the route to 192.168.1.1

  1 11.1.1.5 40 msec 28 msec 28 msec
  2 15.15.2.1 52 msec 72 msec 36 msec
  3 10.0.0.4 [AS 65000] [MPLS: Labels 27/0/48 Exp 0] 152 msec 160 msec 128 msec
  4 10.0.0.2 [AS 65000] [MPLS: Labels 16/0/48 Exp 0] 168 msec 116 msec 156 msec
  5 15.15.1.1 [AS 65000] [MPLS: Label 48 Exp 0] 96 msec 148 msec 104 msec
  6 15.15.1.2 [AS 65000] 152 msec 128 msec 156 msec
CustomerA4#
```

UBUNTU SERVER
```

$ traceroute 192.168.2.1
traceroute to 192.168.2.1 (192.168.2.1), 30 hops max, 60 byte packets
 1  192.168.1.2 (192.168.1.2)  51.753 ms  50.929 ms  50.819 ms
 2  15.15.1.1 (15.15.1.1)  80.912 ms  111.532 ms  130.846 ms
 3  10.0.0.7 (10.0.0.7)  247.363 ms  267.194 ms  313.357 ms
 4  15.15.2.1 (15.15.2.1)  247.285 ms  313.282 ms  328.731 ms
 5  15.15.2.2 (15.15.2.2)  372.714 ms  405.144 ms  405.094 ms
$
$
$
$
$
$ traceroute 192.168.2.1
traceroute to 192.168.2.1 (192.168.2.1), 30 hops max, 60 byte packets
 1  192.168.1.2 (192.168.1.2)  16.058 ms  13.700 ms  13.496 ms
 2  15.15.1.1 (15.15.1.1)  39.833 ms  39.518 ms  71.508 ms
 3  10.0.0.7 (10.0.0.7)  200.326 ms  200.076 ms  225.370 ms
 4  15.15.2.1 (15.15.2.1)  176.531 ms  199.196 ms  198.894 ms
 5  15.15.2.2 (15.15.2.2)  270.276 ms  270.010 ms  316.045 ms
$ ping 192.168.2.1
PING 192.168.2.1 (192.168.2.1) 56(84) bytes of data.
64 bytes from 192.168.2.1: icmp_seq=1 ttl=250 time=125 ms
64 bytes from 192.168.2.1: icmp_seq=2 ttl=250 time=121 ms
64 bytes from 192.168.2.1: icmp_seq=3 ttl=250 time=127 ms
64 bytes from 192.168.2.1: icmp_seq=4 ttl=250 time=144 ms
64 bytes from 192.168.2.1: icmp_seq=5 ttl=250 time=118 ms
64 bytes from 192.168.2.1: icmp_seq=6 ttl=250 time=104 ms
64 bytes from 192.168.2.1: icmp_seq=7 ttl=250 time=119 ms
64 bytes from 192.168.2.1: icmp_seq=8 ttl=250 time=142 ms
64 bytes from 192.168.2.1: icmp_seq=135 ttl=254 time=101 ms
64 bytes from 192.168.2.1: icmp_seq=136 ttl=254 time=111 ms
64 bytes from 192.168.2.1: icmp_seq=137 ttl=254 time=85.4 ms
64 bytes from 192.168.2.1: icmp_seq=138 ttl=254 time=111 ms
64 bytes from 192.168.2.1: icmp_seq=139 ttl=254 time=102 ms
64 bytes from 192.168.2.1: icmp_seq=141 ttl=254 time=90.3 ms
64 bytes from 192.168.2.1: icmp_seq=142 ttl=254 time=97.0 ms
64 bytes from 192.168.2.1: icmp_seq=143 ttl=254 time=71.6 ms
64 bytes from 192.168.2.1: icmp_seq=145 ttl=254 time=94.1 ms
64 bytes from 192.168.2.1: icmp_seq=146 ttl=254 time=86.7 ms
64 bytes from 192.168.2.1: icmp_seq=147 ttl=254 time=76.4 ms
64 bytes from 192.168.2.1: icmp_seq=148 ttl=254 time=54.3 ms
64 bytes from 192.168.2.1: icmp_seq=149 ttl=254 time=91.8 ms
64 bytes from 192.168.2.1: icmp_seq=150 ttl=254 time=106 ms
64 bytes from 192.168.2.1: icmp_seq=151 ttl=254 time=89.4 ms
64 bytes from 192.168.2.1: icmp_seq=152 ttl=254 time=103 ms
64 bytes from 192.168.2.1: icmp_seq=153 ttl=254 time=104 ms
64 bytes from 192.168.2.1: icmp_seq=154 ttl=254 time=102 ms
64 bytes from 192.168.2.1: icmp_seq=155 ttl=254 time=102 ms
64 bytes from 192.168.2.1: icmp_seq=156 ttl=254 time=71.3 ms
64 bytes from 192.168.2.1: icmp_seq=157 ttl=254 time=80.6 ms
64 bytes from 192.168.2.1: icmp_seq=158 ttl=254 time=55.8 ms
64 bytes from 192.168.2.1: icmp_seq=159 ttl=254 time=75.8 ms
64 bytes from 192.168.2.1: icmp_seq=160 ttl=254 time=108 ms
64 bytes from 192.168.2.1: icmp_seq=161 ttl=254 time=106 ms
64 bytes from 192.168.2.1: icmp_seq=162 ttl=254 time=85.7 ms
64 bytes from 192.168.2.1: icmp_seq=163 ttl=254 time=73.1 ms
64 bytes from 192.168.2.1: icmp_seq=164 ttl=254 time=78.2 ms
64 bytes from 192.168.2.1: icmp_seq=166 ttl=254 time=80.1 ms
64 bytes from 192.168.2.1: icmp_seq=167 ttl=254 time=88.2 ms
64 bytes from 192.168.2.1: icmp_seq=168 ttl=254 time=130 ms
64 bytes from 192.168.2.1: icmp_seq=170 ttl=254 time=74.9 ms
64 bytes from 192.168.2.1: icmp_seq=171 ttl=254 time=77.8 ms
64 bytes from 192.168.2.1: icmp_seq=172 ttl=254 time=93.1 ms
64 bytes from 192.168.2.1: icmp_seq=173 ttl=254 time=87.9 ms
64 bytes from 192.168.2.1: icmp_seq=174 ttl=254 time=84.8 ms
64 bytes from 192.168.2.1: icmp_seq=175 ttl=254 time=83.7 ms
64 bytes from 192.168.2.1: icmp_seq=176 ttl=254 time=90.5 ms
64 bytes from 192.168.2.1: icmp_seq=177 ttl=254 time=109 ms
64 bytes from 192.168.2.1: icmp_seq=178 ttl=254 time=102 ms
64 bytes from 192.168.2.1: icmp_seq=179 ttl=254 time=96.1 ms
64 bytes from 192.168.2.1: icmp_seq=180 ttl=254 time=104 ms
64 bytes from 192.168.2.1: icmp_seq=181 ttl=254 time=91.1 ms
64 bytes from 192.168.2.1: icmp_seq=182 ttl=254 time=87.7 ms
64 bytes from 192.168.2.1: icmp_seq=183 ttl=254 time=98.9 ms

--- 192.168.2.1 ping statistics ---^C
183 packets transmitted, 53 received, 71.0383% packet loss, time 185214ms
rtt min/avg/max/mdev = 54.300/96.098/144.414/18.850 ms
$ traceroute 192.168.2.1
traceroute to 192.168.2.1 (192.168.2.1), 30 hops max, 60 byte packets
 1  192.168.1.3 (192.168.1.3)  11.294 ms  24.200 ms  23.959 ms
 2  40.0.0.2 (40.0.0.2)  89.438 ms  114.654 ms  128.940 ms
$ ping 192.168.2.1
PING 192.168.2.1 (192.168.2.1) 56(84) bytes of data.
64 bytes from 192.168.2.1: icmp_seq=1 ttl=254 time=162 ms
64 bytes from 192.168.2.1: icmp_seq=2 ttl=254 time=85.7 ms
64 bytes from 192.168.2.1: icmp_seq=3 ttl=254 time=98.2 ms
64 bytes from 192.168.2.1: icmp_seq=4 ttl=254 time=79.6 ms
64 bytes from 192.168.2.1: icmp_seq=5 ttl=254 time=61.7 ms
64 bytes from 192.168.2.1: icmp_seq=6 ttl=254 time=76.2 ms
64 bytes from 192.168.2.1: icmp_seq=7 ttl=254 time=102 ms
64 bytes from 192.168.2.1: icmp_seq=8 ttl=254 time=94.6 ms
64 bytes from 192.168.2.1: icmp_seq=9 ttl=254 time=87.3 ms
64 bytes from 192.168.2.1: icmp_seq=10 ttl=254 time=83.8 ms
64 bytes from 192.168.2.1: icmp_seq=12 ttl=254 time=90.6 ms
64 bytes from 192.168.2.1: icmp_seq=14 ttl=254 time=105 ms
64 bytes from 192.168.2.1: icmp_seq=15 ttl=254 time=94.6 ms
64 bytes from 192.168.2.1: icmp_seq=16 ttl=254 time=96.4 ms
64 bytes from 192.168.2.1: icmp_seq=17 ttl=254 time=87.5 ms
64 bytes from 192.168.2.1: icmp_seq=18 ttl=254 time=167 ms
64 bytes from 192.168.2.1: icmp_seq=19 ttl=254 time=180 ms
64 bytes from 192.168.2.1: icmp_seq=20 ttl=254 time=81.5 ms
64 bytes from 192.168.2.1: icmp_seq=21 ttl=254 time=105 ms
64 bytes from 192.168.2.1: icmp_seq=22 ttl=254 time=86.0 ms
64 bytes from 192.168.2.1: icmp_seq=23 ttl=254 time=94.5 ms
64 bytes from 192.168.2.1: icmp_seq=24 ttl=254 time=84.4 ms
64 bytes from 192.168.2.1: icmp_seq=25 ttl=254 time=102 ms
64 bytes from 192.168.2.1: icmp_seq=27 ttl=253 time=121 ms
64 bytes from 192.168.2.1: icmp_seq=28 ttl=253 time=174 ms
64 bytes from 192.168.2.1: icmp_seq=29 ttl=253 time=117 ms
64 bytes from 192.168.2.1: icmp_seq=30 ttl=253 time=107 ms
64 bytes from 192.168.2.1: icmp_seq=31 ttl=253 time=126 ms
64 bytes from 192.168.2.1: icmp_seq=32 ttl=253 time=97.7 ms
64 bytes from 192.168.2.1: icmp_seq=33 ttl=253 time=135 ms
64 bytes from 192.168.2.1: icmp_seq=34 ttl=253 time=134 ms
64 bytes from 192.168.2.1: icmp_seq=35 ttl=253 time=154 ms
64 bytes from 192.168.2.1: icmp_seq=36 ttl=253 time=122 ms
64 bytes from 192.168.2.1: icmp_seq=37 ttl=253 time=155 ms
64 bytes from 192.168.2.1: icmp_seq=38 ttl=253 time=155 ms
64 bytes from 192.168.2.1: icmp_seq=39 ttl=253 time=151 ms
64 bytes from 192.168.2.1: icmp_seq=40 ttl=253 time=134 ms
64 bytes from 192.168.2.1: icmp_seq=41 ttl=253 time=123 ms
64 bytes from 192.168.2.1: icmp_seq=43 ttl=253 time=132 ms
64 bytes from 192.168.2.1: icmp_seq=44 ttl=253 time=138 ms
64 bytes from 192.168.2.1: icmp_seq=45 ttl=253 time=133 ms
64 bytes from 192.168.2.1: icmp_seq=46 ttl=253 time=152 ms
64 bytes from 192.168.2.1: icmp_seq=47 ttl=253 time=150 ms
64 bytes from 192.168.2.1: icmp_seq=48 ttl=253 time=140 ms
64 bytes from 192.168.2.1: icmp_seq=49 ttl=253 time=145 ms
64 bytes from 192.168.2.1: icmp_seq=50 ttl=253 time=114 ms
64 bytes from 192.168.2.1: icmp_seq=51 ttl=253 time=156 ms
64 bytes from 192.168.2.1: icmp_seq=52 ttl=253 time=101 ms
64 bytes from 192.168.2.1: icmp_seq=53 ttl=253 time=129 ms
64 bytes from 192.168.2.1: icmp_seq=54 ttl=253 time=147 ms
64 bytes from 192.168.2.1: icmp_seq=55 ttl=253 time=154 ms
64 bytes from 192.168.2.1: icmp_seq=56 ttl=253 time=162 ms
64 bytes from 192.168.2.1: icmp_seq=57 ttl=253 time=107 ms
64 bytes from 192.168.2.1: icmp_seq=58 ttl=253 time=136 ms
64 bytes from 192.168.2.1: icmp_seq=59 ttl=253 time=129 ms
64 bytes from 192.168.2.1: icmp_seq=60 ttl=253 time=148 ms
64 bytes from 192.168.2.1: icmp_seq=61 ttl=253 time=128 ms
64 bytes from 192.168.2.1: icmp_seq=63 ttl=253 time=130 ms
64 bytes from 192.168.2.1: icmp_seq=64 ttl=253 time=149 ms
64 bytes from 192.168.2.1: icmp_seq=65 ttl=253 time=149 ms
64 bytes from 192.168.2.1: icmp_seq=66 ttl=253 time=154 ms
64 bytes from 192.168.2.1: icmp_seq=67 ttl=253 time=116 ms
64 bytes from 192.168.2.1: icmp_seq=68 ttl=253 time=152 ms
64 bytes from 192.168.2.1: icmp_seq=69 ttl=253 time=153 ms
64 bytes from 192.168.2.1: icmp_seq=71 ttl=253 time=128 ms
64 bytes from 192.168.2.1: icmp_seq=72 ttl=253 time=135 ms
64 bytes from 192.168.2.1: icmp_seq=73 ttl=253 time=170 ms
64 bytes from 192.168.2.1: icmp_seq=74 ttl=253 time=128 ms
64 bytes from 192.168.2.1: icmp_seq=75 ttl=253 time=146 ms
64 bytes from 192.168.2.1: icmp_seq=76 ttl=253 time=150 ms
64 bytes from 192.168.2.1: icmp_seq=77 ttl=253 time=140 ms
64 bytes from 192.168.2.1: icmp_seq=78 ttl=253 time=137 ms
64 bytes from 192.168.2.1: icmp_seq=79 ttl=253 time=131 ms
64 bytes from 192.168.2.1: icmp_seq=80 ttl=253 time=157 ms
64 bytes from 192.168.2.1: icmp_seq=81 ttl=253 time=164 ms
64 bytes from 192.168.2.1: icmp_seq=82 ttl=253 time=152 ms
64 bytes from 192.168.2.1: icmp_seq=83 ttl=253 time=158 ms
64 bytes from 192.168.2.1: icmp_seq=84 ttl=253 time=159 ms
64 bytes from 192.168.2.1: icmp_seq=85 ttl=253 time=131 ms
64 bytes from 192.168.2.1: icmp_seq=87 ttl=253 time=150 ms
64 bytes from 192.168.2.1: icmp_seq=88 ttl=253 time=111 ms
64 bytes from 192.168.2.1: icmp_seq=89 ttl=253 time=131 ms
64 bytes from 192.168.2.1: icmp_seq=90 ttl=253 time=135 ms
64 bytes from 192.168.2.1: icmp_seq=91 ttl=253 time=138 ms
64 bytes from 192.168.2.1: icmp_seq=92 ttl=253 time=152 ms
64 bytes from 192.168.2.1: icmp_seq=93 ttl=253 time=126 ms
64 bytes from 192.168.2.1: icmp_seq=95 ttl=253 time=133 ms
64 bytes from 192.168.2.1: icmp_seq=96 ttl=253 time=135 ms
64 bytes from 192.168.2.1: icmp_seq=97 ttl=253 time=131 ms
64 bytes from 192.168.2.1: icmp_seq=98 ttl=253 time=109 ms
64 bytes from 192.168.2.1: icmp_seq=99 ttl=253 time=175 ms
64 bytes from 192.168.2.1: icmp_seq=100 ttl=253 time=125 ms
64 bytes from 192.168.2.1: icmp_seq=101 ttl=251 time=134 ms
64 bytes from 192.168.2.1: icmp_seq=102 ttl=251 time=119 ms
64 bytes from 192.168.2.1: icmp_seq=103 ttl=251 time=109 ms
64 bytes from 192.168.2.1: icmp_seq=104 ttl=251 time=112 ms
64 bytes from 192.168.2.1: icmp_seq=105 ttl=251 time=131 ms
64 bytes from 192.168.2.1: icmp_seq=106 ttl=251 time=126 ms
64 bytes from 192.168.2.1: icmp_seq=107 ttl=251 time=129 ms
64 bytes from 192.168.2.1: icmp_seq=108 ttl=251 time=120 ms
64 bytes from 192.168.2.1: icmp_seq=109 ttl=251 time=151 ms
64 bytes from 192.168.2.1: icmp_seq=110 ttl=251 time=128 ms
64 bytes from 192.168.2.1: icmp_seq=111 ttl=251 time=117 ms
64 bytes from 192.168.2.1: icmp_seq=112 ttl=251 time=139 ms
64 bytes from 192.168.2.1: icmp_seq=113 ttl=251 time=155 ms
64 bytes from 192.168.2.1: icmp_seq=114 ttl=251 time=140 ms
64 bytes from 192.168.2.1: icmp_seq=115 ttl=251 time=155 ms
64 bytes from 192.168.2.1: icmp_seq=116 ttl=251 time=126 ms
64 bytes from 192.168.2.1: icmp_seq=117 ttl=251 time=129 ms
64 bytes from 192.168.2.1: icmp_seq=118 ttl=251 time=101 ms
64 bytes from 192.168.2.1: icmp_seq=119 ttl=251 time=124 ms
64 bytes from 192.168.2.1: icmp_seq=120 ttl=251 time=111 ms
64 bytes from 192.168.2.1: icmp_seq=121 ttl=251 time=121 ms
64 bytes from 192.168.2.1: icmp_seq=122 ttl=251 time=138 ms
64 bytes from 192.168.2.1: icmp_seq=123 ttl=251 time=127 ms
64 bytes from 192.168.2.1: icmp_seq=124 ttl=251 time=148 ms
64 bytes from 192.168.2.1: icmp_seq=125 ttl=251 time=150 ms
64 bytes from 192.168.2.1: icmp_seq=126 ttl=251 time=150 ms
64 bytes from 192.168.2.1: icmp_seq=127 ttl=251 time=128 ms
64 bytes from 192.168.2.1: icmp_seq=128 ttl=251 time=134 ms
64 bytes from 192.168.2.1: icmp_seq=129 ttl=251 time=125 ms
64 bytes from 192.168.2.1: icmp_seq=130 ttl=251 time=147 ms
64 bytes from 192.168.2.1: icmp_seq=131 ttl=251 time=137 ms
64 bytes from 192.168.2.1: icmp_seq=132 ttl=251 time=137 ms
64 bytes from 192.168.2.1: icmp_seq=133 ttl=251 time=126 ms
64 bytes from 192.168.2.1: icmp_seq=134 ttl=251 time=147 ms
64 bytes from 192.168.2.1: icmp_seq=135 ttl=251 time=122 ms
64 bytes from 192.168.2.1: icmp_seq=136 ttl=251 time=169 ms
64 bytes from 192.168.2.1: icmp_seq=137 ttl=251 time=104 ms
64 bytes from 192.168.2.1: icmp_seq=138 ttl=251 time=127 ms
64 bytes from 192.168.2.1: icmp_seq=139 ttl=251 time=132 ms
64 bytes from 192.168.2.1: icmp_seq=140 ttl=251 time=120 ms
64 bytes from 192.168.2.1: icmp_seq=141 ttl=251 time=138 ms
64 bytes from 192.168.2.1: icmp_seq=142 ttl=251 time=114 ms
64 bytes from 192.168.2.1: icmp_seq=143 ttl=251 time=145 ms
64 bytes from 192.168.2.1: icmp_seq=144 ttl=251 time=148 ms
64 bytes from 192.168.2.1: icmp_seq=145 ttl=251 time=148 ms
64 bytes from 192.168.2.1: icmp_seq=146 ttl=251 time=130 ms
64 bytes from 192.168.2.1: icmp_seq=147 ttl=251 time=133 ms
64 bytes from 192.168.2.1: icmp_seq=148 ttl=251 time=110 ms
64 bytes from 192.168.2.1: icmp_seq=149 ttl=251 time=155 ms
64 bytes from 192.168.2.1: icmp_seq=150 ttl=251 time=101 ms
64 bytes from 192.168.2.1: icmp_seq=151 ttl=251 time=133 ms
64 bytes from 192.168.2.1: icmp_seq=152 ttl=251 time=112 ms
64 bytes from 192.168.2.1: icmp_seq=153 ttl=251 time=151 ms
64 bytes from 192.168.2.1: icmp_seq=154 ttl=251 time=155 ms
64 bytes from 192.168.2.1: icmp_seq=155 ttl=251 time=144 ms
64 bytes from 192.168.2.1: icmp_seq=156 ttl=251 time=145 ms
64 bytes from 192.168.2.1: icmp_seq=157 ttl=251 time=103 ms
64 bytes from 192.168.2.1: icmp_seq=158 ttl=251 time=96.8 ms
^C
--- 192.168.2.1 ping statistics ---
158 packets transmitted, 150 received, 5.06329% packet loss, time 157565ms
rtt min/avg/max/mdev = 61.657/129.727/179.866/23.052 ms
$ traceroute 192.168.2.1
traceroute to 192.168.2.1 (192.168.2.1), 30 hops max, 60 byte packets
 1  192.168.1.2 (192.168.1.2)  11.669 ms  11.554 ms  11.687 ms
 2  15.15.1.1 (15.15.1.1)  42.886 ms  42.823 ms  72.810 ms
 3  10.0.0.1 (10.0.0.1)  213.775 ms  213.729 ms  228.706 ms
 4  10.0.0.3 (10.0.0.3)  228.654 ms  246.335 ms  293.032 ms
 5  15.15.2.1 (15.15.2.1)  276.192 ms  292.903 ms  319.507 ms
 6  15.15.2.2 (15.15.2.2)  334.201 ms  327.667 ms  345.016 ms
$
```


NOTES:
```
HSRP behavior validated on both customer sites.

IP SLA is configured to track reachability of the primary MPLS path. When the
tracked object fails, the HSRP priority is reduced which causes the standby
router to become the active gateway.

Failure scenario simulated in the Service Provider network which caused:

IP SLA reachability failure

Tracking state change

HSRP active router transition

Traffic then shifted to the backup path through the alternative WAN link
(40.0.0.x network). Traceroute outputs confirm the change in forwarding path.

During the initial convergence event, the Ubuntu continuous ping experienced
temporary packet loss (~71%), which reflects normal convergence delay caused
by the following sequence:

IP SLA failure detection

Track state change

HSRP role transition

Routing table update

Traffic redirection to backup path

After the primary path recovered, IP SLA detected reachability restoration.
HSRP preemption returned the router to its original active role and traffic
was again forwarded through the MPLS core.

End-to-end connectivity was successfully restored in both directions.
```
