# hacking shortcuts
- verify HTTP / SYN
```
netstat -an | grep :80 | sort
```
- verify all TCP / UDP connections

```
netstat -ntu | grep ESTAB | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr
```

- Bans IP's

```
iptables -I INPUT -s <ipaddress> -j DROP     //ban
iptables -D INPUT -s <ipaddress> -j DROP     //unban
```

old

```
iptables -A INPUT 1 -s <ipaddress> -j DROP/REJECT
```

- KILL && Restart connection

```
killall -KILL httpd

service httpd start     // for Red Hat systems
/etc/init/d/apache2 restrat // for Debian systems
```
