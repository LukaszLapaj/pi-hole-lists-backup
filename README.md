# Pi-hole-lists-backup
Simple script to backup Pi-hole blacklist and keep up with changes.

## Background
Many of the great Pi-hole blocklists randomly disappeared in the past from mirrors and were lost irrevocably.
This is a simple solution to back up them and save them from being gone.
Also, this allows to track recent changes in the lists.


## Usage
1. Go to Pi-hole admin panel
2. Go to settings and `Teleporter` tab
3. Create backup
4. Extract `adlist.json` form archive
5. Fork this repository to save backups on Github
6. Put `adlist.json` in forked and cloned repository
7. Run `commit.sh` manually
8. Schedule it with cron to run as frequently as You want