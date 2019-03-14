#!/bin/bash
block1(){
	for file in $(find . -name "TESTEFR.*"); do
	    if [ "$(grep '&#' $file)" ]; then
	    	grep -H '&#' $file | tee -a changecodes.log
	    fi
	done
	sed -i 's/.clean:/.clean|/g' changecodes.log
}

block2(){
	#./TESTEFR.HTM.clean|l&#8217;homme|https://www.book2.nl/book2/PX/SOUND/0009.mp3
	while IFS="|" read Fname Code Url; do
		mycode=$(echo $Code | grep -o '&#.*;')
		if [ "$(grep $mycode htmlcodes)" ]; then
			replace=$(grep $mycode htmlcodes | awk -F"|" '{print $2}')
			echo "$Fname|$mycode|$replace"
			sed -i "s/$mycode/$replace/g" $Fname
		else
			echo "$Fname|$mycode|Code not found"
		fi
	done < changecodes.log
}

block2