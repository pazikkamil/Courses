# LVM - Linux Volume Manager.
It helps to extend partitions on the fly - even from differend disks.

## PE - Physical Extent
Is assigned to volume groups

- pvcreate

## VG - Volume Group
Has couple/one of phisical volume

- vgcreate vg1 /dev/XXX


## Snapshots

## Configure

- fdisk -l
- pvs (pvscan)
- pvcreate /dev/XXX
- vgcreate /dev/XXX
- vgcreate