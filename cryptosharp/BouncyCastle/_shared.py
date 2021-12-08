import os
import clr

# due to the default settings of net framework,
# assemblies from other computers are not trusted
# and have to be either unblocked by hand or loaded via UnsafeLoadFrom
global BOUNCY_CASTLE_PATH
BOUNCY_CASTLE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "BouncyCastle.Crypto.dll")

BOUNCY_CASLTE_LOADED = False
def load_bouncy_castle():
    if not BOUNCY_CASLTE_LOADED:
        from System.Reflection import Assembly
        assembly = Assembly.UnsafeLoadFrom(BOUNCY_CASTLE_PATH)