# NTP_Associations Validation Report
Generated: 2026-03-02 01:40:17.601381

```
SP1-PE1#show ntp associations

      address         ref clock     st  when  poll reach  delay  offset    disp
*~172.16.100.2     112.210.51.208    3    40   256  377    27.8   40.83     6.9
 * master (synced), # master (unsynced), + selected, - candidate, ~ configured
```

```
SP1-BR2#show ntp associations

      address         ref clock     st  when  poll reach  delay  offset    disp
*~172.16.100.2     112.210.51.208    3   158   512  377    59.7   53.46    32.0
 * master (synced), # master (unsynced), + selected, - candidate, ~ configured
```

```
SP1-BR3#show ntp associations

      address         ref clock     st  when  poll reach  delay  offset    disp
*~172.16.100.2     112.210.51.208    3     5    64  377    47.8   29.04    15.5
 * master (synced), # master (unsynced), + selected, - candidate, ~ configured
```

```
SP1-RR4#show ntp associations

      address         ref clock     st  when  poll reach  delay  offset    disp
*~172.16.100.2     112.210.51.208    3    38    64  377    15.7   42.17    22.5
 * master (synced), # master (unsynced), + selected, - candidate, ~ configured
```

```
SP1-PE5#show ntp associations

      address         ref clock     st  when  poll reach  delay  offset    disp
*~172.16.100.2     112.210.51.208    3    33   128  377    43.6   19.92     3.6
 * master (synced), # master (unsynced), + selected, - candidate, ~ configured
```

