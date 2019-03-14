#!/bin/bash
homedir=$(pwd)
for lang in french chinese english german italian japanese portuguese spanish; do
	for file in $(find $homedir/goodvocab/$lang -type f -name "*.txt"); do
		for line in $(cat $file | grep https); do
			URL=$(echo $line | cut -d '|' -f1)
			cd $homedir/goodvocab/$lang/
			wget $URL
		done
	done
done