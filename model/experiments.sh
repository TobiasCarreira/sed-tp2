i=0
for file in prisioneros.ma.[0-9]*
do
    if [ $i -gt 349 ]
    then
        mkdir -p log-$i
        ../CDPP_ExtendedStates-codename-Santi/src/bin/cd++ -m $file -t 00:10:00:000 -l log-$i/log.log
        echo $i
    fi
    i=$((i+1))
done