#!/bin/bash

DIRECTORIO="./"

find "$DIRECTORIO" -type f \( -iname "*.mp4" -o -iname "*.mkv" -o -iname "*.webm" \) | while read -r archivo; do
    codec=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name \
             -of default=noprint_wrappers=1:nokey=1 "$archivo")

    if [[ "$codec" == "hevc" ]]; then
        echo "$archivo"
    fi
done
