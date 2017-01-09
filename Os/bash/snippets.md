# Loops

for file in *.c; do echo ${file}; done

# If-s

if ((${i} % 2)); then echo "some rest"; fi

## If modulo
for i in $(seq 100); do if ((${i} % 2)); then echo ${i}; fi; done
