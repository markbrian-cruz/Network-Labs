# QoS_Interface_Summary Validation Report
Generated: 2026-03-02 13:15:17.049020

SP1-PE1#show class-map (iteration 1)
```
 Class Map match-any class-default (id 0)
   Match any 

 Class Map match-all VOICE (id 1)
   Match ip  dscp ef (46)

```

SP1-PE1#show clock
```
13:16:10.963 UTC Mon Mar 2 2026
```

SP1-PE1#show class-map (iteration 2)
```
 Class Map match-any class-default (id 0)
   Match any 

 Class Map match-all VOICE (id 1)
   Match ip  dscp ef (46)

```

SP1-PE1#show clock
```
13:16:19.255 UTC Mon Mar 2 2026
```

SP1-PE5#show class-map (iteration 1)
```
 Class Map match-any class-default (id 0)
   Match any 

 Class Map match-all VOICE (id 1)
   Match ip  dscp ef (46)

```

SP1-PE5#show clock
```
13:17:44.587 UTC Mon Mar 2 2026
```

SP1-PE5#show class-map (iteration 2)
```
 Class Map match-any class-default (id 0)
   Match any 

 Class Map match-all VOICE (id 1)
   Match ip  dscp ef (46)

```

SP1-PE5#show clock
```
13:17:52.915 UTC Mon Mar 2 2026
```

