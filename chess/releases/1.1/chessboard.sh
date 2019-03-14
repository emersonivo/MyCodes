#!/bin/bash
numlin=8
numcol=8
lastcel=$numlin$numcol
(( lastcel=$lastcel+1 ))
homedir="/bkp_local/MyCodes/chess"
tmp="$homedir/tmp"
#rm -fr $tmp/*

createboard(){
for (( x=1; x<=$numlin; x++ )); do
    #lin=""
    for (( y=1; y<=$numcol; y++ )); do 
        lin="$lin;$x$y"
    done
done
echo $lin > $homedir/board/board.txt
}
getdiag(){
    for (( x=1; x<=$numlin; x++ )); do
        for (( y=1; y<=$numcol; y++ )); do
            lincol=$x$y
            if [[ $x -eq 1 && y -eq 1 ]]; then
                var=""
                for (( p=11; p<=$lastcel; p=p+11 )); do
                    var="$var;$p"
                done
                echo $var > $homedir/diags/diag$x$y.txt
            elif [[ $x -eq 1 && $y -gt 1 ]]; then
                beg=$x$y
                (( end=$lastcel+10-(y*10) ))
                var=""
                for (( p=$beg; p<=$end; p=p+11 )); do
                    var="$var;$p"
                done
                echo $var > $homedir/diags/diag$x$y.txt
            elif [[ $x -gt 1 && y -eq 1 ]]; then
                beg=$x$y
                end=$y$x
                var=""
                for (( p=$beg; p>=$end; p=p-9 )); do
                    var="$var;$p"
                done
                echo $var > $homedir/diags/diag$x$y.txt
            elif [[ $x -ge 0 && y -eq 8 ]]; then
                beg=$x$y
                end=$y$x
                var=""
                for (( p=$beg; p<=$end; p=p+9 )); do
                   var="$var;$p"
                done
                echo $var > $homedir/diags/diag$x$y.txt
            elif [[ $x -eq 8 && $y -gt 0 ]]; then
                beg=$x$y
                end=$y$x
                var=""
                for (( p=$beg; p>=$end; p=p-9 )); do
                    var="$var;$p"
                done
                echo $var > $homedir/diags/diag$x$y.txt
            fi
        done
    done
}

getlin(){
for (( x=1; x<=$numlin; x++ )); do
    var=""
    for (( y=1; y<=$numcol; y++ )); do
        var="$var;$x$y"
    done
        echo $var > $homedir/lines/lin$x$y.txt
done
}

getcol(){
for (( x=1; x<=$numlin; x++ )); do
    var=""
    for (( y=1; y<=$numcol; y++ )); do
        var="$var;$y$x"
    done
        echo $var > $homedir/cols/col$y$x.txt
done
}

createboard
getdiag
getlin
getcol

cp -fr $homedir/lines/ $tmp/; cp -fr $homedir/cols/ $tmp/; cp -fr $homedir/diags $tmp/; cp -fr $homedir/board/ $tmp/
find $homedir/ -name "*.txt" -exec sed -i 's/^;//g' {} \;

makemoney(){
for (( q=1; q<=8; q++ )); do
    if [ -f $tmp/board/board.txt ]; then
        first=$(cat $tmp/board/board.txt | awk -F";" '{print $1'})
        Q$q=$(echo $first)
        if [ $q -eq 1 ]; then
            FirstQueem=$(echo $Q$q)
        fi
        exit
        blockcol=$(grep $Q$q $tmp/cols/* | awk -F":" '{print $2'})
        blocklin=$(grep $Q$q $tmp/lines/* | awk -F":" '{print $2'})
        blockdia=$(grep $Q$q $tmp/diags/* | awk -F":" '{print $2'})
        Qblock="$blockcol;$blocklin;$blockdia"
        echo $Qblock > $tmp/board/Qblock.txt
        cat $tmp/board/board.txt
        for i in ${Qblock//;/ }
        do
            #echo $i
            sed -i "s/$i//g;s/;;/;/g;s/^;//g;s/;$//g" $tmp/board/board.txt
        done #< $tmp/board/Q1block.txt
        cat $tmp/board/board.txt
        exit
    fi
done
}
#makemoney
