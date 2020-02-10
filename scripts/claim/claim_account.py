from config import Key
from beem import Steem
from beem.rc import RC
from beem.account import Account
from tools import logging_tool

logger = logging_tool.setup_logger('claim_accounts', 'claim_accounts.log')


def claim_account(keys, account_name):
    steem_tool = Steem(keys=keys)
    rc = RC(steem_instance=steem_tool)
    claim_account_rc = rc.claim_account()
    creator = Account(account_name)
    current_rc = creator.get_rc_manabar()["current_mana"]
    num = current_rc - claim_account_rc
    while num > 100000000000:
        try:
            steem_tool.claim_account(account_name)
            logger.info("Claimed account for %s" % account_name)
        except Exception as e:
            logger.warning(f'{account_name} Oops, something not right.' + str(e))

    logger.info("Can not claimed account for %s" % account_name)


if __name__ == '__main__':
    for username in Key['beem_accounts']['username']:
        claim_account(Key['beem_accounts']['keys'], username)
