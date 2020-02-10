from steem import Steem
from steem.account import Account
from tools import logging_tool
from config import Key

logger = logging_tool.setup_logger('claim_vests', 'claim_vests.log')


def run_claim(steem_user):
    username = steem_user['username']
    wif = {
        "posting": steem_user['posting_key']
    }
    try:
        account = Account(username)
        steem = Steem(keys=wif)
        sbd = account.balances["rewards"]["SBD"]
        st = account.balances["rewards"]["STEEM"]
        vests = account.balances["rewards"]["VESTS"]

        if sbd > 0 or st > 0 or vests > 0:
            logger.info(f'{username} Claiming rewards ... ')
            steem.claim_reward_balance(account=username)
        else:
            logger.info(f'{username} Nothing to claim')
    except Exception as e:
        logger.warning(f'{username} Oops, something not right.' + str(e))


if __name__ == '__main__':
    for steem_user in Key['steem_accounts']:
        run_claim(steem_user)
