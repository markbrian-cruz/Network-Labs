# VRF_Route_Table Validation Report
Generated: 2026-03-02 13:15:17.049178

SP1-PE1 - CUST_A#show ip route vrf CUST_A
```

Routing Table: CUST_A
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is 10.0.0.1 to network 0.0.0.0

     1.0.0.0/32 is subnetted, 1 subnets
B       1.1.1.1 [20/0] via 15.15.1.2, 05:15:49
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [200/0] via 5.5.5.5, 05:15:26
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [20/0] via 15.15.1.2, 05:15:49
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [200/0] via 5.5.5.5, 05:15:26
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [20/0] via 15.15.1.2, 05:15:19
B       20.0.0.0 [20/0] via 15.15.1.2, 05:15:49
B       20.0.1.0 [20/0] via 15.15.1.2, 05:15:19
B       20.0.0.12 [200/0] via 5.5.5.5, 05:15:26
B       20.0.1.12 [20/0] via 15.15.1.2, 05:15:49
B       20.0.0.8 [20/0] via 15.15.1.2, 05:15:49
B       20.0.1.8 [20/0] via 15.15.1.2, 05:15:49
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [20/0] via 15.15.1.2, 05:15:19
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [20/0] via 15.15.1.2, 05:15:19
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [20/0] via 15.15.1.2, 05:15:49
B       8.8.4.4 [20/0] via 15.15.1.2, 05:15:49
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [20/0] via 15.15.1.2, 05:15:19
B       10.0.0.2/31 [20/0] via 15.15.1.2, 05:15:19
B       10.0.0.0/31 [20/0] via 15.15.1.2, 05:15:19
B       10.0.1.0/30 [20/0] via 15.15.1.2, 05:15:49
B       10.0.0.6/31 [20/0] via 15.15.1.2, 05:15:19
B       10.0.0.4/31 [20/0] via 15.15.1.2, 05:15:19
B       10.0.1.4/30 [20/0] via 15.15.1.2, 05:15:49
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [20/0] via 15.15.1.2, 05:15:49
B       11.1.1.4 [200/0] via 5.5.5.5, 05:15:26
B    192.168.1.0/24 [20/0] via 15.15.1.2, 05:15:49
B    192.168.2.0/24 [200/0] via 5.5.5.5, 05:15:26
     15.0.0.0/24 is subnetted, 2 subnets
C       15.15.1.0 is directly connected, FastEthernet1/0
B       15.15.2.0 [200/0] via 5.5.5.5, 05:15:26
S*   0.0.0.0/0 [1/0] via 10.0.0.1
               is directly connected, Tunnel10
```

SP1-PE1 - CUST_B#show ip route vrf CUST_B
```

Routing Table: CUST_B
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is 10.0.0.1 to network 0.0.0.0

     15.0.0.0/24 is subnetted, 2 subnets
C       15.15.1.0 is directly connected, FastEthernet2/0
B       15.15.2.0 [200/0] via 5.5.5.5, 05:15:35
S*   0.0.0.0/0 [1/0] via 10.0.0.1
               is directly connected, Tunnel20
```

SP1-PE5 - CUST_A#show ip route vrf CUST_A
```

Routing Table: CUST_A
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is 0.0.0.0 to network 0.0.0.0

     1.0.0.0/32 is subnetted, 1 subnets
B       1.1.1.1 [200/0] via 1.1.1.1, 05:16:54
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [20/0] via 15.15.2.2, 05:17:02
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [200/0] via 1.1.1.1, 05:16:54
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [20/0] via 15.15.2.2, 05:17:02
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [200/0] via 1.1.1.1, 05:16:39
B       20.0.0.0 [20/0] via 15.15.2.2, 05:17:02
B       20.0.1.0 [200/0] via 1.1.1.1, 05:16:39
B       20.0.0.12 [20/0] via 15.15.2.2, 05:17:02
B       20.0.1.12 [20/0] via 15.15.2.2, 05:17:02
B       20.0.0.8 [20/0] via 15.15.2.2, 05:17:02
B       20.0.1.8 [20/0] via 15.15.2.2, 05:17:02
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [200/0] via 1.1.1.1, 05:16:39
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [200/0] via 1.1.1.1, 05:16:39
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [20/0] via 15.15.2.2, 05:17:02
B       8.8.4.4 [20/0] via 15.15.2.2, 05:17:02
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [200/0] via 1.1.1.1, 05:16:39
B       10.0.0.2/31 [200/0] via 1.1.1.1, 05:16:39
B       10.0.0.0/31 [200/0] via 1.1.1.1, 05:16:39
B       10.0.1.0/30 [20/0] via 15.15.2.2, 05:17:02
B       10.0.0.6/31 [200/0] via 1.1.1.1, 05:16:39
B       10.0.0.4/31 [200/0] via 1.1.1.1, 05:16:39
B       10.0.1.4/30 [20/0] via 15.15.2.2, 05:17:02
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [200/0] via 1.1.1.1, 05:16:54
B       11.1.1.4 [20/0] via 15.15.2.2, 05:17:02
B    192.168.1.0/24 [200/0] via 1.1.1.1, 05:16:54
B    192.168.2.0/24 [20/0] via 15.15.2.2, 05:17:02
     15.0.0.0/24 is subnetted, 2 subnets
B       15.15.1.0 [200/0] via 1.1.1.1, 05:16:54
C       15.15.2.0 is directly connected, FastEthernet1/0
S*   0.0.0.0/0 is directly connected, Tunnel10
               [1/0] via 10.0.0.1
```

SP1-PE5 - CUST_B#show ip route vrf CUST_B
```

Routing Table: CUST_B
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is 0.0.0.0 to network 0.0.0.0

     15.0.0.0/24 is subnetted, 2 subnets
B       15.15.1.0 [200/0] via 1.1.1.1, 05:17:03
C       15.15.2.0 is directly connected, FastEthernet2/0
S*   0.0.0.0/0 is directly connected, Tunnel20
               [1/0] via 10.0.0.1
```

