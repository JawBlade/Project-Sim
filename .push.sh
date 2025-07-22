#!/bin/bash

while true; do
  timestamp=$(date "+%Y-%m-%d %H:%M:%S")

  git add .

  git commit -m "Auto commit at $timestamp" 2>/dev/null

  git push

  echo "Pushed at $timestamp. Next in 5 minutes..."
  sleep 300
done
