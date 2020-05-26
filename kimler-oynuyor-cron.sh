#!/bin/sh

bash ~/hunlar/lsgreptail.sh > ~/hunlar/kimler-oynuyor-cron.tmp
cmp --silent ~/hunlar/kimler-oynuyor-cron.tmp ~/hunlar/kimler-oynuyor-simdi.tmp || {
 echo "" > ~/hunlar/kimler-oynuyor-simdi.txt
 grep -qn round00 /root/hunlar/kimler-oynuyor-cron.tmp && echo "~~~yeni~oyun~~~" >> ~/hunlar/kimler-oynuyor-simdi.txt
 grep -qn round01 /root/hunlar/kimler-oynuyor-cron.tmp && echo "~~~yeni~oyun~~~" >> ~/hunlar/kimler-oynuyor-simdi.txt
 cat ~/hunlar/kimler-oynuyor-cron.tmp >> ~/hunlar/kimler-oynuyor-simdi.txt
 cat ~/hunlar/kimler-oynuyor-simdi.tmp >> ~/hunlar/kimler-oynuyor-simdi.txt
 bash ~/hunlar/kimler-oynuyor-simdi.sh >> ~/hunlar/kimler-oynuyor-simdi.txt
 for i in {1..2}; do echo " " >> ~/hunlar/kimler-oynuyor-simdi.txt; done
 cat ~/hunlar/kimler-oynuyor-simdi.txt >> ~/hunlar/kimler-oynuyor-log.txt
 python3 ~/hunlar/telegram_send.py
}
