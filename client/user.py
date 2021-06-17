import binascii
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:
    """Client class that contains the public- and the private key of the instance.
    
    Example:
        Instantiating the class by Object = Client() and 
        then calling Object.identity returns the public key.
    """
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def public_key(self) -> str:
        """Returns the public key.

        Returns:
            public_key[str]: a hexadecimal number. 
        """
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


class User:
    """A user with a unique id, a name, and a balance containing currency.
    
    -- TODO: add extra info here --
    
    Attributes:
        id: a unique key id for specifying the user
        name: the name of the user
        balance: a value describing the currency available to the user
    """ 
    def __init__(self, 
                 id: int, 
                 name: str, 
                 balance: float):
        self.id = id
        self.name = name
        self.balance = balance
    
    @property
    def balance(self):
        return self.balance
    
    @balance.setter
    def receive_value(self, n_currency_received: float):
        """Updates the balance after receiving n currency"""
        return self._set_balance(n_currency_received)
    
    @balance.setter
    def send_value(self, n_currency_sent: float):
        """Updates the balance after sending n currency"""
        return self._set_balance(n_currency_sent)
    
    def _set_balance(self, value: float):
        """Indirect setter to calculate the new balance"""
        return (self.balance + value)