from ._shared import load_bouncy_castle

load_bouncy_castle()

from Org.BouncyCastle.Crypto.Engines import RijndaelEngine
from Org.BouncyCastle.Crypto.Modes import CbcBlockCipher, PaddedBlockCipher
from Org.BouncyCastle.Crypto.Paddings import Pkcs7Padding
from Org.BouncyCastle.Crypto.Parameters import KeyParameter, ParametersWithIV

import Org.BouncyCastle.Crypto.Modes
import Org.BouncyCastle.Crypto.Paddings


class Rijndael:
    engine: RijndaelEngine
    cipher_mode: Org.BouncyCastle.Crypto.Modes
    padding: Org.BouncyCastle.Crypto.Paddings

    def __init__(
        self,
        cipher_mode: Org.BouncyCastle.Crypto.Modes = CbcBlockCipher,
        padding: Org.BouncyCastle.Crypto.Paddings = Pkcs7Padding,
        block_size=256,
    ) -> None:
        """Creates a wrapper around the Bouncy Castle Rijndael engine.

        Args:
            cipher_mode (Org.BouncyCastle.Crypto.Modes, optional): A block cipher mode from Org.BouncyCastle.Crypto.Modes. Defaults to CbcBlockCipher.
            padding (Org.BouncyCastle.Crypto.Paddings, optional): A padding from Org.BouncyCastle.Crypto.Paddings. Defaults to Pkcs7Padding.
            block_size (int, optional): The block size for the Rijndael algorithm. Defaults to 256.
        """
        self.engine = RijndaelEngine(block_size)
        self.cipher_mode = cipher_mode
        self.padding = padding

    def decrypt(self, key: bytes, iv: bytes, data: bytes) -> bytes:
        cipher = PaddedBlockCipher(self.cipher_mode(self.engine), self.padding())
        cipher.Init(False, ParametersWithIV(KeyParameter(key), iv))
        return bytes(cipher.DoFinal(data))

    def encrypt(self, key: bytes, iv: bytes, data: bytes) -> bytes:
        cipher = PaddedBlockCipher(self.cipher_mode(self.engine), self.padding())
        cipher.Init(True, ParametersWithIV(KeyParameter(key), iv))
        return bytes(cipher.DoFinal(data))
