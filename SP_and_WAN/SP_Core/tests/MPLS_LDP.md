# MPLS_LDP Validation Report
Generated: 2026-03-01 15:51:18.882548

## SP1-PE1 (PE)
```
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 2.2.2.2.57300 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 282/280; Downstream
	Up time: 03:53:17
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.1
        Addresses bound to peer LDP Ident:
          2.2.2.2         10.0.0.1        10.0.0.2        20.0.1.2        
          10.0.1.2        
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 5.5.5.5.43529 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 283/281; Downstream
	Up time: 03:53:05
	LDP discovery sources:
	  Targeted Hello 1.1.1.1 -> 5.5.5.5, active, passive
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
    Peer LDP Ident: 4.4.4.4:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 4.4.4.4.65020 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 175/176; Downstream
	Up time: 02:19:34
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.7
        Addresses bound to peer LDP Ident:
          4.4.4.4         10.0.0.7        10.0.0.8        172.16.100.1    
```

## SP1-BR2 (BR)
```
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 2.2.2.2:0
	TCP connection: 3.3.3.3.61505 - 2.2.2.2.646
	State: Oper; Msgs sent/rcvd: 288/284; Downstream
	Up time: 03:53:56
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.3
        Addresses bound to peer LDP Ident:
          3.3.3.3         10.0.0.3        10.0.0.4        20.0.1.6        
          10.0.1.6        
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 2.2.2.2:0
	TCP connection: 1.1.1.1.646 - 2.2.2.2.57300
	State: Oper; Msgs sent/rcvd: 281/283; Downstream
	Up time: 03:53:53
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.0
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
```

## SP1-BR3 (BR)
```
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 2.2.2.2.646 - 3.3.3.3.61505
	State: Oper; Msgs sent/rcvd: 284/288; Downstream
	Up time: 03:54:05
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.2
        Addresses bound to peer LDP Ident:
          2.2.2.2         10.0.0.1        10.0.0.2        20.0.1.2        
          10.0.1.2        
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 5.5.5.5.60461 - 3.3.3.3.646
	State: Oper; Msgs sent/rcvd: 285/282; Downstream
	Up time: 03:53:56
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.5
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
```

## SP1-RR4 (RR)
```
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 4.4.4.4:0
	TCP connection: 1.1.1.1.646 - 4.4.4.4.65020
	State: Oper; Msgs sent/rcvd: 177/176; Downstream
	Up time: 02:20:26
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.6
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
    Peer LDP Ident: 5.5.5.5:0; Local LDP Ident 4.4.4.4:0
	TCP connection: 5.5.5.5.38854 - 4.4.4.4.646
	State: Oper; Msgs sent/rcvd: 175/176; Downstream
	Up time: 02:20:26
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.9
        Addresses bound to peer LDP Ident:
          5.5.5.5         10.0.0.5        10.0.0.9        
```

## SP1-PE5 (PE)
```
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 3.3.3.3.646 - 5.5.5.5.60461
	State: Oper; Msgs sent/rcvd: 282/285; Downstream
	Up time: 03:54:11
	LDP discovery sources:
	  FastEthernet0/0, Src IP addr: 10.0.0.4
        Addresses bound to peer LDP Ident:
          3.3.3.3         10.0.0.3        10.0.0.4        20.0.1.6        
          10.0.1.6        
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 1.1.1.1.646 - 5.5.5.5.43529
	State: Oper; Msgs sent/rcvd: 282/284; Downstream
	Up time: 03:54:05
	LDP discovery sources:
	  Targeted Hello 5.5.5.5 -> 1.1.1.1, active, passive
        Addresses bound to peer LDP Ident:
          1.1.1.1         10.0.0.0        10.0.0.6        
    Peer LDP Ident: 4.4.4.4:0; Local LDP Ident 5.5.5.5:0
	TCP connection: 4.4.4.4.646 - 5.5.5.5.38854
	State: Oper; Msgs sent/rcvd: 176/176; Downstream
	Up time: 02:20:34
	LDP discovery sources:
	  FastEthernet0/1, Src IP addr: 10.0.0.8
        Addresses bound to peer LDP Ident:
          4.4.4.4         10.0.0.7        10.0.0.8        172.16.100.1    
```

