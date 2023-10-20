#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Uso: $0 <imagen_entrada> <color_hex>"
  exit 1
fi

imagen_entrada="$1"
color_hex="$2"

nombre_base=$(basename -- "$imagen_entrada")
nombre_salida="${nombre_base%.*}-colorized.${nombre_base##*.}"

convert "$imagen_entrada" -fill "$color_hex" -colorize 100% "$nombre_salida" && \
convert "$imagen_entrada" "$nombre_salida" -compose multiply -composite "$nombre_salida"
