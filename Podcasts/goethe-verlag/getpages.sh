#!/bin/bash
homedir=$(pwd)
URL="https://www.goethe-verlag.com/book2/"

download002(){
	for L in ES; do #EM FR IT JA ZH DE; do 
		wget --no-check-certificate "https://www.goethe-verlag.com/book2/PX/PX"$L"/PX"$L"002.HTM"
		wget --no-check-certificate "https://www.goethe-verlag.com/book2/"$L"/"$L"PX/"$L"PX002.HTM"
	done
}

clean002(){
	for L in ES; do # PX EM FR IT JA ZH DE; do
		for F in $(ls $L*HTM); do
			NewF=$(echo $F | cut -d. -f1)
			pattern='<a href="'$L
			grep "$pattern" $F > $NewF.clear
			sed -i 's#<a href="##g' $NewF.clear
			sed -i 's#"><span class="gray">#;#g' $NewF.clear
			sed -i 's# </span>#;#g' $NewF.clear
			sed -i 's#</a>##g' $NewF.clear
			sed -i '#BUY the BOOK#d' $NewF.clear
		done
	done
}

changenum(){
	for L in ES EM FR IT DE; do
		for F in $(ls $L*clear); do
			NewF=$(echo $F | cut -d. -f1)
			for line in $(cat $F); do
				p=$(echo $line | awk -F";" '{print $1}')
				x=$(echo $line | awk -F";" '{print $2}')
				n=$(echo $line | awk -F";" '{print $3}')
				if [ $(echo $x | wc -c) == 2 ]; then
					y="00$x"
				elif [ $(echo $x | wc -c) == 3 ]; then
					y="0$x"
				elif [ $(echo $x | wc -c) == 4 ]; then
					y="$x"
				fi
				echo "$p;$y;$n" >> $NewF.num
			done
		done
	done
}

makebook(){
	if [ -f mypolibook.csv ]; then rm mypolibook.csv ; fi
	for line in $(cat PXFR002.num); do
		num=$(echo $line | awk -F";" '{print $2}')
		pxnom=$(grep ";$num;" PXFR002.num | awk -F";" '{print $3}')
		emnom=$(grep ";$num;" EMPX002.num | awk -F";" '{print $3}')
		frnom=$(grep ";$num;" FRPX002.num | awk -F";" '{print $3}')
		denom=$(grep ";$num;" DEPX002.num | awk -F";" '{print $3}')
		esnom=$(grep ";$num;" ESPX002.num | awk -F";" '{print $3}')
		itnom=$(grep ";$num;" ITPX002.num | awk -F";" '{print $3}')
		echo "$num;$pxnom;$emnom;$frnom;$denom;$esnom;$itnom" >> mypolibook.csv
	done
}

downloadphrases(){
	for x in {3..102}; do
		if [ $(echo $x | wc -c) == 2 ]; then
			y="00$x"
		elif [ $(echo $x | wc -c) == 3 ]; then
			y="0$x"
		elif [ $(echo $x | wc -c) == 4 ]; then
			y="$x"
		fi
		mkdir -p $homedir/vocab/$y
		curl -k "https://www.goethe-verlag.com/book2/PX/PXEM/PXEM"$y".HTM" > "$homedir/vocab/"$y"/PXEM"$y".HTM"
		                             #https://www.goethe-verlag.com/book2/PX/PXDE/PXDE003.HTM
		for L in ES EM FR IT JA ZH DE; do 			
			curl -k "https://www.goethe-verlag.com/book2/"$L"/"$L"PX/"$L"PX"$y".HTM" > "$homedir/vocab/"$y"/"$L"PX"$y".HTM"
		done
	done
}

