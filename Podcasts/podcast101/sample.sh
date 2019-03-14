#!/bin/bash
homedir="/drives/h/Podcasts101/"
for UpperL in FR; do
	if [ "$UpperL" == "FR" ]; then 
	    x="french"
		l="fr"
	elif [ "$UpperL" == "DE" ]; then
	    x="german"
		l="de"		
	elif [ "$UpperL" == "ES" ]; then
	    x="spanish"
		l="es"	
	fi
	project=$x"pod101"
	#cd /drives/h/Podcasts101/$project/2000\ Most\ Common\  
	workdir="/drives/h/Podcasts101/$project/2000_Most_Common_Words"
	echo $(pwd)
    for f in $(ls $workdir/*.html); do
	    #URLx="https://www."$x"pod101.com/"$x"-word-lists/?coreX="$n
		input=$f
		output=$workdir/$UpperL"_"$(basename $f)
		#if [ "$(curl -k $URLx >> $input)" ]; then
		#	curl -k $URLx >> $input
		#else
		#	wget --no-check-certificate $URLx --output-document=$input
		#fi
		grep 'span class\|audio src' $input >> $output
		sed -i "s/^[ \t]*//" $output; tail -n10 $output
		sed -i ':a;N;$! ba;s/\n//g' $output; tail -n10 $output
		sed -i "s/<audio src=\"/\n<audio src=\"/g" $output; tail -n10 $output
		sed -i '/^<audio/!d' $output; tail -n10 $output
		sed -i '/audio_preview/d' $output; cat $output
		sed -i 's#</span>#\n#g' $output; cat $output
		sed -i 's#<audio src="##g' $output; cat $output
		sed -i '/^https/!d' $output; cat $output
		sed -i "s#\" preload=\"none\"></audio><span class=\"wlv-item__english\" lang=\"$l\">#;#g" $output; cat $output
		sed -i "s#\" preload=\"none\"></audio><span class=\"wlv-item__word js-wlv-word\" lang=\"$l\">#;#g" $output; cat $output
		sed -i "s#\" preload=\"none\"></audio><span class=\"wlv-item__english js-wlv-english\">#;#g" $output; cat $output
		sed -i "s#\" preload=\"none\"></audio><span class=\"wlv-item__word\" lang=\"$l\">#;#g" $output; cat $output
		sed -i "s#\"_preload*_lang=\""$x\"">#;#g" $output; cat $output
		sed -i 's#"_preload*english">#;#g' $output; cat $output
		sed -i 's#\r##g' $output; cat $output
		sed -i 's#title=#\n#g' $output; cat $output
		sed -i 's/ /_/g' $output; cat $output
		sed -i 's/\.$//g; s/,/_/g; s/\?//g' $output; cat $output
	done
done
cd $homedir