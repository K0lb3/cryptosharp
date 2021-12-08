from cryptosharp.BouncyCastle.rijndael import Rijndael
from cryptosharp.BouncyCastle.padding import ZERO
from cryptosharp.BouncyCastle.mode import CBC
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def test_bouncycastle_aes_cbc():
    data = get_random_bytes(32*10)
    key = get_random_bytes(32)
    iv = get_random_bytes(16)
    
    crypto_enc = AES.new(key, AES.MODE_CBC, iv).encrypt(data)
    cryptography_enc = Rijndael(cipher_mode=CBC, padding=ZERO, block_size=128).encrypt(key, iv, data)
    
    # TODO
    assert(cryptography_enc[:len(crypto_enc)] == crypto_enc)
    
    crypto_dec = AES.new(key, AES.MODE_CBC, iv).decrypt(crypto_enc)
    cryptography_dec = Rijndael(cipher_mode=CBC, padding=ZERO, block_size=128).decrypt(key, iv, cryptography_enc)
    
    # TODO
    assert(cryptography_dec == crypto_dec)

if __name__ == "__main__":
    test_bouncycastle_aes_cbc()