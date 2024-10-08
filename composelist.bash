#!/bin/bash

StartDir=`pwd`
DirList=`ls -d apps/*/`
#echo $DirList

for thisdir in $DirList
do
  cd $thisdir
  if [ -f docker-compose.yml ]
  then
        pwd >> $StartDir/AppsList.txt

        docker-compose ps >> $StartDir/AppsList.txt
  fi
  echo '##############################################################' >> $StartDir/AppsList.txt
  cd $StartDir
  #echo 'In progress'
done

echo 'done'
