import pdb
import threading
from Crypto.Cipher import AES

def pad(s):
    """
    Stellt sicher dass die Zeichenanzahl durch 16 teilbar ist,
    da AES nur mit dieser Länngenanzahl arbeiten kann
    :param s: Text
    :return: Textergänzung falls Länge nicht durch 16 teilbar
    """
    return s + ((16 - len(s) % 16) * '{')
class Test(threading.Thread):
    """ Threads werden erstellt um eine Nachricht zu verschlüsseln """
    key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18' """ Schlüssel zur Verschlüsselung"""
    cipher = AES.new(key)

    def __init__(self, message):
        """
        Konstruktor
        :param message: die Message
        """
        threading.Thread.__init__(self)
        self.message = message
    def encrypt(plaintext):
        """
        Verschlüsselung
        :return: verschlüsselter Text
        """
        return Test.cipher.encrypt(pad(plaintext))

    def decrypt(ciphertext):
        """
        Entschlüsselung
        :return: entschlüsselter Text
        """
        dec = Test.cipher.decrypt(ciphertext).decode('utf-8')
        l = dec.count('{')
        return dec[:len(dec) - l]

    def run(self):
        """
        run-methode wird überschrieben
        Message wird verschlüsselt und entschlüsselt
        """
        encrypted = Test.encrypt(self.message)
        print("Encrypted:", encrypted)
        decrypted = Test.decrypt(encrypted)


def splitten(message, number):
    """
    Die Message wird in mehrere Teile gesplittet
    :param message: die Message
    :param number:
    :return: Liste mit gesplitteten Text
    """
    k = len(message)
    teil = k / float(number)
    wert = 0.0
    box = []

    while wert < k:
        box.append(message[int(wert): int(wert + teil)])
        wert += teil
    print("Threadanzahl: "+str(number))

    return box

"""
Ausführung
"""
message = input("Message eingeben: ")
threadanzahl = int(input("Threadanzahl eingeben: "))

message_parts = splitten(message,threadanzahl)
threads=[]


for x in range(0,threadanzahl):
    threads.append(Test(message_parts[x]))
    threads[x].start()
print("Decrypted:")
for x in range(0,threadanzahl):
    threads[x].join()
    print (threads[x].message)

