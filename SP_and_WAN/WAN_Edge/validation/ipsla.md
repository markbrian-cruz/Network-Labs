CustomerA1# show ip sla summary
                        ^
% Invalid input detected at '^' marker.


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
B       2.2.2.2 [20/0] via 15.15.1.1, 00:20:08
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [200/0] via 11.1.1.2, 02:46:58
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [20/0] via 15.15.1.1, 00:17:06
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [200/0] via 11.1.1.2, 02:46:58
B       20.0.0.0 [200/0] via 11.1.1.2, 02:46:58
B       20.0.1.0 [200/0] via 11.1.1.2, 02:46:32
B       20.0.0.12 [200/0] via 11.1.1.2, 02:46:58
B       20.0.1.12 [200/0] via 11.1.1.2, 02:46:58
B       20.0.0.8 [200/0] via 11.1.1.2, 02:46:58
B       20.0.1.8 [200/0] via 11.1.1.2, 02:46:58
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [200/0] via 11.1.1.2, 02:46:32
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [200/0] via 11.1.1.2, 02:46:32
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [200/0] via 11.1.1.2, 02:46:58
B       8.8.4.4 [200/0] via 11.1.1.2, 02:46:58
     40.0.0.0/30 is subnetted, 1 subnets
O       40.0.0.0 [250/1001] via 192.168.1.3, 02:46:42, FastEthernet1/0
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [200/0] via 11.1.1.2, 02:46:32
B       10.0.0.2/31 [200/0] via 11.1.1.2, 02:46:58
B       10.0.0.0/31 [200/0] via 11.1.1.2, 02:46:32
B       10.0.1.0/30 [200/0] via 11.1.1.2, 02:46:58
B       10.0.0.6/31 [200/0] via 11.1.1.2, 02:46:32
B       10.0.0.4/31 [200/0] via 11.1.1.2, 02:46:58
B       10.0.1.4/30 [200/0] via 11.1.1.2, 02:46:58
     11.0.0.0/30 is subnetted, 2 subnets
C       11.1.1.0 is directly connected, FastEthernet0/1
B       11.1.1.4 [20/0] via 15.15.1.1, 00:20:03
C    192.168.1.0/24 is directly connected, FastEthernet1/0
O    192.168.2.0/24 [250/1002] via 192.168.1.3, 00:16:35, FastEthernet1/0
     15.0.0.0/24 is subnetted, 2 subnets
C       15.15.1.0 is directly connected, FastEthernet0/0
S       15.15.2.0 [1/0] via 15.15.1.1, FastEthernet0/0
S*   0.0.0.0/0 is directly connected, FastEthernet0/1

CustomerA2# show ip sla summary
                        ^
% Invalid input detected at '^' marker.


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
B       1.1.1.1 [20/0] via 15.15.2.1, 00:20:13
     2.0.0.0/32 is subnetted, 1 subnets
C       2.2.2.2 is directly connected, Loopback0
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [20/0] via 15.15.2.1, 00:20:13
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [200/0] via 11.1.1.6, 00:17:13
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [20/0] via 15.15.2.1, 00:20:13
B       20.0.0.0 [20/0] via 15.15.2.1, 00:20:13
B       20.0.1.0 [20/0] via 15.15.2.1, 00:20:13
B       20.0.0.12 [20/0] via 15.15.2.1, 00:20:13
B       20.0.1.12 [20/0] via 15.15.2.1, 00:20:13
B       20.0.0.8 [20/0] via 15.15.2.1, 00:20:13
B       20.0.1.8 [20/0] via 15.15.2.1, 00:20:13
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [20/0] via 15.15.2.1, 00:20:13
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [20/0] via 15.15.2.1, 00:20:13
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [20/0] via 15.15.2.1, 00:20:13
B       8.8.4.4 [20/0] via 15.15.2.1, 00:20:13
     40.0.0.0/30 is subnetted, 1 subnets
O       40.0.0.0 [250/1001] via 192.168.2.3, 00:16:59, FastEthernet1/0
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [20/0] via 15.15.2.1, 00:20:13
B       10.0.0.2/31 [20/0] via 15.15.2.1, 00:20:13
B       10.0.0.0/31 [20/0] via 15.15.2.1, 00:20:13
B       10.0.1.0/30 [20/0] via 15.15.2.1, 00:20:13
B       10.0.0.6/31 [20/0] via 15.15.2.1, 00:20:13
B       10.0.0.4/31 [20/0] via 15.15.2.1, 00:20:13
B       10.0.1.4/30 [20/0] via 15.15.2.1, 00:20:13
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [20/0] via 15.15.2.1, 00:20:13
C       11.1.1.4 is directly connected, FastEthernet0/1
B    192.168.1.0/24 [20/0] via 15.15.2.1, 00:20:13
C    192.168.2.0/24 is directly connected, FastEthernet1/0
     15.0.0.0/24 is subnetted, 2 subnets
