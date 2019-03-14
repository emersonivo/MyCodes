#!/bim/bash
homedir=$(pwd)

block1(){
	rm $homedir/changecodesfilename.log
	for names in $(find phrases/ -type d -name "*https#*"); do 
		newname=$(echo $names | sed 's/https#/\&#/g')
		x=$(echo $newname | grep -o '&#' | wc -l)
		for (( y=1; y<=$x; y++)); do
			i=$(($y * 2)); 
			gotcode=$(echo $newname | awk -v a="$i" -F'[&;]' '{print ($a)}')
			echo "$names|https$gotcode|&$gotcode;" | tee -a $homedir/changecodesfilename.log
		done	
	done
}

block2(){
	rm $homedir/renamehtmlremoved.log $homedir/changehtmlcodesfilename.err
	while IFS="|" read Fname badCode Code; do
		mycode=$(echo $Code | grep -o '&#.*;')
		if [ "$(grep $mycode htmlcodes)" ]; then
			replace=$(grep $mycode htmlcodes | awk -F"|" '{print $2}')
			#echo "$Fname|$mycode|$replace"
			newname=$(echo $Fname | sed "s/$badCode;/$replace/g")
			mv $Fname $newname | tee -a $homedir/renamehtmlremoved.log
		else
			echo "$Fname|$mycode|Code not found" | tee -a $homedir/changehtmlcodesfilename.err
		fi
	done < $homedir/changecodesfilename.log
}

block1
block2