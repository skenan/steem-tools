# steem-tools

## Installation

Update Ubuntu

```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev python3-dev

```
Have to use python >= 3.5

```
pip3 install steem
pip3 install sendgrid
```

## Set Steem Node
 ```
 steempy set nodes https://gtg.steem.house:8090/,https://steemd.steemit.com
 ```

## Config

Rename the config_template.py to config.py  
Replace with your own username and posting key in config.py


## Cron Job

Run the script every 30 minutes
```
*/30 * * * * python3 ~/steem-tools/claim/auto_claim.py
```


## Notice

If you have the following error:

```

from funcy.simple_funcs import rpartial
ImportError: No module named 'funcy.simple_funcs'

```

do

```
pip3 install funcy==1.8
```