downloadvocab(){
	for x in {1..42}; do
		if [ $(echo $x | wc -c) == 2 ]; then
			y="0$x"
		elif [ $(echo $x | wc -c) == 3 ]; then
			y="$x"
		fi
		#https://www.goethe-verlag.com/book2/_VOCAB/PX/PXDE/42.HTM
		mkdir -p $homedir/vocab/$y
		curl -k "https://www.goethe-verlag.com/book2/_VOCAB/PX/PXEM/"$y".HTM" > "$homedir/vocab/"$y"/PXEM"$y".HTM"
		                             #https://www.goethe-verlag.com/book2/PX/PXDE/PXDE003.HTM
		for L in ES EM FR IT JA ZH DE; do
			if [ ! -f "$homedir/vocab/"$L"PX.HTM" ]; then
				curl -k "https://www.goethe-verlag.com/book2/_VOCAB/"$L"/"$L"PX/"$L"PX.HTM"	> "$homedir/vocab/"$L"PX.HTM"
			fi
			curl -k "https://www.goethe-verlag.com/book2/_VOCAB/"$L"/"$L"PX/"$y".HTM" > "$homedir/vocab/"$y"/"$L"PX"$y".HTM"
		done
	done
}

clearphrases(){
	for x in {3..102}; do
		if [ $(echo $x | wc -c) == 2 ]; then
			y="00$x"
		elif [ $(echo $x | wc -c) == 3 ]; then
			y="0$x"
		elif [ $(echo $x | wc -c) == 4 ]; then
			y="$x"
		fi

		for f in $(ls $homedir/phrases/$y); do
			input="$homedir/phrases/$y/$f"
			output="$homedir/phrases/$y/$f.clean"
			sed ':a;N;$!ba;s/\n//g' $input > $output
			sed -i 's#\r##g' $output
			sed -i 's#<source src="https#\n\#\#https#g' $output
			sed -i 's#<span class="Stil36"><b>#\n\#\##g' $output
			sed -i 's#<tr><td><div class="Stil35">#\n\#\##g' $output
			sed -i 's#</b></span></div></td></tr>#\#\#\n#g' $output
			sed -i 's#</div></td><td><div class=#\#\#\n#g' $output
			sed -i 's#" type="audio/mpeg" /></audio></td></tr>#\#\#\n#g' $output
			sed -i '/^##/!d' $output
			sed -i '/##$/!d' $output
			sed -i ':a;N;$!ba;s/\n//g' $output 
			sed -i 's/####https/|https/g' $output
			sed -i 's/####/\n###/g' $output
			sed -i 's/###//g' $output
			sed -i 's/##//g' $output
		done
	done
}

downloadmp3phrases(){
	for x in {3..102}; do
		if [ $(echo $x | wc -c) == 2 ]; then
			y="00$x"
		elif [ $(echo $x | wc -c) == 3 ]; then
			y="0$x"
		elif [ $(echo $x | wc -c) == 4 ]; then
			y="$x"
		fi

		for f in $(ls $homedir/phrases/$y/*.clean); do
			for line in $(cat $f | grep -v '^https'); do
				if [ "$(echo $line | grep -o 'https' | wc -l )" -gt 1 ]; then
					URL=$(echo $line | cut -d '|' -f3)
				else
					URL=$(echo $line | cut -d '|' -f2)
				fi
				cd $homedir/phrases/$y/
				wget $URL
			done
		done
	done
}

nada(){
	#<tr><td><div class="Stil35">eu</div></td><td>
	#<tr><td><div class="Stil35">I</div></td><td>
	#<audio id="3"><source src="https://www.book2.nl/book2/EM/SOUND/0003.mp3" type="audio/mpeg" /></audio></td>
	#<audio id="3"><source src="https://www.book2.nl/book2/PX/SOUND/0003.mp3" type="audio/mpeg" /></audio></td>

	while IFS=";" read file path; do 
		mkdir $path
		cd $path
		wget --no-check-certificate https://www.goethe-verlag.com/book2/PX/PX$L/$file
		for line in $(grep -o 'https://www.book2.nl/book2/ZH/SOUND/........' $file); do
			wget --no-check-certificate $line
		done
		cd ..
	done < chindex
}

#download002
#clean002
#changenum
#makebook
#downloadphrases
#downloadvocab
#clearphrases
downloadmp3phrases

