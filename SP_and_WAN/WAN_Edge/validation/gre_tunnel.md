CustomerA3
```
CustomerA3#sh int tu0
Tunnel0 is up, line protocol is up
  Hardware is Tunnel
  Internet address is 40.0.0.1/30
  MTU 1514 bytes, BW 9 Kbit/sec, DLY 500000 usec,
     reliability 255/255, txload 28/255, rxload 28/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel source 20.0.0.10, destination 20.0.0.14
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255
  Fast tunneling enabled
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Tunnel protection via IPSec (profile "IPSEC_PROF")
  Last input 00:00:03, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 10
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 1000 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 0 packets/sec
     5425 packets input, 626516 bytes, 0 no buffer
     Received 0 broadcasts, 0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     5712 packets output, 635484 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
CustomerA3#

CustomerA3#ping 20.0.0.14

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 20.0.0.14, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 48/72/104 ms
CustomerA3#

CustomerA3#ping 40.0.0.2 size 1360 df-bit

Type escape sequence to abort.
Sending 5, 1360-byte ICMP Echos to 40.0.0.2, timeout is 2 seconds:
Packet sent with the DF bit set
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 40/78/116 ms
CustomerA3#

```

CustomerA4
```
CustomerA4#sh int tu0
Tunnel0 is up, line protocol is up
  Hardware is Tunnel
  Internet address is 40.0.0.2/30
  MTU 1514 bytes, BW 9 Kbit/sec, DLY 500000 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel source 20.0.0.14, destination 20.0.0.10
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255
  Fast tunneling enabled
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Tunnel protection via IPSec (profile "IPSEC_PROF")
  Last input 00:00:07, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 8
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     5724 packets input, 667612 bytes, 0 no buffer
     Received 0 broadcasts, 0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     5710 packets output, 667740 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
CustomerA4#

CustomerA4#ping 20.0.0.10

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 20.0.0.10, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 40/87/108 ms

CustomerA4#ping 40.0.0.1 size 1360 df-bit

Type escape sequence to abort.
Sending 5, 1360-byte ICMP Echos to 40.0.0.1, timeout is 2 seconds:
Packet sent with the DF bit set
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 72/84/104 ms
CustomerA4#

```

NOTE
```
-Tunnel is up

-underlay ip is reachable

-tunnel ip is reachable even with 1360 DF
  → 1400-byte packets may experience intermittent drops due to MTU overhead
```
