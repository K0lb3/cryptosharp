from cryptosharp.Cryptography.rijndael import Rijndael, CipherMode, PaddingMode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def test_cryptography_aes_cbc():
    data = get_random_bytes(32*10)
    key = get_random_bytes(32)
    iv = get_random_bytes(16)
    
    crypto_enc = AES.new(key, AES.MODE_CBC, iv).encrypt(data)
    cryptography_enc = Rijndael(key = key, iv = iv, mode=CipherMode.CBC, padding=PaddingMode.Zeros).encrypt(data)
    
    assert(cryptography_enc == crypto_enc)
    
    crypto_dec = AES.new(key, AES.MODE_CBC, iv).decrypt(crypto_enc)
    cryptography_dec = Rijndael(key = key, iv = iv, mode=CipherMode.CBC, padding=PaddingMode.Zeros).decrypt(cryptography_enc)
    
    assert(cryptography_dec == crypto_dec)

if __name__ == "__main__":
    test_cryptography_aes_cbc()