from typing import Union
from enum import IntEnum

# import clr to enable C# imports via pythonnet
import clr

# import the C# library components
from System.IO import MemoryStream
from System.Security.Cryptography import (
    Rijndael as CS_Rijndael,
    CryptoStream,
    CryptoStreamMode,
    RijndaelManaged,
)

# rename both modes so that we can mask them with Python Enums
from System.Security.Cryptography import (
    PaddingMode as CS_PaddingMode,
    CipherMode as CS_CipherMode,
)


class PaddingMode(IntEnum):
    ANSIX923 = 4  # The ANSIX923 padding string consists of a sequence of bytes filled with zeros before the length.
    ISO10126 = (
        5  # The ISO10126 padding string consists of random data before the length.
    )
    NONE = 1  # No padding is done.
    PKCS7 = 2  # The PKCS #7 padding string consists of a sequence of bytes, each of which is equal to the total number of padding bytes added.
    Zeros = 3  # The padding string consists of bytes set to zero.


class CipherMode(IntEnum):
    CBC = 1
    CFB = 4
    CTS = 5
    ECB = 2
    OFB = 3


class Rijndael(object):
    def __init__(
        self,
        rijndael: CS_Rijndael = None,
        mode: CipherMode = CipherMode.CBC,
        padding: PaddingMode = PaddingMode.PKCS7,
        key: Union[bytes, bytearray] = None,
        iv: Union[bytes, bytearray] = None,
        block_size: int = 128,
    ) -> None:
        super().__init__()
        if not rijndael:
            self.myRijndael = CS_Rijndael.Create()
        else:
            self.myRijndael = rijndael

        self.mode = mode
        self.padding = padding
        self.block_size = block_size
        if key:
            self.key = key
        else:
            self.generate_key()
        if iv:
            self.iv = iv
        else:
            self.generate_iv()

    @property
    def block_size(self):
        """Gets or sets the block size, in bits, of the cryptographic operation."""
        return self.myRijndael.BlockSize

    @block_size.setter
    def block_size(self, value: int):
        """Gets or sets the block size, in bits, of the cryptographic operation."""
        self.myRijndael.BlockSize = value

    @property
    def feedback_size(self):
        """Gets or sets the feedback size, in bits, of the cryptographic operation for the Cipher Feedback (CFB) and Output Feedback (OFB) cipher modes."""
        return self.myRijndael.FeedbackSize

    @feedback_size.setter
    def feedback_size(self, value: int):
        """Gets or sets the feedback size, in bits, of the cryptographic operation for the Cipher Feedback (CFB) and Output Feedback (OFB) cipher modes."""
        self.myRijndael.FeedbackSize = value

    @property
    def iv(self):
        """Gets or sets the initialization vector (IV) for the symmetric algorithm."""
        return bytes(self.myRijndael.IV)

    @iv.setter
    def iv(self, value: Union[bytes, bytearray]):
        """Gets or sets the initialization vector (IV) for the symmetric algorithm."""
        self.myRijndael.IV = value

    @property
    def key(self):
        """Gets or sets the secret key for the symmetric algorithm."""
        return bytes(self.myRijndael.Key)

    @key.setter
    def key(self, value: Union[bytes, bytearray]):
        """Gets or sets the secret key for the symmetric algorithm."""
        self.myRijndael.Key = value

    @property
    def key_size(self):
        """Gets or sets the size, in bits, of the secret key used by the symmetric algorithm."""
        return self.myRijndael.KeySize

    @key_size.setter
    def key_size(self, value):
        """Gets or sets the size, in bits, of the secret key used by the symmetric algorithm."""
        self.myRijndael.KeySize = value

    @property
    def legal_block_sizes(self):
        """Gets the block sizes, in bits, that are supported by the symmetric algorithm."""
        return self.myRijndael.LegalBlockSizes

    @legal_block_sizes.setter
    def legal_block_sizes(self, value):
        """Gets the block sizes, in bits, that are supported by the symmetric algorithm."""
        self.myRijndael.LegalBlockSizes = value

    @property
    def legal_key_sizes(self):
        """Gets the key sizes, in bits, that are supported by the symmetric algorithm."""
        return self.myRijndael.LegalKeySizes

    @legal_key_sizes.setter
    def legal_key_sizes(self, value):
        """Gets the key sizes, in bits, that are supported by the symmetric algorithm."""
        self.myRijndael.LegalKeySizes = value

    @property
    def mode(self) -> CipherMode:
        """Gets or sets the mode for operation of the symmetric algorithm."""
        return CipherMode(self.myRijndael.Mode)

    @mode.setter
    def mode(self, value: Union[int, CipherMode]):
        """Gets or sets the mode for operation of the symmetric algorithm."""
        self.myRijndael.Mode = CS_CipherMode(value)

    @property
    def padding(self) -> PaddingMode:
        """Gets or sets the padding mode used in the symmetric algorithm."""
        return PaddingMode(self.myRijndael.padding)

    @padding.setter
    def padding(self, value: Union[int, PaddingMode]):
        """Gets or sets the padding mode used in the symmetric algorithm."""
        self.myRijndael.Padding = CS_PaddingMode(value)

    def clear(self):
        """Releases all resources used by the SymmetricAlgorithm class."""
        return self.myRijndael.Clear()

    def dispose(self, release_manged_resources: bool = False):
        """Releases all resources used by the current instance of the SymmetricAlgorithm class."""
        """Releases the unmanaged resources used by the SymmetricAlgorithm and optionally releases the managed resources."""
        return self.myRijndael.Dispose(release_manged_resources)

    def __eq__(self, Object):
        """Determines whether the specified object is equal to the current object."""
        return self.myRijndael.Equals(Object)

    def generate_iv(self):
        """When overridden in a derived class, generates a random initialization vector (IV) to use for the algorithm."""
        return self.myRijndael.GenerateIV()

    def generate_key(self):
        """When overridden in a derived class, generates a random key (Key) to use for the algorithm."""
        return self.myRijndael.GenerateKey()

    def __hash__(self):
        """Serves as the default hash function."""
        return self.myRijndael.GetHashCode()

    def __type__(self):
        """Gets the Type of the current instance."""
        return self.myRijndael.GetType()

    def memberwise_clone(self):
        """Creates a shallow copy of the current Object."""
        return self.myRijndael.MemberwiseClone()

    def __str__(self):
        """Returns a string that represents the current object."""
        return self.myRijndael.ToString()

    def valid_key_size(self, size: int):
        """Determines whether the specified key size is valid for the current algorithm."""
        return self.myRijndael.ValidKeySize(size)

    def decrypt(self, cipherdata: Union[bytes, bytearray]) -> bytes:
        """Decrypts the cipherdata and returns the plaindata."""
        alg = self.myRijndael

        # Create a MemoryStream that is going to accept the
        # decrypted bytes
        ms = MemoryStream()

        # Create a CryptoStream through which we are going to be
        # pumping our data.
        # CryptoStreamMode.Write means that we are going to be
        # writing data to the stream
        # and the output will be written in the MemoryStream
        # we have provided.
        cs = CryptoStream(ms, alg.CreateDecryptor(), CryptoStreamMode.Write)

        # Write the data and make it do the decryption
        cs.Write(cipherdata, 0, len(cipherdata))

        # Close the crypto stream (or do FlushFinalBlock).
        # This will tell it that we have done our decryption
        # and there is no more data coming in,
        # and it is now a good time to remove the padding
        # and finalize the decryption process.
        cs.Close()

        # Now get the decrypted data from the MemoryStream.
        # Some people make a mistake of using GetBuffer() here,
        # which is not the right way.
        decryptedData = ms.ToArray()

        return bytes(decryptedData)

    def encrypt(self, plaindata: Union[bytes, bytearray]) -> bytes:
        """Encrypts the plaindata and returns the cipherdata."""
        alg = self.myRijndael

        # Create a MemoryStream that is going to accept the
        # decrypted bytes
        ms = MemoryStream()

        # Create a CryptoStream through which we are going to be
        # pumping our data.
        # CryptoStreamMode.Write means that we are going to be
        # writing data to the stream
        # and the output will be written in the MemoryStream
        # we have provided.
        cs = CryptoStream(ms, alg.CreateEncryptor(), CryptoStreamMode.Write)

        # Write the data and make it do the decryption
        cs.Write(plaindata, 0, len(plaindata))

        # Close the crypto stream (or do FlushFinalBlock).
        # This will tell it that we have done our encryption
        # and there is no more data coming in,
        # and it is now a good time to remove the padding
        # and finalize the decryption process.
        cs.Close()

        # Now get the encrypted data from the MemoryStream.
        # Some people make a mistake of using GetBuffer() here,
        # which is not the right way.
        encryptedData = ms.ToArray()

        return bytes(encryptedData)
