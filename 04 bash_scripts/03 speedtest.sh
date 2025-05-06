#!/bin/bash

echo "Enter tests count"
read tests_count
printf 'Iteration,Download,Upload\n' > stats.csv
max_download=0
max_upload=0
for i in $(seq 1 $tests_count);
do
    speedtest > speed.txt
    cat speed.txt | grep -P ".+load.+"
    download=$(cat speed.txt | grep "Download" | tr -s ' ' | cut -d ' ' -f 3)
    if [ $download > $max_download ]; then 
        max_download=$download
    fi
    upload=$(cat speed.txt | grep "Upload" | tr -s ' ' | cut -d ' ' -f 3)
    if [ $upload > $max_upload ]; then
        max_upload=$upload
    fi
    printf "$i,$download,$upload\n" >> stats.csv
done
printf "Peak speeds:\nUpload: $max_upload\nDownload: $max_download\n"
