#!/bin/bash
homedir=$(pwd)
URL="https://www.goethe-verlag.com/book2/"

download002(){
	for L2 in PX ES EM FR IT DE; do 
		if [ ! -d $homedir"/get002/" ]; then mkdir -p $homedir"/get002/"; fi
		for L1 in PX ES EM FR IT DE; do
			if [ "$L2" != "$L1" ]; then
				curl -k "https://www.goethe-verlag.com/book2/"$L2"/"$L2""$L1"/"$L2""$L1"002.HTM" > $homedir"/get002/"$L2$L1"txt+audio.HTM"
				#https://www.goethe-verlag.com/book2/PX/PXFR/PXFR002.HTM
				cp $homedir"/get002/"$L2"txt+audio.HTM" $homedir"/get002/"$L2$L1"txt.HTM"
			fi
		done
	done
}

downloadphrases(){
	for L1 in PX ES EM FR IT DE; do
		for L2 in PX ES EM FR IT DE; do
			if [ "$L1" != "$L2" ]; then
				for x in {3..102}; do
					if [ $(echo $x | wc -c) == 2 ]; then
						y="00$x"
					elif [ $(echo $x | wc -c) == 3 ]; then
						y="0$x"
					elif [ $(echo $x | wc -c) == 4 ]; then
						y="$x"
					fi
					mkdir $homedir/phrases/$L1""$L2
					mkdir $homedir/phrases/$L1""$L2/$y
					curl -k "https://www.goethe-verlag.com/book2/"$L1"/"$L1""$L2"/"$L1""$L2""$y".HTM" > $homedir"/phrases/"$L1""$L2"/"$y"/"$L1""$L2""$y".HTM"
				done
			fi
		done
	done
}

downloadvocab(){
	for L1 in PX ES EM FR IT DE; do
		for L2 in PX ES EM FR IT DE; do
			if [ "$L1" != "$L2" ]; then
				for x in {1..42}; do
					if [ $(echo $x | wc -c) == 2 ]; then
						y="0$x"
					elif [ $(echo $x | wc -c) == 3 ]; then
						y="$x"
					fi
					mkdir $homedir/vocab/$L1""$L2
					mkdir $homedir/vocab/$L1""$L2/$y
					curl -k "https://www.goethe-verlag.com/book2/_VOCAB/"$L1"/"$L1""$L2"/"$y".HTM" > $homedir"/vocab/"$L1""$L2"/"$y"/"$y".HTM"
				done
			fi
		done
	done
}

