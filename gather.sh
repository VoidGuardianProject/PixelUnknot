#!/bin/bash

if [ -z "$3" ]; then
  usage "$0 domain board threadid"
  exit
fi

# Which chan forum / board to scrape
DOMAIN=$1
BOARD=$2
THREAD=$3

# URL variable
URL=https://boards.$DOMAIN/$BOARD/thread/$THREAD
# Images
IMGS=is2.$DOMAIN

# Get those images
wget -P $THREAD -nd -np -r -l 1 -e robots=off -H -D $IMGS -A jpg,jpeg $URL

# loop over them and run the python detect.py file
for F in $THREAD/*.jp*g;
    do python detect.py $F;
done
