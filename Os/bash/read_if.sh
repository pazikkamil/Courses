#!/usr/bin/env bash
read wejscie
if [ "${wejscie}" == "y" -o "${wejscie} == "Y" ]
then echo "YES"
elif [ "${wejscie}" == "n" -o "${wejscie} == "N" ]
then echo "NO"
fi
