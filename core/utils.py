import hashlib
import math


def encrypt_user_password(password: str) -> str:
    encrypt_password = hashlib.sha256(password.encode()).hexdigest()
    return encrypt_password


def adapter_records_info(objs, pageSize):
    total = len(objs)
    pages = math.ceil(total / pageSize)
    size = pageSize
    return {"pages": pages, "total": total, "size": size}
