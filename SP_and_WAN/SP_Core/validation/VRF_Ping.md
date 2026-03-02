# VRF_Ping Validation Report
Generated: 2026-03-02 01:03:04.193970

## SP1-PE1
Router: SP1-PE1
Command: ping vrf CUST_A 15.15.2.1 repeat 2
```

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.2.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 92/220/348 ms
```

## SP1-PE1
Router: SP1-PE1
Command: ping vrf CUST_B 15.15.2.1 repeat 2
```

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.2.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 64/200/336 ms
```

## SP1-PE5
Router: SP1-PE5
Command: ping vrf CUST_A 15.15.1.1 repeat 2
```

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.1.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 76/84/92 ms
```

## SP1-PE5
Router: SP1-PE5
Command: ping vrf CUST_B 15.15.1.1 repeat 2
```

Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 15.15.1.1, timeout is 2 seconds:
!!
Success rate is 100 percent (2/2), round-trip min/avg/max = 68/78/88 ms
```

