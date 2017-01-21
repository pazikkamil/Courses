# Variables
zmienna=1
ciag="jakis tekst"

# Loops

```bash
for file in *.c; do echo ${file}; done
```
# If-s

if ((${i} % 2)); then echo "some rest"; fi

## If modulo
for i in $(seq 100); do if ((${i} % 2)); then echo ${i}; fi; done

## If statements

[ -e filepath ] true if file exists
[ -x filepath ] true if exist & executable
[ -S filepath ] tru if file exists and is socket
[ expr1 -a expr2 ] true if both are true
[ expr1 -o expr2 ] true if either of 1 / 2 is true

if [ -n $X ]; then 	# -n tests to see if the argument is non empty
	echo "the variable X is not the empty string"
fi

# Inputs
read zmienna
read -t 1 # read but timeout = 1 sec

# Comparisions
if [ $a -gt $b ]; then echo "wieksza a"; fi;

if [ $first -eq 0 ] && [ $second -eq 0 ]
then
	echo "Num1 and Num2 are zero"
elif [ $first -eq $second ]
then
	echo "Both Values are equal"
elif [ $first -gt $second ]
then
	echo "$first is greater than $second"
else
	echo "$first is lesser than $second"
fi

# Variable assignment
 
zmienna=`wc -l plik`
zmienna=$(wc -l plik)

# To remember !!!

* in comparision we use space bar
* in assignment we dont use space bar
=======

## Greps
grep -i -r "Cannot refresh"


## Std out / Errors out
find / -type f -iname "*.pem" 2> /dev/null


## Comparision of string
```bash
if [ "${X}" == "abc" ]; then echo "ok"; fi;
```
