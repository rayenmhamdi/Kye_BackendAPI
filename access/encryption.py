import uuid
import json
from cryptography.fernet import Fernet

def get_mac():
    return ''.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])


def string_to_bytes(text):
    return text[2:text.__len__() - 1].encode('utf8')


def encrypt(text, bkey):
    try:
        f = Fernet(bkey)
        return f.encrypt(text.encode('utf8'))
    except Exception as e:
        return str(e)


def decrypt(text, key):
    try:
        f = Fernet(key)
        return f.decrypt(text).decode('utf8')
    except :
        return ''


def get_module_validity(module, plain_licence):
    # plainlicence format <MODULENAME>_X
    # X can be 1 or 0
    if plain_licence != '':
        licence = plain_licence.replace(module.upper(), '')
        if licence == '_1':
            return True
        else:
            return False
    else:
        return False


def empty_licence():
    return {
            "valid": False,
            "custmng": False,
            "prvdmng": False,
            "prodmng": False,
            "mantmng": False,
            "muluser": False,
            "statrpt": False
        }

def request_licence():
    # this function need an internet connection to work
    # this method used when the owner request a valid licence
    # send us the store data
    # mac address
    # we will save a fixture file that need to be fed to the database to fill the table
    pass

def get_licence():
    # this function need an internet connection to work
    # after requesting a licence the request is registered in our database
    # we need to accept it manually
    # if the licence is accepted this function will get the data from us to fill the licence table
    pass

def update_module_licence():
    # he must contact us to
    # 1.prolong the period of a module
    # 2.activate another module
    # this function will get the licence of this module from us directly
    pass





def generate_full_licence():
    license = {
        "encryption_key" : "",
        "basic_key": "",
        "custmng": "",
        "prvdmng": "",
        "prodmng": "",
        "mantmng": "",
        "mulstor": "",
        "muluser": "",
        "statrpt": ""
    }

    key = Fernet.generate_key()
    license["encryption_key"] = str(key)
    license["basic_key"] = str(encrypt(get_mac(), key))
    license["custmng"] = str(encrypt("CUSTMNG_1", key))
    license["prvdmng"] = str(encrypt("PRVDMNG_1", key))
    license["prodmng"] = str(encrypt("PRODMNG_1", key))
    license["mantmng"] = str(encrypt("MANTMNG_1", key))
    license["mulstor"] = str(encrypt("MULSTOR_1", key))
    license["muluser"] = str(encrypt("MULUSER_1", key))
    license["statrpt"] = str(encrypt("STATRPT_1", key))
    print(license)
    with open('licence.json', 'w') as fp:
        json.dump(license, fp)