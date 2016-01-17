#!/bin/bash
export DISPLAY=:0.0

if [ $# -eq 0 ]; then
  echo usage: $(basename $0) "on|off|status"
  exit 1
fi

if [ $1 = "off" ]; then
  echo -en "Turning monitor off..."
  #xset dpms force off
  tvservice -o

  echo -en "done.\nCheck:"
  xset -q|grep "Monitor is"
  tvservice -s

elif [ $1 = "on" ]; then
  echo -en "Turning monitor on..."
  tvservice --preferred > /dev/null

  #xset dpms force on
  fbset -depth 8; fbset -depth 32; xrefresh
  echo -en "done.\nCheck:"
  xset -q|grep "Monitor is"
  tvservice -s

elif [ $1 = "status" ]; then
  xset -q|sed -ne 's/^[ ]*Monitor is //p'
  tvservice -s
else
  echo usage: $(basename $0) "on|off|status"
fi - See more at: https://systembash.com/how-to-turn-off-your-monitor-via-command-line-in-ubuntu/#sthash.wyLNwV8L.dpuf