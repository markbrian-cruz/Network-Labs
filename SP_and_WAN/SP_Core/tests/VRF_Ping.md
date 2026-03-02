# VRF_Ping Validation Report
Generated: 2026-03-02 01:40:17.601528

```
SP1-PE1#ping vrf CUST_A 15.15.2.1 repeat 2

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.2.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 148/370/592 ms
```

```
SP1-PE1#ping vrf CUST_B 15.15.2.1 repeat 2

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.2.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 84/208/332 ms
```

```
SP1-PE5#ping vrf CUST_A 15.15.1.1 repeat 2

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.1.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 72/78/84 ms
```

```
SP1-PE5#ping vrf CUST_B 15.15.1.1 repeat 2

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.1.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 60/62/64 ms
```

