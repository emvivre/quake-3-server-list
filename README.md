# quake-3-server-list

Simple code to fetch server list from a master server. You can specify the master server to connect by setting the MASTER variable in the python script.

To list servers from a master server :
``$ q3_list.py``

To get status from a game server : 
```
$ q3_list.py <SERVER>:<PORT>
$ ./q3_list.py 198.167.223.31:27960
  sv_privateClients : 0
  sv_minPing : 0
  g_needpass : 0
  gamename : baseq3
  sv_floodProtect : 1
  capturelimit : 8
  timelimit : 0
  com_protocol : 71
  g_gametype : 0
  g_maxGameClients : 0
  dmflags : 0
  version : ioq3 1.36+u20140802+gca9eebb-2+b1/Debian linux-x86_64 Oct 14 2014
  bot_minplayers : 0
  sv_dlRate : 100
  sv_hostname : noname
  mapname : q3dm6
  com_gamename : Quake3Arena
  sv_maxclients : 8
  sv_maxRate : 0
  sv_maxPing : 0
  sv_allowDownload : 0
  fraglimit : 20
  sv_minRate : 0
```
