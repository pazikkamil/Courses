# How to get drivers list
- basename $(readlink /sys/class/net/eth0/device/driver/module)
- lsmod | cut --fields=1 -d " " | sort
