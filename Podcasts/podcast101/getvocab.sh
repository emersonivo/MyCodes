#!/bin/bash
homedir=$(pwd)
for lang in chinese english french german italian japanese portuguese spanish; do
	mkdir $homedir"/goodvocab/"$lang
	mkdir $homedir"/goodvocab/"$lang"/extra"
done

for file in $(ls $homedir/goodvocab/*.lst); do
	if [ "$(echo $file | grep common)" ]; then
		while read line; do
			curl --user $username:$password -k "https://www.chineseclass101.com/chinese-vocabulary-lists/$line" > $homedir"/goodvocab/chinese/"$line".txt"
			curl --user $username:$password -k "https://www.englishclass101.com/english-vocabulary-lists/$line" > $homedir"/goodvocab/english/"$line".txt"
			curl --user $username:$password -k "https://www.frenchpod101.com/french-vocabulary-lists/$line" > $homedir"/goodvocab/french/"$line".txt"
			curl --user $username:$password -k "https://www.germanpod101.com/german-vocabulary-lists/$line" > $homedir"/goodvocab/german/"$line".txt"
			curl --user $username:$password -k "https://www.italianpod101.com/italian-vocabulary-lists/$line" > $homedir"/goodvocab/italian/"$line".txt"
			curl --user $username:$password -k "https://www.japanesepod101.com/japanese-vocabulary-lists/$line" > $homedir"/goodvocab/japanese/"$line".txt"
			curl --user $username:$password -k "https://www.portuguesepod101.com/portuguese-vocabulary-lists/$line" > $homedir"/goodvocab/portuguese/"$line".txt"
			curl --user $username:$password -k "https://www.spanishpod101.com/spanish-vocabulary-lists/$line" > $homedir"/goodvocab/spanish/"$line".txt"
		done < $file
	else
		for lang in portuguese spanish french chinese english german italian japanese; do
			if [ "$(echo $file | grep $lang)" ]; then
				outdir=$homedir"/goodvocab/"$lang
				while read infile; do
					if [ "$(echo $file | grep extra)" ]; then
						outdir=$homedir"/goodvocab/"$lang"/extra"
					fi
					if [ "$(echo $lang)" == "chinese" ]; then
						URL="https://www.chineseclass101.com/chinese-vocabulary-lists"
					elif [ "$(echo $lang)" == "english" ]; then
						URL="https://www.englishclass101.com/english-vocabulary-lists"
					elif [ "$(echo $lang)" == "french" ]; then
						URL="https://www.frenchpod101.com/french-vocabulary-lists"
					elif [ "$(echo $lang)" == "german" ]; then
						URL="https://www.germanpod101.com/german-vocabulary-lists"
					elif [ "$(echo $lang)" == "italian" ]; then
						URL="https://www.italianpod101.com/italian-vocabulary-lists"
					elif [ "$(echo $lang)" == "japanese" ]; then
						URL="https://www.japanesepod101.com/japanese-vocabulary-lists"
					elif [ "$(echo $lang)" == "portuguese" ]; then
						URL="https://www.portuguesepod101.com/portuguese-vocabulary-lists"
					elif [ "$(echo $lang)" == "spanish" ]; then
						URL="https://www.spanishpod101.com/spanish-vocabulary-lists"
					fi
					curl --user $username:$password -d -k "$URL/$infile" > $outdir"/"$infile
					#https://www.chineseclass101.com/chinese-vocabulary-lists/bugs-and-insects
				done < $file
			fi
		done
	fi
done
bash -x cleanvocab.sh | tee -a $homedir/cleanvocab.out