#!/bin/bash

while true; do
  sleep 300  # Wait 5 minutes

  # Check if there are any changes (unstaged or staged)
  if git status --porcelain | grep . > /dev/null; then
    timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    commit_message="${1:-Auto commit at $timestamp}"

    git add .

    git commit -m "$commit_message" 2>/dev/null

    git push

    echo "Pushed: $commit_message"
  else
    echo "No changes to commit at $(date)."
  fi
done
