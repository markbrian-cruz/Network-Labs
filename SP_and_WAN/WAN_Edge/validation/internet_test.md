CustomerA1# ping 8.8.8.8 repeat 5

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 60/80/108 ms

CustomerA1# traceroute 8.8.8.8

Type escape sequence to abort.
Tracing the route to 8.8.8.8

  1 11.1.1.2 16 msec 24 msec 24 msec
  2 20.0.0.9 [AS 64800] 56 msec 40 msec 60 msec
  3 20.0.1.10 [AS 64900] 100 msec 100 msec 88 msec

CustomerA1# show ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is 0.0.0.0 to network 0.0.0.0

     1.0.0.0/32 is subnetted, 1 subnets
C       1.1.1.1 is directly connected, Loopback0
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [20/0] via 15.15.1.1, 00:20:24
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [200/0] via 11.1.1.2, 02:47:13
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [20/0] via 15.15.1.1, 00:17:21
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [200/0] via 11.1.1.2, 02:47:13
B       20.0.0.0 [200/0] via 11.1.1.2, 02:47:13
B       20.0.1.0 [200/0] via 11.1.1.2, 02:46:47
B       20.0.0.12 [200/0] via 11.1.1.2, 02:47:13
B       20.0.1.12 [200/0] via 11.1.1.2, 02:47:13
B       20.0.0.8 [200/0] via 11.1.1.2, 02:47:13
B       20.0.1.8 [200/0] via 11.1.1.2, 02:47:13
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [200/0] via 11.1.1.2, 02:46:47
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [200/0] via 11.1.1.2, 02:46:47
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [200/0] via 11.1.1.2, 02:47:13
B       8.8.4.4 [200/0] via 11.1.1.2, 02:47:13
     40.0.0.0/30 is subnetted, 1 subnets
O       40.0.0.0 [250/1001] via 192.168.1.3, 02:46:57, FastEthernet1/0
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [200/0] via 11.1.1.2, 02:46:47
B       10.0.0.2/31 [200/0] via 11.1.1.2, 02:47:13
B       10.0.0.0/31 [200/0] via 11.1.1.2, 02:46:47
B       10.0.1.0/30 [200/0] via 11.1.1.2, 02:47:13
B       10.0.0.6/31 [200/0] via 11.1.1.2, 02:46:47
B       10.0.0.4/31 [200/0] via 11.1.1.2, 02:47:13
B       10.0.1.4/30 [200/0] via 11.1.1.2, 02:47:13
     11.0.0.0/30 is subnetted, 2 subnets
C       11.1.1.0 is directly connected, FastEthernet0/1
B       11.1.1.4 [20/0] via 15.15.1.1, 00:20:18
C    192.168.1.0/24 is directly connected, FastEthernet1/0
O    192.168.2.0/24 [250/1002] via 192.168.1.3, 00:16:50, FastEthernet1/0
     15.0.0.0/24 is subnetted, 2 subnets
C       15.15.1.0 is directly connected, FastEthernet0/0
S       15.15.2.0 [1/0] via 15.15.1.1, FastEthernet0/0
S*   0.0.0.0/0 is directly connected, FastEthernet0/1

CustomerA2# ping 8.8.8.8 repeat 5

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 148/216/348 ms

CustomerA2# traceroute 8.8.8.8

Type escape sequence to abort.
Tracing the route to 8.8.8.8

  1 15.15.2.1 228 msec 36 msec 88 msec
  2 10.0.0.4 [AS 65000] [MPLS: Labels 21/0/29 Exp 0] 164 msec 120 msec 144 msec
  3 10.0.0.2 [AS 65000] [MPLS: Labels 21/0/29 Exp 0] 140 msec 132 msec 168 msec
  4 15.15.1.1 [MPLS: Label 29 Exp 0] 120 msec 116 msec 120 msec
  5 15.15.1.2 164 msec 132 msec 148 msec
  6 11.1.1.2 [AS 65000] 172 msec 132 msec 196 msec
  7 20.0.0.9 [AS 64800] 164 msec 148 msec 152 msec
  8 20.0.1.10 [AS 64900] 204 msec 160 msec 208 msec

CustomerA2# show ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is 0.0.0.0 to network 0.0.0.0

     1.0.0.0/32 is subnetted, 1 subnets
