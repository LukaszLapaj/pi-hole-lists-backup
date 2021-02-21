#!/bin/bash
set -e

git add .
git commit -m "Blocklist update `date`"
git push