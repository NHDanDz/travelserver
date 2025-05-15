import hashlib

def md5(s, salt=''):
    """
    MD5 encryption
    """
    m = hashlib.md5()
    s = s + salt
    m.update(s.encode('utf-8'))
    return m.hexdigest()