#!/bin/bash
homedir=$(pwd)
for F in $(find $homedir/phrases/ -type f -name "*.clean"); do
	Dir=$(dirname $F)
	while IFS="|" read phrase url; do
		cd $Dir
		wget --no-check-certificate $url
	done < $F
done