S       15.15.1.0 [1/0] via 15.15.2.1, FastEthernet0/0
C       15.15.2.0 is directly connected, FastEthernet0/0
S*   0.0.0.0/0 is directly connected, FastEthernet0/1

CustomerA3# show ip sla summary
                        ^
% Invalid input detected at '^' marker.


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
B       1.1.1.1 [200/0] via 11.1.1.1, 02:47:05
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [200/0] via 11.1.1.1, 00:20:15
     3.0.0.0/32 is subnetted, 1 subnets
C       3.3.3.3 is directly connected, Loopback0
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [200/0] via 11.1.1.1, 00:17:13
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [20/0] via 20.0.0.9, 02:47:05
B       20.0.0.0 [20/0] via 20.0.0.9, 02:47:05
B       20.0.1.0 [20/0] via 20.0.0.9, 02:46:39
B       20.0.0.12 [20/0] via 20.0.0.9, 02:47:05
B       20.0.1.12 [20/0] via 20.0.0.9, 02:47:05
C       20.0.0.8 is directly connected, FastEthernet0/1
B       20.0.1.8 [20/0] via 20.0.0.9, 02:47:05
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [20/0] via 20.0.0.9, 02:46:39
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [20/0] via 20.0.0.9, 02:46:39
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [20/0] via 20.0.0.9, 02:47:05
B       8.8.4.4 [20/0] via 20.0.0.9, 02:47:05
     40.0.0.0/30 is subnetted, 1 subnets
C       40.0.0.0 is directly connected, Tunnel0
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [20/0] via 20.0.0.9, 02:46:39
B       10.0.0.2/31 [20/0] via 20.0.0.9, 02:47:05
B       10.0.0.0/31 [20/0] via 20.0.0.9, 02:46:39
B       10.0.1.0/30 [20/0] via 20.0.0.9, 02:47:05
B       10.0.0.6/31 [20/0] via 20.0.0.9, 02:46:39
B       10.0.0.4/31 [20/0] via 20.0.0.9, 02:47:05
B       10.0.1.4/30 [20/0] via 20.0.0.9, 02:47:05
     11.0.0.0/30 is subnetted, 2 subnets
C       11.1.1.0 is directly connected, FastEthernet0/0
B       11.1.1.4 [200/0] via 11.1.1.1, 00:20:10
C    192.168.1.0/24 is directly connected, FastEthernet1/0
S    192.168.2.0/24 [250/0] via 40.0.0.2, Tunnel0
     15.0.0.0/24 is subnetted, 2 subnets
B       15.15.1.0 [200/0] via 11.1.1.1, 02:47:05
B       15.15.2.0 [200/0] via 11.1.1.1, 00:20:10

CustomerA4# show ip sla summary
                        ^
% Invalid input detected at '^' marker.


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
B       1.1.1.1 [200/0] via 11.1.1.5, 00:17:20
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [200/0] via 11.1.1.5, 00:17:20
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [200/0] via 11.1.1.5, 00:17:20
     4.0.0.0/32 is subnetted, 1 subnets
C       4.4.4.4 is directly connected, Loopback0
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [200/0] via 11.1.1.5, 00:17:20
B       20.0.0.0 [200/0] via 11.1.1.5, 00:17:20
B       20.0.1.0 [200/0] via 11.1.1.5, 00:17:20
C       20.0.0.12 is directly connected, FastEthernet0/1
B       20.0.1.12 [200/0] via 11.1.1.5, 00:17:20
B       20.0.0.8 [200/0] via 11.1.1.5, 00:17:20
B       20.0.1.8 [200/0] via 11.1.1.5, 00:17:20
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [200/0] via 11.1.1.5, 00:17:20
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [200/0] via 11.1.1.5, 00:17:20
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [200/0] via 11.1.1.5, 00:17:20
B       8.8.4.4 [200/0] via 11.1.1.5, 00:17:20
     40.0.0.0/30 is subnetted, 1 subnets
C       40.0.0.0 is directly connected, Tunnel0
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [200/0] via 11.1.1.5, 00:17:20
B       10.0.0.2/31 [200/0] via 11.1.1.5, 00:17:20
B       10.0.0.0/31 [200/0] via 11.1.1.5, 00:17:20
B       10.0.1.0/30 [200/0] via 11.1.1.5, 00:17:20
B       10.0.0.6/31 [200/0] via 11.1.1.5, 00:17:20
B       10.0.0.4/31 [200/0] via 11.1.1.5, 00:17:20
B       10.0.1.4/30 [200/0] via 11.1.1.5, 00:17:20
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [200/0] via 11.1.1.5, 00:17:20
C       11.1.1.4 is directly connected, FastEthernet0/0
B    192.168.1.0/24 [200/0] via 11.1.1.5, 00:17:20
C    192.168.2.0/24 is directly connected, FastEthernet1/0
     15.0.0.0/24 is subnetted, 2 subnets
B       15.15.1.0 [200/0] via 11.1.1.5, 00:17:20
B       15.15.2.0 [200/0] via 11.1.1.5, 00:17:20

