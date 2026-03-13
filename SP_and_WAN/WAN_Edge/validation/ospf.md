CustomerA3
```
CustomerA3#sh ip ospf database

            OSPF Router with ID (172.16.200.3) (Process ID 1)

                Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
172.16.200.1    172.16.200.1    460         0x80000016 0x00B4EA 2
172.16.200.2    172.16.200.2    369         0x80000016 0x00D6C1 2
172.16.200.3    172.16.200.3    301         0x80000018 0x005B6D 4
172.16.200.4    172.16.200.4    391         0x80000018 0x007B48 4

                Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
192.168.1.3     172.16.200.3    301         0x80000015 0x004DD3
192.168.2.3     172.16.200.4    391         0x80000015 0x0054C8
CustomerA3#sh ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
172.16.200.1      1   FULL/BDR        00:00:33    192.168.1.2     FastEthernet1/0
172.16.200.4      0   FULL/  -        00:00:33    40.0.0.2        Tunnel0
CustomerA3#
```

CustomerA4
```
CustomerA4#sh ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
172.16.200.2      1   FULL/BDR        00:00:37    192.168.2.2     FastEthernet1/0
172.16.200.3      0   FULL/  -        00:00:38    40.0.0.1        Tunnel0
CustomerA4#sh ip ospf database

            OSPF Router with ID (172.16.200.4) (Process ID 1)

                Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
172.16.200.1    172.16.200.1    491         0x80000016 0x00B4EA 2
172.16.200.2    172.16.200.2    398         0x80000016 0x00D6C1 2
172.16.200.3    172.16.200.3    332         0x80000018 0x005B6D 4
172.16.200.4    172.16.200.4    420         0x80000018 0x007B48 4

                Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
192.168.1.3     172.16.200.3    332         0x80000015 0x004DD3
192.168.2.3     172.16.200.4    420         0x80000015 0x0054C8
CustomerA4#
```

CustomerA2
```
CustomerA2#sh ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
172.16.200.4      1   FULL/DR         00:00:37    192.168.2.3     FastEthernet1/0
CustomerA2#sh ip ospf database

            OSPF Router with ID (172.16.200.2) (Process ID 1)

                Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
172.16.200.1    172.16.200.1    511         0x80000016 0x00B4EA 2
172.16.200.2    172.16.200.2    416         0x80000016 0x00D6C1 2
172.16.200.3    172.16.200.3    352         0x80000018 0x005B6D 4
172.16.200.4    172.16.200.4    440         0x80000018 0x007B48 4

                Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
192.168.1.3     172.16.200.3    352         0x80000015 0x004DD3
192.168.2.3     172.16.200.4    440         0x80000015 0x0054C8
CustomerA2#
```

CustomerA1
```
CustomerA1#sh ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
172.16.200.3      1   FULL/DR         00:00:39    192.168.1.3     FastEthernet1/0
CustomerA1#sh ip ospf database

            OSPF Router with ID (172.16.200.1) (Process ID 1)

                Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
172.16.200.1    172.16.200.1    526         0x80000016 0x00B4EA 2
172.16.200.2    172.16.200.2    437         0x80000016 0x00D6C1 2
172.16.200.3    172.16.200.3    369         0x80000018 0x005B6D 4
172.16.200.4    172.16.200.4    459         0x80000018 0x007B48 4

                Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
192.168.1.3     172.16.200.3    369         0x80000015 0x004DD3
192.168.2.3     172.16.200.4    459         0x80000015 0x0054C8
CustomerA1#
```

NOTES
```
- OSPF adjacency is established and FULL on all routers:

  - CustomerA1 ↔ CustomerA3 (DR/BDR)
  - CustomerA2 ↔ CustomerA4 (DR/BDR)
  - CustomerA3 ↔ CustomerA4 (over Tunnel0, point-to-point)

- All routers have synchronized OSPF databases for Area 0.

- Router and Network Link States are visible and consistent across the topology.

- No OSPF neighbor flaps or missing adjacencies observed.
```








