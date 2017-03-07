# Logging

## Script for collecting log
```bash
cat /home/kamil/Desktop/postgres_old_all.csv | tr ',' '\n' | grep 'duration:' | grep -Eo '[.0-9]+ ms' | sort -n | cut -f 1 -d " "|  xargs  | sed -e 's/\ /+/g' | bc
```

