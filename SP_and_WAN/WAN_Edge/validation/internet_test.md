CustomerA3
```
CustomerA3#ping 8.8.8.8

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 48/58/64 ms
CustomerA3#
```

CustomerA4
```
CustomerA4#ping 8.8.8.8

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 36/85/112 ms
CustomerA4#
```


CustomerA2
```
CustomerA2#ping 8.8.8.8

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
.!!!.
Success rate is 60 percent (3/5), round-trip min/avg/max = 96/117/140 ms
CustomerA2#
```

```
CustomerA1#ping 8.8.8.8

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 52/95/124 ms
CustomerA1#
```

UBUNTU SERVER
```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=2 ttl=253 time=78.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=253 time=83.6 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=253 time=93.0 ms                                                                                         ^C 
 --- 8.8.8.8 ping statistics ---      
4 packets transmitted, 3 received, 25% packet loss, time 3050ms 
rtt min/avg/max/mdev = 78.630/85.095/93.043/5.976 ms 
```

NOTES
```
-All routers and the Ubuntu host can reach the Internet (8.8.8.8).

-CustomerA3 and CustomerA4 reach it via direct BGP routes (see BGP filter validation).

-CustomerA1, CustomerA2, and Ubuntu host reach the Internet through NAT.

-Some packet loss is observed on NAT-ted nodes due to emulation limitations.
```
