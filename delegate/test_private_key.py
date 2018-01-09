from steembase.account import PasswordKey

account = 'test'
password = 'test'


key_types = [
    'owner',
    'posting'
]

for key_type in key_types:
    private_key = PasswordKey(account, password, key_type).get_private_key()
    public_key = private_key.pubkey
    print(str(private_key))
    print(str(public_key))





