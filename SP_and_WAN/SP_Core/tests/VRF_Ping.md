# VRF_Ping Validation Report
Generated: 2026-03-02 13:15:17.049059

SP1-PE1 - CUST_A#ping vrf CUST_A 15.15.2.1
```

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.2.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 80/212/344 ms
```

SP1-PE1 - CUST_B#ping vrf CUST_B 15.15.2.1
```

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.2.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 56/210/364 ms
```

SP1-PE5 - CUST_A#ping vrf CUST_A 15.15.1.1
```

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.1.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 72/74/76 ms
```

SP1-PE5 - CUST_B#ping vrf CUST_B 15.15.1.1
```

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.1.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 48/50/52 ms
```

