from steem import Steem
from steem.converter import Converter
from steem.account import Account
import time
from datetime import datetime, timedelta
from config import Key

user = Key['steem_2']['user_name']
wif = {
    "active": Key['steem_2']['active_key']
}


def run_delegate():
    s = Steem(keys=wif)
    vests = '{} VESTS'.format(Converter().sp_to_vests(2))
    for u in s.get_vesting_delegations('cnsteem', '', 1000):
        amount, units = u['vesting_shares'].split()
        if float(amount) > 5000:
            res = s.delegate_vesting_shares(u['delegatee'], vests, user)
            print("Done:", u['delegatee'])
            time.sleep(1)


def check_vesting():
    s = Steem(keys=wif)
    date_7_days_ago = str(datetime.now() - timedelta(days=7))
    vests = '{}'.format(Converter().sp_to_vests(2))
    for u in s.get_vesting_delegations('cnsteem', '', 1000):
        acc = Account(u['delegatee'])
        amount, units = acc['vesting_shares'].split()
        if acc['created'] < date_7_days_ago and acc['last_post'] < date_7_days_ago :
            s.delegate_vesting_shares(u['delegatee'], '0 VESTS', user)
            print(u['delegatee'], acc['created'], acc['last_post'])

        if float(amount) > float(vests):
            s.delegate_vesting_shares(u['delegatee'], '0 VESTS', user)
            print(u['delegatee'], float(amount))