B       1.1.1.1 [20/0] via 15.15.2.1, 00:20:34
     2.0.0.0/32 is subnetted, 1 subnets
C       2.2.2.2 is directly connected, Loopback0
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [20/0] via 15.15.2.1, 00:20:34
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [200/0] via 11.1.1.6, 00:17:33
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [20/0] via 15.15.2.1, 00:20:34
B       20.0.0.0 [20/0] via 15.15.2.1, 00:20:34
B       20.0.1.0 [20/0] via 15.15.2.1, 00:20:34
B       20.0.0.12 [20/0] via 15.15.2.1, 00:20:34
B       20.0.1.12 [20/0] via 15.15.2.1, 00:20:34
B       20.0.0.8 [20/0] via 15.15.2.1, 00:20:34
B       20.0.1.8 [20/0] via 15.15.2.1, 00:20:34
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [20/0] via 15.15.2.1, 00:20:34
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [20/0] via 15.15.2.1, 00:20:34
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [20/0] via 15.15.2.1, 00:20:34
B       8.8.4.4 [20/0] via 15.15.2.1, 00:20:34
     40.0.0.0/30 is subnetted, 1 subnets
O       40.0.0.0 [250/1001] via 192.168.2.3, 00:17:20, FastEthernet1/0
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [20/0] via 15.15.2.1, 00:20:34
B       10.0.0.2/31 [20/0] via 15.15.2.1, 00:20:34
B       10.0.0.0/31 [20/0] via 15.15.2.1, 00:20:34
B       10.0.1.0/30 [20/0] via 15.15.2.1, 00:20:34
B       10.0.0.6/31 [20/0] via 15.15.2.1, 00:20:34
B       10.0.0.4/31 [20/0] via 15.15.2.1, 00:20:34
B       10.0.1.4/30 [20/0] via 15.15.2.1, 00:20:34
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [20/0] via 15.15.2.1, 00:20:34
C       11.1.1.4 is directly connected, FastEthernet0/1
B    192.168.1.0/24 [20/0] via 15.15.2.1, 00:20:34
C    192.168.2.0/24 is directly connected, FastEthernet1/0
     15.0.0.0/24 is subnetted, 2 subnets
S       15.15.1.0 [1/0] via 15.15.2.1, FastEthernet0/0
C       15.15.2.0 is directly connected, FastEthernet0/0
S*   0.0.0.0/0 is directly connected, FastEthernet0/1

CustomerA3# ping 8.8.8.8 repeat 5

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 36/49/60 ms

CustomerA3# traceroute 8.8.8.8

Type escape sequence to abort.
Tracing the route to 8.8.8.8

  1 20.0.0.9 20 msec 24 msec 36 msec
  2 20.0.1.10 [AS 64900] 36 msec 52 msec 56 msec

CustomerA3# show ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is not set

     1.0.0.0/32 is subnetted, 1 subnets
B       1.1.1.1 [200/0] via 11.1.1.1, 02:47:27
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [200/0] via 11.1.1.1, 00:20:37
     3.0.0.0/32 is subnetted, 1 subnets
C       3.3.3.3 is directly connected, Loopback0
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [200/0] via 11.1.1.1, 00:17:34
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [20/0] via 20.0.0.9, 02:47:27
B       20.0.0.0 [20/0] via 20.0.0.9, 02:47:27
B       20.0.1.0 [20/0] via 20.0.0.9, 02:47:01
B       20.0.0.12 [20/0] via 20.0.0.9, 02:47:27
B       20.0.1.12 [20/0] via 20.0.0.9, 02:47:27
C       20.0.0.8 is directly connected, FastEthernet0/1
B       20.0.1.8 [20/0] via 20.0.0.9, 02:47:27
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [20/0] via 20.0.0.9, 02:47:01
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [20/0] via 20.0.0.9, 02:47:01
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [20/0] via 20.0.0.9, 02:47:27
B       8.8.4.4 [20/0] via 20.0.0.9, 02:47:27
     40.0.0.0/30 is subnetted, 1 subnets
C       40.0.0.0 is directly connected, Tunnel0
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [20/0] via 20.0.0.9, 02:47:01
B       10.0.0.2/31 [20/0] via 20.0.0.9, 02:47:27
B       10.0.0.0/31 [20/0] via 20.0.0.9, 02:47:01
B       10.0.1.0/30 [20/0] via 20.0.0.9, 02:47:27
B       10.0.0.6/31 [20/0] via 20.0.0.9, 02:47:01
B       10.0.0.4/31 [20/0] via 20.0.0.9, 02:47:27
B       10.0.1.4/30 [20/0] via 20.0.0.9, 02:47:27
     11.0.0.0/30 is subnetted, 2 subnets
