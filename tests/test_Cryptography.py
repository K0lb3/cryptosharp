from cryptosharp.Cryptography.rijndael import Rijndael, CipherMode, PaddingMode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def test_cryptography_aes_cbc():
    data = get_random_bytes(32*10)
    key = get_random_bytes(32)
    iv = get_random_bytes(16)
    
    crypto_cipher = AES.new(key, AES.MODE_CBC, iv)
    cryptography_cipher = Rijndael(key = key, iv = iv, mode=CipherMode.CBC, padding=PaddingMode.Zeros)
    
    crypto_enc = crypto_cipher.encrypt(data)
    cryptography_enc = cryptography_cipher.encrypt(data)
    
    assert(cryptography_enc == crypto_enc)
    
    crypto_dec = crypto_cipher.decrypt(crypto_enc)
    cryptography_dec = cryptography_cipher.decrypt(cryptography_enc)
    
    assert(cryptography_dec == crypto_dec)
    
    # prevent segault on macOS
    cryptography_cipher.dispose(True)

if __name__ == "__main__":
    test_cryptography_aes_cbc()