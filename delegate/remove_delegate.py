from steem import Steem
from steem.converter import Converter
import time
from config import Key

user = Key['steem_2']['user_name']
wif = {
    "active": Key['steem_2']['active_key']
}

s = Steem(keys = wif)
# TODO check accounts post
vests = '{} VESTS'.format(Converter().sp_to_vests(2))
for u in s.get_vesting_delegations('cnsteem', '', 1000):
    amount, units = u['vesting_shares'].split()
    if float(amount) > 5000:
        res = s.delegate_vesting_shares(u['delegatee'], vests, user)
        print("Done:", u['delegatee'])
        time.sleep(1)

