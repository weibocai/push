# coding=utf-8
import hashlib


class SignUtil:
    def __init__(self, app_id, app_key, app_secret):
        self.app_id = app_id
        self.app_key = app_key
        self.app_secret = app_secret

    def sign_util(self, timestamp):
        m = hashlib.md5()
        m.update(self.app_id.encode("UTF-8"))
        m.update(self.app_key.encode("UTF-8"))
        m.update(str(timestamp).encode("UTF-8"))
        m.update(self.app_secret.encode("UTF-8"))
        return m.hexdigest()
