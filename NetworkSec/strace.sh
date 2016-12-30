#!/usr/bin/env bash

# just open calls from ls
strace -e open ls
strae -e trace=open,read ls

# save output to file
strace -o output.txt ls

# trace specific process
pgrep firefox-bin
sudo strace -p 1725 -o firefox_trace.txt

# print timestamps
strace -t -e open ls /home
strace -tt -e open ls /home
strace -ttt -e open ls /home

# print summary
strace -vc ./proces

# summary + contionous output
strace -C ./proces

"""
﻿% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
100.00    0.000098           1       100           read
  0.00    0.000000           0         2           write
  0.00    0.000000           0        84        15 open
  0.00    0.000000           0        83           close
  0.00    0.000000           0       206        24 stat
  0.00    0.000000           0       116           fstat
  0.00    0.000000           0         8           lstat
  0.00    0.000000           0        51         6 lseek
  0.00    0.000000           0        71           mmap
  0.00    0.000000           0        17           mprotect
  0.00    0.000000           0        24           munmap
  0.00    0.000000           0        18           brk
  0.00    0.000000           0        67           rt_sigaction
  0.00    0.000000           0         1           rt_sigprocmask
  0.00    0.000000           0        13         1 ioctl
  0.00    0.000000           0         9         9 access
  0.00    0.000000           0         3           dup
  0.00    0.000000           0         1           socket
  0.00    0.000000           0         1           bind
  0.00    0.000000           0         1           listen
  0.00    0.000000           0         1           clone
  0.00    0.000000           0         1           execve
  File "/usr/lib/python3.5/socket.py", line 195, in accept
    fd, addr = self._accept()
  0.00    0.000000           0         1           fcntl
  0.00    0.000000           0        22           getdents
  0.00    0.000000           0         1           getcwd
  0.00    0.000000           0         2         2 readlink
  0.00    0.000000           0         1           getrlimit
  0.00    0.000000           0         1           getuid
  0.00    0.000000           0         1           getgid
  0.00    0.000000           0         1           geteuid
  0.00    0.000000           0         1           getegid
  0.00    0.000000           0         1           sigaltstack
  0.00    0.000000           0         1           arch_prctl
  0.00    0.000000           0         7         2 futex
  0.00    0.000000           0         1           set_tid_address
  0.00    0.000000           0        11           openat
  0.00    0.000000           0         1           set_robust_list
  0.00    0.000000           0         1           accept4
------ ----------- ----------- --------- --------- ----------------
100.00    0.000098                   932        59 total
"""