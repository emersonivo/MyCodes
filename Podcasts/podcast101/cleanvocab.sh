#!/bin/bash
homedir=$(pwd)
for lang in french chinese english german italian japanese portuguese spanish; do
	for file in $(find $homedir/goodvocab/$lang -type f -name "*.txt"); do
		if [ "$lang" == "french" ]; then shortl="fr"; fi
		if [ "$lang" == "chinese" ]; then shortl="zh"; fi
		if [ "$lang" == "english" ]; then shortl="en"; fi
		if [ "$lang" == "german" ]; then shortl="de"; fi
		if [ "$lang" == "italian" ]; then shortl="it"; fi
		if [ "$lang" == "japanese" ]; then shortl="jp"; fi
		if [ "$lang" == "portuguese" ]; then shortl="pt"; fi
		if [ "$lang" == "spanish" ]; then shortl="es"; fi

		sed ':a;N;$!ba;s/\n//g' $file > $file.clean
		sed -i 's|\r||g' $file.clean
		sed -i 's|<h1 class="wlv-header__title">|\n###<h1 class="wlv-header__title">|g' $file.clean
		sed -i 's|</h1>|\n|g' $file.clean
		sed -i 's|<audio src="https://d1pra95f92lrn3.cloudfront.net/audio/|\n###<audio src="https://d1pra95f92lrn3.cloudfront.net/audio/|g' $file.clean
		sed -i 's|</audio>|\n|g' $file.clean
		sed -i 's|<span class="wlv-item__english js-wlv-english">|\n###<span class="wlv-item__english js-wlv-english">|g' $file.clean
		sed -i 's|</span>|\n|g' $file.clean
		sed -i 's|<span class="wlv-item__word" lang="'$shortl'">|\n###<span class="wlv-item__word" lang="'$shortl'">|g' $file.clean
		sed -i 's|<span class="wlv-item__english" lang="'$shortl'">|\n###<span class="wlv-item__english" lang="'$shortl'">|g' $file.clean
		sed -i 's|<span class="wlv-item__word js-wlv-word" lang="'$shortl'">|\n###<span class="wlv-item__word js-wlv-word" lang="'$shortl'">|g' $file.clean
		sed -i 's|<span lang="'$shortl'">|\n###<span lang="'$shortl'">|g' $file.clean
		sed -i '/^###/!d' $file.clean
		sed -i 's|###<h1 class="wlv-header__title">||g' $file.clean
		sed -i 's|###<audio src="||g' $file.clean
		sed -i 's|" preload="none">||g' $file.clean		
		sed -i 's|###<span class="wlv-item__english" lang="'$shortl'">||g' $file.clean
		sed -i 's|###<span class="wlv-item__english js-wlv-english">||g' $file.clean
		sed -i 's|###<span lang="'$shortl'">||g' $file.clean
		sed -i 's|###<span class="wlv-item__word js-wlv-word" lang="'$shortl'">||g' $file.clean
		sed -i 's|###<span class="wlv-item__word" lang="'$shortl'">||g' $file.clean
		sed -i 's#$#|#g' $file.clean
		sed -i ':a;N;$!ba;s/\n//g' $file.clean
		sed -i 's/https/\nhttps/g' $file.clean
		sed -i 's#|$##g' $file.clean
	done
done