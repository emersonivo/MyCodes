#!/bin/bash
x=1
for i in $(cat $1); do
    if [ $(echo $x | wc -c) == 2 ]; then
        dir="00$x"
    elif [ $(echo $x | wc -c) == 3 ]; then
        dir="0$x"
    elif [ $(echo $x | wc -c) == 4 ]; then
        dir="$x"
    fi
    mkdir "$dir-$i"
    mydir="$dir-$i"
    mypath="$mydir/$i"
    curl -k https://www.frenchpod101.com/french-vocabulary-lists/$i > $mypath
	output=$mypath.out
	grep 'span class\|audio src' $mypath > $output
	sed -i "s/^[ \t]*//" $output
	sed -i ':a;N;$! ba;s/\n//g' $output
	sed -i "s/<audio src=\"/\n<audio src=\"/g" $output
	sed -i '/^<audio/!d' $output
	sed -i '/audio_preview/d' $output
	sed -i 's#" preload="none"></audio><span class="wlv-item__word js-wlv-word" lang="fr">#;#g' $output
	sed -i 's#" preload="none"></audio><span class="wlv-item__english js-wlv-english">#g' $output
	sed -i 's#" preload="none"></audio><span class="wlv-item__word" lang="fr">#;#g' $output
	sed -i 's#" preload="none"></audio><span class="wlv-item__english" lang="fr">#;#g' $output
	sed -i 's#" preload="none"></audio><span class="wlv-item__english js-wlv-english">#;#g' $output
	sed -i 's#</span>#\n#g' $output
	sed -i 's#<audio src="##g' $output
	sed -i 's#title=#\n#g' $output
	sed -i '/^https/!d' $output
	sed -i 's/ /_/g' $output
	sed -i 's/\.$//g; s/,/_/g; s/\?//g' $output

	Lang="FR"
	y=1
	while IFS=";" read Url fname; do
		if [ $(echo $y | wc -c) == 2 ]; then
			fcount="00$y"
		elif [ $(echo $y | wc -c) == 3 ]; then
			fcount="0$y"
		elif [ $(echo $y | wc -c) == 4 ]; then
			fcount="$y"
		fi



		if [ ! -d "$Lang" ]; then mkdir $mydir/$Lang ; fi
		destfile="$Lang/$fcount-$fname.mp3"
#		curl -k $Url > $mydir/$destfile
		if [ "$Lang" == "FR" ]; then
		    FRname=$fname
		    FRurl=$Url
		    Lang="EN"
		else
		    ENname=$fname
                    ENurl=$Url
		    curl -k $ENurl > "$mydir/$Lang/$fcount-$ENname-FR-$FRname.mp3"
#		    echo "$FRurl;$fcount-$FRname-EN-$ENname.mp3"
#		    echo "$ENurl;$fcount-$ENname-FR-$FRname.mp3"
		    Lang="FR"
		    curl -k $FRurl > "$mydir/$Lang/$fcount-$FRname-EN-$ENname.mp3"
		    (( y++ ))
		fi
	done < $output
	#exit
    (( x++ ))
done
