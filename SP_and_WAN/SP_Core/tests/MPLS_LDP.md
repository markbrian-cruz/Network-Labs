# MPLS_LDP Validation Report
Generated: 2026-03-02 13:15:17.048697

SP1-PE1#show mpls ldp neighbor
```
    Peer LDP Ident: 4.4.4.4:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 4.4.4.4.45635 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 379/380; Downstream
	Up time: 05:17:05
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.7
        Addresses bound to peer LDP Ident:
          4.4.4.4         10.0.0.7        10.0.0.8        172.16.100.1    
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 2.2.2.2.39246 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 379/378; Downstream
	Up time: 05:17:04
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.1
        Addresses bound to peer LDP Ident:
          2.2.2.2         10.0.0.1        10.0.0.2        20.0.1.2        
          10.0.1.2        
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 5.5.5.5.52395 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 377/378; Downstream
	Up time: 05:16:32
	LDP discovery sources:
	  Targeted Hello 1.1.1.1 -> 5.5.5.5, active, passive
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
```

SP1-BR2#show mpls ldp neighbor
```
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 2.2.2.2:0
	TCP connection: 1.1.1.1.646 - 2.2.2.2.39246
	State: Oper; Msgs sent/rcvd: 379/380; Downstream
	Up time: 05:18:12
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.0
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 2.2.2.2:0
	TCP connection: 3.3.3.3.61499 - 2.2.2.2.646
	State: Oper; Msgs sent/rcvd: 381/383; Downstream
	Up time: 05:17:48
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.3
        Addresses bound to peer LDP Ident:
          3.3.3.3         10.0.0.3        10.0.0.4        20.0.1.6        
          10.0.1.6        
```

SP1-BR3#show mpls ldp neighbor
```
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 2.2.2.2.646 - 3.3.3.3.61499
	State: Oper; Msgs sent/rcvd: 383/381; Downstream
	Up time: 05:17:58
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.2
        Addresses bound to peer LDP Ident:
          2.2.2.2         10.0.0.1        10.0.0.2        20.0.1.2        
          10.0.1.2        
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 5.5.5.5.59105 - 3.3.3.3.646
	State: Oper; Msgs sent/rcvd: 379/380; Downstream
	Up time: 05:17:45
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.5
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
```

SP1-RR4#show mpls ldp neighbor
```
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 4.4.4.4:0
	TCP connection: 1.1.1.1.646 - 4.4.4.4.45635
	State: Oper; Msgs sent/rcvd: 381/381; Downstream
	Up time: 05:18:30
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.6
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 4.4.4.4:0
	TCP connection: 5.5.5.5.41535 - 4.4.4.4.646
	State: Oper; Msgs sent/rcvd: 379/380; Downstream
	Up time: 05:17:59
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.9
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
```

SP1-PE5#show mpls ldp neighbor
```
    Peer LDP Ident: 4.4.4.4:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 4.4.4.4.646 - 5.5.5.5.41535
	State: Oper; Msgs sent/rcvd: 380/379; Downstream
	Up time: 05:18:07
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.8
        Addresses bound to peer LDP Ident:
          4.4.4.4         10.0.0.7        10.0.0.8        172.16.100.1    
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 1.1.1.1.646 - 5.5.5.5.52395
	State: Oper; Msgs sent/rcvd: 380/379; Downstream
	Up time: 05:18:05
	LDP discovery sources:
	  Targeted Hello 5.5.5.5 -> 1.1.1.1, active, passive
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 3.3.3.3.646 - 5.5.5.5.59105
	State: Oper; Msgs sent/rcvd: 380/379; Downstream
	Up time: 05:18:00
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.4
        Addresses bound to peer LDP Ident:
          3.3.3.3         10.0.0.3        10.0.0.4        20.0.1.6        
          10.0.1.6        
```

