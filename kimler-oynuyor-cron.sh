#!/bin/sh

bash ~/hunlar/lsgreptail.sh > ~/hunlar/kimler-oynuyor-cron.tmp
cmp --silent ~/hunlar/kimler-oynuyor-cron.tmp ~/hunlar/kimler-oynuyor-simdi.tmp || {
 cat ~/hunlar/kimler-oynuyor-cron.tmp > ~/hunlar/kimler-oynuyor-simdi.txt
 cat ~/hunlar/kimler-oynuyor-simdi.tmp >> ~/hunlar/kimler-oynuyor-simdi.txt
 bash ~/hunlar/kimler-oynuyor-simdi.sh >> ~/hunlar/kimler-oynuyor-simdi.txt
 for i in {1..3}; do echo " " >> ~/hunlar/kimler-oynuyor-simdi.txt; done
}
