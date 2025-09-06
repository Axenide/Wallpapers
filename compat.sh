mkdir -p .backup

for f in *.mp4 *.mkv; do
    codec=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name \
        -of default=noprint_wrappers=1:nokey=1 "$f")
    if [ "$codec" = "av1" ]; then
        tmpfile="${f%.*}_h265.${f##*.}"
        ffmpeg -i "$f" -c:v libx265 -pix_fmt yuv420p -tag:v hvc1 \
               -c:a copy -c:s copy "$tmpfile"
        if [ $? -eq 0 ]; then
            mv "$f" ".backup/$f"
            mv "$tmpfile" "$f"
            echo "Convertido: $f"
        else
            echo "❌ Error al convertir: $f"
            rm -f "$tmpfile"
        fi
    fi
done
