#!/bin/sh

#\ place\ this\ script\ in\ ~/bin
#\ you\ must\ use\ the\ correct\ path\ to\ the\ python\ in\ whatever\ virtual\ 
#\ environment\ you\ built\ this\ project\ in,\ and\ point\ the\ right\ path\ 
#\ to\ otto3.py
#\ chmod\ +x\ ~/bin/otto.sh
#\ put\ 
#\ alias\ otto="~/bin/otto.sh"
/home/bard/miniconda3/envs/Otto/bin/python\ /home/bard/Code/Otto3/Otto3.py\ 2>/dev/null
#\ \ then\ you\ can\ type\ otto\ &\ to\ start\ otto\ in\ the\ background
