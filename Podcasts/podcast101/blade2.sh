#!/bin/bash
homedir="/drives/h/Podcasts101"

Lines="""
ES|https://www.spanishpod101.com/spanish-vocabulary-lists
JA|https://www.japanesepod101.com/japanese-vocabulary-lists
DE|https://www.germanpod101.com/german-vocabulary-lists
IT|https://www.italianpod101.com/italian-vocabulary-lists
BR|https://www.portuguesepod101.com/portuguese-vocabulary-lists
CH|https://www.chineseclass101.com/chinese-vocabulary-lists
FR|https://www.frenchpod101.com/french-vocabulary-lists
"""
y=1
while read vocaburl; do	
	for line in $Lines; do
		Lang=$(echo $line | cut -d"|" -f1)
		Url=$(echo $line | cut -d"|" -f2)
		if [ ! -d "$homedir/$Lang" ]; then mkdir $homedir"/"$Lang; fi
		
		if [ $(echo $y | wc -c) == 2 ]; then
			fcount="00$y"
		elif [ $(echo $y | wc -c) == 3 ]; then
			fcount="0$y"
		elif [ $(echo $y | wc -c) == 4 ]; then
			fcount="$y"
		fi		
		mkdir $homedir"/"$Lang"/"$fcount"-"$vocaburl
		mypath=$homedir"/"$Lang"/"$fcount"-"$vocaburl
		uid="$username:$password"
		if [ "$Lang" == "ES" ]; then
			if [ ! "$(curl --user $uid -k $Url"/"$vocaburl)" ]; then
				if [ ! "$(curl --user $uid -k $Url"/"$vocaburl"-mexican-spanish")" ]; then
					echo "$fcount|$Lang|$Url|Not found" >> $homedir/getpod101.err
				else
					curl --user $uid -k $Url"/"$vocaburl"-mexican-spanish" > $mypath/$vocaburl"-mexican-spanish.html"
					input=$mypath/$vocaburl"-mexican-spanish.html"
				fi
			else
				curl --user $uid -k $Url"/"$vocaburl > $mypath"/"$vocaburl".html"
				input=$mypath/$vocaburl".html"
			fi
		else
			if [ ! "$(curl --user $uid -k $Url"/"$vocaburl)" ]; then
				echo "$Lang|$Url|Not found" >> $homedir/getpod101.err
			else
				curl --user $uid -k $Url"/"$vocaburl > $mypath"/"$vocaburl".html"
				input=$mypath/$vocaburl".html"
			fi
		fi
		if [ -f $input ]; then
			output=$input".out"
			lang=$(echo ${Lang,,})
			grep 'span class\|audio src' $input > $output
			sed -i "s/^[ \t]*//" $output
			sed -i ':a;N;$! ba;s/\n//g' $output
			sed -i "s/<audio src=\"/\n<audio src=\"/g" $output
			sed -i '/^<audio/!d' $output
			sed -i '/audio_preview/d' $output
			sed -i 's#" preload="none"></audio><span class="wlv-item__word js-wlv-word" lang="'$lang'">#|#g' $output
			sed -i 's#" preload="none"></audio><span class="wlv-item__english js-wlv-english">#|#g' $output
			sed -i 's#" preload="none"></audio><span class="wlv-item__word" lang="'$lang'">#|#g' $output
			sed -i 's#" preload="none"></audio><span class="wlv-item__english" lang="'$lang'">#|#g' $output
			sed -i 's#" preload="none"></audio><span class="wlv-item__english js-wlv-english">#|#g' $output
			sed -i 's#</span>#\n#g' $output
			sed -i 's#<audio src="##g' $output
			sed -i 's#title=#\n#g' $output
			sed -i '/^http/!d' $output
			sed -i 's/ /_/g' $output
			sed -i 's/\.$//g; s/,/_/g; s/\?//g' $output
		fi
	done
#		y=1
#		while IFS="|" read Url fname; do
#			if [ $(echo $y | wc -c) == 2 ]; then
#				fcount="00$y"
#			elif [ $(echo $y | wc -c) == 3 ]; then
#				fcount="0$y"
#			elif [ $(echo $y | wc -c) == 4 ]; then
#				fcount="$y"
#			fi
#			if [ ! -d "$Lang" ]; then mkdir $mydir/$Lang ; fi
#				destfile="$Lang/$fcount-$fname.mp3"
#			if [ "$Lang" == "DE" ]; then
#				DEname=$fname
#				DEurl=$Url
#				Lang="EN"
#			else
#				ENname=$fname
#				ENurl=$Url
#				curl -k $ENurl > "$mydir/$Lang/$fcount-$ENname-DE-$DEname.mp3"
#				if [ -f "$mydir/$Lang/$fcount-$ENname-DE-$DEname.mp3" ]; then
#					echo -e "$fcount - EN-$ENname / DE-$DEname\n" >> "$mydir/Phrases.txt"
#					Lang="DE"
#					curl -k $DEurl > "$mydir/$Lang/$fcount-$DEname-EN-$ENname.mp3"
#					(( y++ ))
#				else
#					echo "$Url;$fname" >> /drives/h/germanpop1/wrong-path.log
#				fi
#			fi
#		done < $output
	(( y++ ))
	#if [ $y -eq 4 ]; then exit; fi
done < $1