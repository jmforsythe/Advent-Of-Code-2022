for i in *.cpp; do
    [ -f "$i" ] || break
    g++ $i -o ${i%.*}.exe
done