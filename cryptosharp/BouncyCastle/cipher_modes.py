from ._shared import load_bouncy_castle

load_bouncy_castle()


from Org.BouncyCastle.Crypto.Modes import (
    CbcBlockCipher,
    CcmBlockCipher,
    CfbBlockCipher,
    ChaCha20Poly1305,
    CtsBlockCipher,
    EaxBlockCipher,
    GcmBlockCipher,
    GcmSivBlockCipher,
    GOfbBlockCipher,
    KCcmBlockCipher,
    KCtrBlockCipher,
)


CBC = CbcBlockCipher
CCM = CcmBlockCipher
CFB = CfbBlockCipher
CTS = CtsBlockCipher
EAX = EaxBlockCipher
GCM = GcmBlockCipher
GCMSiv = GcmSivBlockCipher
GOFB = GOfbBlockCipher
KCCM = KCcmBlockCipher
KCTR = KCtrBlockCipher
ChaCha20Poly1305 = ChaCha20Poly1305


