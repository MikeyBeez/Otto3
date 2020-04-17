#!/bin/sh
for i in `ls`
do
	cd $i && ls >> ~/mymusiclist.txt && cd ..
done

