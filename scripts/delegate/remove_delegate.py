from steem import Steem
from steem.converter import Converter
from steem.account import Account
from datetime import datetime, timedelta
from config import Key


def check_vesting(steem_user):
    username = steem_user['username']
    wif = {
        "active": steem_user['active_key']
    }

    s = Steem(keys=wif)
    date_7_days_ago = str(datetime.now() - timedelta(days=7))
    vests = '{}'.format(Converter().sp_to_vests(2))
    for u in s.get_vesting_delegations(username, '', 1000):
        acc = Account(u['delegatee'])
        amount, units = acc['vesting_shares'].split()
        if acc['created'] < date_7_days_ago and acc['last_post'] < date_7_days_ago:
            s.delegate_vesting_shares(u['delegatee'], '0 VESTS', username)
            print(u['delegatee'], acc['created'], acc['last_post'])

        if float(amount) > float(vests):
            s.delegate_vesting_shares(u['delegatee'], '0 VESTS', username)
            print(u['delegatee'], float(amount))


if __name__ == '__main__':
    for steem_user in Key['steem_accounts']:
        check_vesting(steem_user)
