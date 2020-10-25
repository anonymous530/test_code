#!/bin/bash
#find files contains a keyword

#echo -e "\nThis is a script to find all the files in a specified path contains a keyword!"
#
#echo -e "\nPlease input a keyword:"
#read key
#if [ "$key" == "" ]; then
#    echo -e "keyword can not be null!\n"
#    exit 0
#fi
#keyword=$key
keyword="*_gt.json"

echo -e "\nPlease input your specified path:"
read dir
#判断该路径是否存在，并且是目录，不存在输出提示
test ! -d $dir && echo -e "The $dir is not exist in your system.\n\n" && exit 0

echo -e "\n---------------You find files are:---------------\n"

find $dir -type f -name $keyword

echo -e "\n-------------------------------------------------"
echo -e "\nFind Finished!\n"
