#!/bin/bash
set -e

git pull
git add .
git commit -m "Blocklist update `date`"
git push
