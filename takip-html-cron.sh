#!/bin/sh

bash ~/hunlar/lsgreptail.sh > ~/hunlar/takip-html-cron.tmp

cmp --silent ~/hunlar/takip-html-cron.tmp ~/hunlar/takip-html-simdi.tmp || {
 bash ~/hunlar/lsgreptail.sh > ~/hunlar/takip-html-simdi.tmp
 echo "<html> <head> <meta http-equiv='refresh' content='5' /> <title>Hunlar vs Gokturkler</title> </head><body><pre>";
 echo "---------------------------------------------------------------------------";
 date;
 echo "---------------------------------------------------------------------------";
 /usr/local/bin/python3.8 ~/hunlar/hunlar.py;
 echo "===========================================================================";
  cat ~/hunlar/takip-html-cron.tmp;
  cat ~/hunlar/takip-html-simdi.tmp;
 echo "</pre></body></html>"; 
#} > /var/www/html/hunlar.html 
} > /usr/local/apache/htdocs/hunlar.html 
