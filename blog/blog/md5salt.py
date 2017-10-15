from hashlib import md5



def create_md5(pwd, salt):
    md5_obj = md5()
    md5_obj.update(pwd + salt)
    return md5_obj.hexdigest()


# salt = "Ecm6"

