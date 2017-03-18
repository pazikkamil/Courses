# Debugging
```bash
free -m
vmstat -m
```
vmstat -t 1 20

fuser -u -v /dev/urandom

# Disk IO
```bash
iotop -o
iostat -p ALL #shows usage of disks
```
# Top RAM usage
```bash
ps aux | tail -n +2 | sort -rnk 4
```

