# Partitions

## MBR (Master Boot Record)
Thiis is 512 bytes of storage device. Contains bootloader.
**C**(ylinder)**H**(eader)**S**(ector). Type of partitioning.
Have problem with larger partitions > 2TB

- Just 4 partitions
- 8 bit for partition type

## GPT - Globally Unique Identifier Partition Table.
LBA - type of partitioning

- Many partitions
- 128 bit for partition type

# LVM - Linux Volume Manager.
It helps to extend partitions on the fly - even from differend disks.
First sector of the device (offset 0)

## PE - Physical Extent
Is assigned to volume groups

- pvcreate

## VG - Volume Group
Has couple/one of physical volume

- vgcreate vg1 /dev/XXX

## LV - Logical Volume

- lvcreate -L 5G -n data vg1
- lvextend -L +5G /dev/vg1/data


## Snapshots

## Configure

- fdisk -l
- pvs (pvscan)
- pvcreate /dev/XXX
- vgcreate /dev/XXX
- vgcreate
- mkfs
- df -Th # filesystem + GB

## Schema and mount options

/tmp                    nodev,nosuid,noexec
/hom                    nodev, xattr

- nodev - dont support character or block special devices
- nosuid - ignore set user identifier / or group
- noexec - dont allow execute any binaries
- xattr - gives extra attributes like acls, selinux etc.. for ext4 
and other fs. 

cat /proc/fs/ext4/sda1/options | grep xattr

## Extending

- vgextend vg1 /dev/XXX

## Tools

- mount -a # mounts what reads from /etc/fstab