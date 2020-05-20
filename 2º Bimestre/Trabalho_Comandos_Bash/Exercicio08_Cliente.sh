#!/bin/bash

echo "Nathan Mainka Soares"
echo "Nathan Mainka Soares" > cliente_1.txt && less cliente_1.txt
ls -a
echo "Joinville" >> cliente_1.txt 
cat cliente_1.txt 
mkdir clientes
ls -la
mv ./cliente_1.txt ./clientes
cd clientes/
ls -la
cp ./cliente_1.txt ./cliente_1.txt.bkp
cat cliente_1.txt.bkp 
ls -la
rm cliente_1.txt
ls -la
