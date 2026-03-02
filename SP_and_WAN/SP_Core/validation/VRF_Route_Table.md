# VRF_Route_Table Validation Report
Generated: 2026-03-02 01:03:04.194022

## SP1-PE1
Router: SP1-PE1
Command: show ip route vrf CUST_A
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
B       1.1.1.1 [20/0] via 15.15.1.2, 01:21:20
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [200/0] via 5.5.5.5, 00:55:16
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [20/0] via 15.15.1.2, 01:21:20
B       11.1.1.4 [200/0] via 5.5.5.5, 00:55:16
B    192.168.2.0/24 [200/0] via 5.5.5.5, 00:55:16
     15.0.0.0/24 is subnetted, 2 subnets
C       15.15.1.0 is directly connected, FastEthernet1/0
B       15.15.2.0 [200/0] via 5.5.5.5, 00:55:16
S*   0.0.0.0/0 [1/0] via 10.0.0.1
```

## SP1-PE1
Router: SP1-PE1
Command: show ip route vrf CUST_B
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
B       15.15.2.0 [200/0] via 5.5.5.5, 00:53:19
S*   0.0.0.0/0 [1/0] via 10.0.0.1
```

## SP1-PE5
Router: SP1-PE5
Command: show ip route vrf CUST_A
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
B       1.1.1.1 [200/0] via 1.1.1.1, 00:56:16
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [20/0] via 15.15.2.2, 01:22:20
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [200/0] via 1.1.1.1, 00:56:16
B       11.1.1.4 [20/0] via 15.15.2.2, 01:22:20
B    192.168.2.0/24 [20/0] via 15.15.2.2, 01:22:20
     15.0.0.0/24 is subnetted, 2 subnets
B       15.15.1.0 [200/0] via 1.1.1.1, 00:56:16
C       15.15.2.0 is directly connected, FastEthernet1/0
S*   0.0.0.0/0 [1/0] via 10.0.0.1
```

## SP1-PE5
Router: SP1-PE5
Command: show ip route vrf CUST_B
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
B       15.15.1.0 [200/0] via 1.1.1.1, 00:56:24
C       15.15.2.0 is directly connected, FastEthernet2/0
S*   0.0.0.0/0 [1/0] via 10.0.0.1
```

