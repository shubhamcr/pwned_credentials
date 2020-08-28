import requests
import hashlib
import re


class PwnedPasswordService:
    def __init__(self, password):
        self.password = password
        self.sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    def pwned_count(self):
        head, tail = self.sha1password[:5], self.sha1password[5:]
        response = requests.get("https://api.pwnedpasswords.com/range/" + head)
        if response.status_code != 200:
            return -1
        hashes = (line.split(":") for line in response.text.splitlines())
        for h, cnt in hashes:
            if h == tail:
                return int(cnt)
        return 0

    def check_password_strength(self):
        result = []
        if len(self.password) < 8:
            result.append("Password length is short. Password length must be atleast 8 characters.")
        if not re.search(r"[A-Z]", self.password):
            result.append("Password must contain an uppercase alphabet.")
        if not re.search(r"[a-z]", self.password):
            result.append("Password must contain a lowercase alphabet.")
        if not re.search(r"\d", self.password):
            result.append("Password must contain a digit.")
        if not re.search(r"\W", self.password):
            result.append("Password must contain a special character like $,#,@ etc.")
        return result
