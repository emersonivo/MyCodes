#!/bin/bash
homedir="/drives/h/Podcasts101"
input="$homedir/lists/portuguese-vocabulary-lists.txt"
nada(){
for file in $(ls $homedir/lists/*.txt); do
	if [ "$(basename $file)" != "$(basename $input)" ]; then
		while read line; do
			if [ "$( grep $line $input )" ]; then
				echo "$line" >> $homedir"/lists/"$(basename $file | cut -d '.' -f1)"_pt.lst"
			else
				echo "$line" >> $homedir"/lists/"$(basename $file | cut -d '.' -f1)"_pt-extra.lst"
			fi
		done < $file
	fi
done
}

while read ptline; do
	if [ "$(grep "^$ptline" $homedir/lists/*-lists.txt | wc -l)" -gt 7 ]; then
			echo $ptline >> $homedir/vocab/vocabulary-lists_common.lst
			#sed -i "/$ptline/d" $homedir"/lists/"$lang*
	else
		for lang in chinese english french german italian japanese portuguese spanish; do
			if [ "$(grep "^$ptline" $homedir'/lists/'$lang'-vocabulary-lists.txt')" ]; then
				echo $ptline >> $homedir/vocab/$lang-vocabulary-lists_pt-extra.lst
			fi
		done
	fi
done < $input