# MPLS_LDP Validation Report
Generated: 2026-03-02 01:03:04.193806

## SP1-PE1
Router: SP1-PE1
Command: show mpls ldp neighbor
```
    Peer LDP Ident: 4.4.4.4:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 4.4.4.4.41835 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 112/110; Downstream
	Up time: 01:22:37
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.7
        Addresses bound to peer LDP Ident:
          4.4.4.4         10.0.0.7        10.0.0.8        172.16.100.1    
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 2.2.2.2.42922 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 110/109; Downstream
	Up time: 01:22:36
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.1
        Addresses bound to peer LDP Ident:
          2.2.2.2         10.0.0.1        10.0.0.2        20.0.1.2        
          10.0.1.2        
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 5.5.5.5.28288 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 111/110; Downstream
	Up time: 01:22:35
	LDP discovery sources:
	  Targeted Hello 1.1.1.1 -> 5.5.5.5, active, passive
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
```

## SP1-BR2
Router: SP1-BR2
Command: show mpls ldp neighbor
```
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 2.2.2.2:0
	TCP connection: 3.3.3.3.18138 - 2.2.2.2.646
	State: Oper; Msgs sent/rcvd: 112/112; Downstream
	Up time: 01:23:14
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.3
        Addresses bound to peer LDP Ident:
          3.3.3.3         10.0.0.3        10.0.0.4        20.0.1.6        
          10.0.1.6        
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 2.2.2.2:0
	TCP connection: 1.1.1.1.646 - 2.2.2.2.42922
	State: Oper; Msgs sent/rcvd: 110/111; Downstream
	Up time: 01:23:14
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.0
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
```

## SP1-BR3
Router: SP1-BR3
Command: show mpls ldp neighbor
```
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 2.2.2.2.646 - 3.3.3.3.18138
	State: Oper; Msgs sent/rcvd: 112/112; Downstream
	Up time: 01:23:23
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.2
        Addresses bound to peer LDP Ident:
          2.2.2.2         10.0.0.1        10.0.0.2        20.0.1.2        
          10.0.1.2        
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 5.5.5.5.22707 - 3.3.3.3.646
	State: Oper; Msgs sent/rcvd: 111/111; Downstream
	Up time: 01:23:21
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.5
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
```

## SP1-RR4
Router: SP1-RR4
Command: show mpls ldp neighbor
```
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 4.4.4.4:0
	TCP connection: 5.5.5.5.55461 - 4.4.4.4.646
	State: Oper; Msgs sent/rcvd: 111/111; Downstream
	Up time: 01:23:30
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.9
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 4.4.4.4:0
	TCP connection: 1.1.1.1.646 - 4.4.4.4.41835
	State: Oper; Msgs sent/rcvd: 111/113; Downstream
	Up time: 01:23:29
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.6
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
```

## SP1-PE5
Router: SP1-PE5
Command: show mpls ldp neighbor
```
    Peer LDP Ident: 4.4.4.4:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 4.4.4.4.646 - 5.5.5.5.55461
	State: Oper; Msgs sent/rcvd: 112/111; Downstream
	Up time: 01:23:38
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.8
        Addresses bound to peer LDP Ident:
          4.4.4.4         10.0.0.7        10.0.0.8        172.16.100.1    
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 3.3.3.3.646 - 5.5.5.5.22707
	State: Oper; Msgs sent/rcvd: 111/111; Downstream
	Up time: 01:23:36
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.4
        Addresses bound to peer LDP Ident:
          3.3.3.3         10.0.0.3        10.0.0.4        20.0.1.6        
          10.0.1.6        
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 1.1.1.1.646 - 5.5.5.5.28288
	State: Oper; Msgs sent/rcvd: 111/112; Downstream
	Up time: 01:23:35
	LDP discovery sources:
	  Targeted Hello 5.5.5.5 -> 1.1.1.1, active, passive
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
```

