from base64 import b64encode, b64decode

import pysodium
from mnemonic import Mnemonic


def generate_key_pair(seed_phrase):
    mnemo = Mnemonic("english")
    entropy = mnemo.to_entropy(seed_phrase)
    return pysodium.crypto_sign_seed_keypair(bytes(entropy))


def get_ed_pk_in_curve(public_key):
    signingKey = pysodium.crypto_sign_pk_to_box_pk(public_key)
    return b64encode(signingKey)


def decrypt(ecryptedMessage, nonce, private_key, pub_key):
    new_private_key = pysodium.crypto_sign_sk_to_box_sk(private_key)
    new_pub_key = pysodium.crypto_sign_pk_to_box_pk(pub_key)
    return pysodium.crypto_box_open(
        b64decode(ecryptedMessage),
        b64decode(nonce),
        new_pub_key,
        new_private_key
    ).decode("utf-8")