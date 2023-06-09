#!/bin/bash

### Path to your config folder you want to backup
config_folder=~/printer_data/config

### The branch of the repository that you want to save your config
### By default that is 'master'
branch=main

# To fully automate this and not have to deal with auth issues, generate a legacy token on Github
# then update the command below to use the token. Run the command in your base directory and it will
# handle auth. This should just be executed in your shell and not committed to any files or
# Github will revoke the token. =)
# git remote set-url origin https://XXXXXXXXXXX@github.com/EricZimmerman/Voron24Configs.git/
# Note that that format is for changing things after the repository is in use, vs initially

push_config(){
  cd $config_folder

  mkdir -p backup_configs
  mv printer[0-9]*-* backup_configs
  mv *.moonraker.conf.bkp backup_configs 

  git pull origin $branch
  git add .
  current_date=$(date +"%Y-%m-%d %T")
  git commit -m "Autocommit from $current_date" -m "$m1" -m "$m2" -m "$m3" -m "$m4"
  git push origin $branch
}

push_config


