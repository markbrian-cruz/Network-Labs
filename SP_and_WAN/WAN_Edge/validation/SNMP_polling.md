
CustomerA1
```
$ snmpwalk -v2c -c <Redacted Community Strings> 192.168.1.2 SNMPv2-MIB::sysName
SNMPv2-MIB::sysName.0 = STRING: CustomerA1.lab.local
$ snmpwalk -v2c -c CustomerA_ReadOnly 192.168.1.2 SNMPv2-MIB::sysUpTime
SNMPv2-MIB::sysUpTime.0 = Timeticks: (2304776) 6:24:07.76
```

CustomerA3
```
$ snmpwalk -v2c -c <Redacted Community Strings> 192.168.1.3 SNMPv2-MIB::sysName
SNMPv2-MIB::sysName.0 = STRING: CustomerA3.lab.local
$ snmpwalk -v2c -c CustomerA_ReadOnly 192.168.1.3 SNMPv2-MIB::sysUpTime
SNMPv2-MIB::sysUpTime.0 = Timeticks: (2306410) 6:24:24.10
```

CustomerA2
```
$ snmpwalk -v2c -c <Redacted Community Strings> 192.168.2.2 SNMPv2-MIB::sysName
SNMPv2-MIB::sysName.0 = STRING: CustomerA2.lab.local
$ snmpwalk -v2c -c CustomerA_ReadOnly 192.168.2.2 SNMPv2-MIB::sysUpTime
SNMPv2-MIB::sysUpTime.0 = Timeticks: (2307714) 6:24:37.14
```

CustomerA4
```
$ snmpwalk -v2c -c <Redacted Community Strings> 192.168.2.3 SNMPv2-MIB::sysName
SNMPv2-MIB::sysName.0 = STRING: CustomerA4.lab.local
$ snmpwalk -v2c -c CustomerA_ReadOnly 192.168.2.3 SNMPv2-MIB::sysUpTime
SNMPv2-MIB::sysUpTime.0 = Timeticks: (2309509) 6:24:55.09
```
NOTE:
```
All CustomerA routers respond to ubuntu server snmp polling
```

