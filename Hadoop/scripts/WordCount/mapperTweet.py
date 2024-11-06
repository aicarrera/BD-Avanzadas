#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

# Leer la entrada como CSV
reader = csv.reader(sys.stdin)

# Ignorar la cabecera
next(reader)

for row in reader:
    # Asegurarse de que hay suficientes campos en la fila
    if len(row) > 9:
        tweet = row[9]  # Suponiendo que el campo Tweet es el tercero (índice 2)
        tweet = tweet.replace('\n', ' ')  # Reemplazar saltos de línea por espacio
        words = tweet.split()  # Dividir el tweet en palabras
        for word in words:
            # Emitir cada palabra con el conteo de 1
            print('%s\t%s' % (word, 1))