clean002(){
	for L in ES PX EM FR IT JA ZH DE; do
		for F in $(ls $homedir/get002/$L*HTM); do
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

changenum002(){
	for L in PX ES EM FR IT DE; do
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

clearphrases(){
	#for x in {3..102}; do
	#	if [ $(echo $x | wc -c) == 2 ]; then
	#		y="00$x"
	#	elif [ $(echo $x | wc -c) == 3 ]; then
	#		y="0$x"
	#	elif [ $(echo $x | wc -c) == 4 ]; then
	#		y="$x"
	#	fi
	#done
	for F in $(find $homedir/phrases/ -type f -name "*.HTM"); do
		output=$F".clean"
		sed ':a;N;$!ba;s/\n//g' $F > $output
		sed -i 's#\r##g' $output
		sed -i 's#<title>#\n\#\##g' $output
		sed -i 's#<source src="https#\n\#\#https#g' $output
		sed -i 's#<span class="Stil36"><b>#\n\#\##g' $output
		sed -i 's#<span class="Stil36">#\n\#\##g' $output
		sed -i 's#</span><br /><br /></div></td></tr>#\#\#\n#g' $output
		sed -i 's#</b></span></div></td></tr></table>#\#\#\n#g' $output
		sed -i 's#<span class="Stil36"><b>#\n\#\##g' $output
		sed -i 's#<tr><td><div class="Stil35">#\n\#\##g' $output
		sed -i 's#</b></span></div></td></tr>#\#\#\n#g' $output
		sed -i 's#</div></td><td><div class=#\#\#\n#g' $output
		sed -i 's#" type="audio/mpeg" /></audio></td></tr>#\#\#\n#g' $output
		sed -i '/^##/!d' $output
		sed -i '/##$/!d' $output
		sed -i ':a;N;$!ba;s/\n//g' $output
		sed -i 's/.mp3####/.mp3\n/g' $output
		sed -i 's/####/|/g' $output
	done
}

changehtmlcodes(){	
	block1(){
		for file in $(find $homedir/phrases/ -type f -name "*.clean"); do
			if [ "$(grep '&#' $file)" ]; then
				grep -H '&#' $file > $homedir/lines.tmp
				sed -i 's/.clean:/.clean|/g' $homedir/lines.tmp
				while IFS="|" read Fname Code Url; do
					x=$(echo $Code | grep -o '&#' | wc -l)
					for (( y=1; y<=$x; y++)); do
						i=$(($y * 2)); 
						gotcode=$(echo $Code | awk -v a="$i" -F'[&;]' '{print ($a)}')
						echo "$Fname|&$gotcode;|$Url" | tee -a $homedir/changecodes.log
					done
				done < $homedir/lines.tmp
			fi
		done
		sed -i 's/.clean:/.clean|/g' $homedir/changecodes.log
	}
	block2(){
		while IFS="|" read Fname Code Url; do
			mycode=$(echo $Code | grep -o '&#.*;')
			if [ "$(grep $mycode htmlcodes)" ]; then
				replace=$(grep $mycode htmlcodes | awk -F"|" '{print $2}')
				#echo "$Fname|$mycode|$replace"
				sed -i "s/$mycode/$replace/g" $Fname
			else
				echo "$Fname|$mycode|Code not found" | tee -a $homedir/changehtmlcodes.err
			fi
		done < $homedir/changecodes.log
	}
	#if [ -f $homedir/changecodes.log ]; then
	#	read -p "File changecodes.log exist. Use it?" usefile
	#	if [ "$usefile" == "y" ]; then
	#		block2
	#	else
	#		block1
	#		block2
	#	fi
	#else
		block1
		block2
	#fi
}

clearphrases2(){
	for F in $(find $homedir/phrases/ -type f -name "*.clean"); do
		moveline1=$(grep '^##' $F | awk -F"|" '{print $2}')
		getline2=$(grep '^https' $F )
		newline2="$moveline1|$getline2"
		sed -i "s/|$moveline1|/|/g" $F
		sed -i "s/^https/$moveline1|https/g" $F
		sed -i 's/##//g' $F
	done
}

rename(){

	rm -f $homedir/rename.out
	for L1 in PX ES EM FR IT DE; do
		for L2 in EM PX ES FR IT DE; do
			if [ "$L1" != "$L2" ]; then
				for F in $(find $homedir/phrases/ -type f -name "$L1$L2*.clean"); do
					NewF=$(basename $F | cut -d. -f1)
					Dir=$(dirname $F)
					LF=$(echo $NewF | cut -c 1-4)
					NF=$(echo $NewF | cut -c 5-7)
					NewNF=$(expr $NF - 2)
					if [ $(echo $NewNF | wc -c) == 2 ]; then
						NewNF="00$NewNF"
					elif [ $(echo $NewNF | wc -c) == 3 ]; then
						NewNF="0$NewNF"
					elif [ $(echo $NewNF | wc -c) == 4 ]; then
						NewNF="$NewNF"
					fi
					newDir=$homedir/phrases/$LF/$NewNF-$(cat $F | awk 'NR==2' | awk -F"|" '{print $1}' | sed 's/ /_/g')
					newFName="$NewNF$LF-$(cat $F | awk 'NR==2' | awk -F"|" '{print $1}' | sed 's/ /_/g').txt"
					#newFName=$(echo $newFName | sed 's/ /_/g')
					mkdir $homedir/phrases/$LF
					mkdir $newDir
					mv $F $newDir/$newFName | tee -a $homedir/rename.out
					mv $Dir/*.mp3 $newDir
					#exit
				done
			fi
			#exit
		done
		#exit
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
#downloadphrases
#downloadvocab
#clean002
#changenum002
#clearphrases
#changehtmlcodes
#clearphrases2
rename
#changehtmlcodes
#####makebook