C       11.1.1.0 is directly connected, FastEthernet0/0
B       11.1.1.4 [200/0] via 11.1.1.1, 00:20:31
C    192.168.1.0/24 is directly connected, FastEthernet1/0
S    192.168.2.0/24 [250/0] via 40.0.0.2, Tunnel0
     15.0.0.0/24 is subnetted, 2 subnets
B       15.15.1.0 [200/0] via 11.1.1.1, 02:47:27
B       15.15.2.0 [200/0] via 11.1.1.1, 00:20:31

CustomerA4# ping 8.8.8.8 repeat 5

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 168/220/344 ms

CustomerA4# traceroute 8.8.8.8

Type escape sequence to abort.
Tracing the route to 8.8.8.8

  1 11.1.1.5 216 msec 44 msec 52 msec
  2 15.15.2.1 88 msec 56 msec 72 msec
  3 10.0.0.4 [AS 65000] [MPLS: Labels 21/0/29 Exp 0] 164 msec 184 msec 196 msec
  4 10.0.0.2 [AS 65000] [MPLS: Labels 21/0/29 Exp 0] 148 msec 176 msec 164 msec
  5 15.15.1.1 [AS 65000] [MPLS: Label 29 Exp 0] 148 msec 164 msec 140 msec
  6 15.15.1.2 [AS 65000] 180 msec 232 msec 148 msec
  7 11.1.1.2 [AS 65000] 240 msec 176 msec 228 msec
  8 20.0.0.9 [AS 64800] 148 msec 148 msec 164 msec
  9 20.0.1.10 [AS 64900] 176 msec 196 msec 196 msec

CustomerA4# show ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is not set

     1.0.0.0/32 is subnetted, 1 subnets
B       1.1.1.1 [200/0] via 11.1.1.5, 00:17:48
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [200/0] via 11.1.1.5, 00:17:48
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [200/0] via 11.1.1.5, 00:17:48
     4.0.0.0/32 is subnetted, 1 subnets
C       4.4.4.4 is directly connected, Loopback0
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [200/0] via 11.1.1.5, 00:17:48
B       20.0.0.0 [200/0] via 11.1.1.5, 00:17:48
B       20.0.1.0 [200/0] via 11.1.1.5, 00:17:48
C       20.0.0.12 is directly connected, FastEthernet0/1
B       20.0.1.12 [200/0] via 11.1.1.5, 00:17:48
B       20.0.0.8 [200/0] via 11.1.1.5, 00:17:48
B       20.0.1.8 [200/0] via 11.1.1.5, 00:17:48
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [200/0] via 11.1.1.5, 00:17:48
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [200/0] via 11.1.1.5, 00:17:48
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [200/0] via 11.1.1.5, 00:17:48
B       8.8.4.4 [200/0] via 11.1.1.5, 00:17:48
     40.0.0.0/30 is subnetted, 1 subnets
C       40.0.0.0 is directly connected, Tunnel0
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [200/0] via 11.1.1.5, 00:17:48
B       10.0.0.2/31 [200/0] via 11.1.1.5, 00:17:48
B       10.0.0.0/31 [200/0] via 11.1.1.5, 00:17:48
B       10.0.1.0/30 [200/0] via 11.1.1.5, 00:17:48
B       10.0.0.6/31 [200/0] via 11.1.1.5, 00:17:48
B       10.0.0.4/31 [200/0] via 11.1.1.5, 00:17:48
B       10.0.1.4/30 [200/0] via 11.1.1.5, 00:17:49
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [200/0] via 11.1.1.5, 00:17:49
C       11.1.1.4 is directly connected, FastEthernet0/0
B    192.168.1.0/24 [200/0] via 11.1.1.5, 00:17:49
C    192.168.2.0/24 is directly connected, FastEthernet1/0
     15.0.0.0/24 is subnetted, 2 subnets
B       15.15.1.0 [200/0] via 11.1.1.5, 00:17:49
B       15.15.2.0 [200/0] via 11.1.1.5, 00:17:49

