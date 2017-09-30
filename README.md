# steem-tools

## Installation

Have to use python >= 3.5

```
pip3 install steem
```

## Config

Replace with your own username and posting key in config.py


## Cron Job

Run the script every 30 minutes
```
*/30 * * * * python3 ~/steem-tools/auto_claim.py
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