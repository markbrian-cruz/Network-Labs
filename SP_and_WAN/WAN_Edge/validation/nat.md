CustomerA4
```
CustomerA4#sh ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
icmp 20.0.0.14:11      11.1.1.5:11        8.8.8.8:11         8.8.8.8:11
CustomerA4#sh ip nat statistics
Total active translations: 1 (0 static, 1 dynamic; 1 extended)
Outside interfaces:
  FastEthernet0/1
Inside interfaces:
  FastEthernet0/0, FastEthernet1/0
Hits: 648  Misses: 0
CEF Translated packets: 616, CEF Punted packets: 64
Expired translations: 285
Dynamic mappings:
-- Inside Source
[Id: 1] access-list 1 interface FastEthernet0/1 refcount 0
[Id: 2] access-list 10 interface FastEthernet0/1 refcount 1
[Id: 3] route-map NAT interface FastEthernet0/1 refcount 0
Appl doors: 0
Normal doors: 0
Queued Packets: 0
CustomerA4#
```

CustomerA3
```
CustomerA3#sh ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
icmp 20.0.0.10:3       11.1.1.1:3         8.8.8.8:3          8.8.8.8:3
CustomerA3#sh ip nat statistics
Total active translations: 1 (0 static, 1 dynamic; 1 extended)
Outside interfaces:
  FastEthernet0/1
Inside interfaces:
  FastEthernet0/0, FastEthernet1/0
Hits: 280  Misses: 0
CEF Translated packets: 280, CEF Punted packets: 0
Expired translations: 88
Dynamic mappings:
-- Inside Source
[Id: 1] access-list 1 interface FastEthernet0/1 refcount 0
[Id: 2] route-map NAT interface FastEthernet0/1 refcount 1
Appl doors: 0
Normal doors: 0
Queued Packets: 0
CustomerA3#
```

NOTES
```
-NAT translations are working as expected on CustomerA3 and CustomerA4.

-Active dynamic translations are being created for ICMP traffic to 8.8.8.8.

-Translation statistics show hits, expirations, and interface mappings consistent with normal NAT behavior.
```
