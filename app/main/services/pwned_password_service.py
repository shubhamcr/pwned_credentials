import requests
import hashlib


class PwnedPasswordService:
    def __init__(self, password):
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
