CustomerA1# show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
3.3.3.3           1   FULL/BDR        00:00:38    192.168.1.3     FastEthernet1/0

CustomerA1# show ip route ospf
     40.0.0.0/30 is subnetted, 1 subnets
O       40.0.0.0 [250/1001] via 192.168.1.3, 02:46:17, FastEthernet1/0
O    192.168.2.0/24 [250/1002] via 192.168.1.3, 00:16:10, FastEthernet1/0

CustomerA1# show ip route bgp
     2.0.0.0/32 is subnetted, 1 subnets
B       2.2.2.2 [20/0] via 15.15.1.1, 00:19:44
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [200/0] via 11.1.1.2, 02:46:33
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [20/0] via 15.15.1.1, 00:16:41
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [200/0] via 11.1.1.2, 02:46:33
B       20.0.0.0 [200/0] via 11.1.1.2, 02:46:33
B       20.0.1.0 [200/0] via 11.1.1.2, 02:46:07
B       20.0.0.12 [200/0] via 11.1.1.2, 02:46:33
B       20.0.1.12 [200/0] via 11.1.1.2, 02:46:33
B       20.0.0.8 [200/0] via 11.1.1.2, 02:46:33
B       20.0.1.8 [200/0] via 11.1.1.2, 02:46:33
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [200/0] via 11.1.1.2, 02:46:07
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [200/0] via 11.1.1.2, 02:46:07
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [200/0] via 11.1.1.2, 02:46:33
B       8.8.4.4 [200/0] via 11.1.1.2, 02:46:33
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [200/0] via 11.1.1.2, 02:46:07
B       10.0.0.2/31 [200/0] via 11.1.1.2, 02:46:33
B       10.0.0.0/31 [200/0] via 11.1.1.2, 02:46:07
B       10.0.1.0/30 [200/0] via 11.1.1.2, 02:46:33
B       10.0.0.6/31 [200/0] via 11.1.1.2, 02:46:07
B       10.0.0.4/31 [200/0] via 11.1.1.2, 02:46:33
B       10.0.1.4/30 [200/0] via 11.1.1.2, 02:46:33
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.4 [20/0] via 15.15.1.1, 00:19:38

CustomerA2# show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
4.4.4.4           1   FULL/BDR        00:00:35    192.168.2.3     FastEthernet1/0

CustomerA2# show ip route ospf
     40.0.0.0/30 is subnetted, 1 subnets
O       40.0.0.0 [250/1001] via 192.168.2.3, 00:16:35, FastEthernet1/0

CustomerA2# show ip route bgp
     1.0.0.0/32 is subnetted, 1 subnets
B       1.1.1.1 [20/0] via 15.15.2.1, 00:19:50
     3.0.0.0/32 is subnetted, 1 subnets
B       3.3.3.3 [20/0] via 15.15.2.1, 00:19:50
     4.0.0.0/32 is subnetted, 1 subnets
B       4.4.4.4 [200/0] via 11.1.1.6, 00:16:49
     20.0.0.0/30 is subnetted, 7 subnets
B       20.0.1.4 [20/0] via 15.15.2.1, 00:19:50
B       20.0.0.0 [20/0] via 15.15.2.1, 00:19:50
B       20.0.1.0 [20/0] via 15.15.2.1, 00:19:50
B       20.0.0.12 [20/0] via 15.15.2.1, 00:19:50
B       20.0.1.12 [20/0] via 15.15.2.1, 00:19:50
B       20.0.0.8 [20/0] via 15.15.2.1, 00:19:50
B       20.0.1.8 [20/0] via 15.15.2.1, 00:19:50
     5.0.0.0/32 is subnetted, 1 subnets
B       5.5.5.5 [20/0] via 15.15.2.1, 00:19:50
     172.16.0.0/24 is subnetted, 1 subnets
B       172.16.100.0 [20/0] via 15.15.2.1, 00:19:50
     8.0.0.0/32 is subnetted, 2 subnets
B       8.8.8.8 [20/0] via 15.15.2.1, 00:19:50
B       8.8.4.4 [20/0] via 15.15.2.1, 00:19:50
     10.0.0.0/8 is variably subnetted, 7 subnets, 2 masks
B       10.0.0.8/31 [20/0] via 15.15.2.1, 00:19:50
B       10.0.0.2/31 [20/0] via 15.15.2.1, 00:19:50
B       10.0.0.0/31 [20/0] via 15.15.2.1, 00:19:50
B       10.0.1.0/30 [20/0] via 15.15.2.1, 00:19:50
B       10.0.0.6/31 [20/0] via 15.15.2.1, 00:19:50
B       10.0.0.4/31 [20/0] via 15.15.2.1, 00:19:50
B       10.0.1.4/30 [20/0] via 15.15.2.1, 00:19:50
     11.0.0.0/30 is subnetted, 2 subnets
B       11.1.1.0 [20/0] via 15.15.2.1, 00:19:50
B    192.168.1.0/24 [20/0] via 15.15.2.1, 00:19:50

CustomerA3# show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
1.1.1.1           1   FULL/DR         00:00:31    192.168.1.2     FastEthernet1/0
4.4.4.4           0   FULL/  -        00:00:30    40.0.0.2        Tunnel0

CustomerA3# show ip route ospf


CustomerA4# show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:35    192.168.2.2     FastEthernet1/0
3.3.3.3           0   FULL/  -        00:00:38    40.0.0.1        Tunnel0

CustomerA4# show ip route ospf


