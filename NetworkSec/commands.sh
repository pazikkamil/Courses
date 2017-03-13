#!/usr/bin/env bash

sudo netstat -plnt
# n - numberic
# t - tcp
# l - listening
# p - proces which listens

# root@kali:~/code/Courses/NetworkSec# netstat -plnt
# Active Internet connections (only servers)
# Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
# tcp        0      0 0.0.0.0:9999            0.0.0.0:*               LISTEN      3151/python3.5

sudo lsof

lsof -i tcp
lsof -p PID
