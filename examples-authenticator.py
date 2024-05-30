from abc import ABC, abstractmethod


class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, username, password):
        pass


class SimpleAuthenticator(Authenticator):
    def authenticate(self, username, password):
        return username == "admin" and password == "!Password123"


class SecureAuthenticator(Authenticator):

    def authenticate(self, username, password):
        stored_password_hash = self.get_stored_password_hash(username)
        pwd_pass = self.verify_password(password, stored_password_hash)
        return username == "admin" and pwd_pass

    def get_stored_password_hash(self, username):
        return "hashed_password"

    def hash_password(self, username):
        return "hashed_password"

    def verify_password(self, password, stored_password_hash):
        pwd = self.hash_password(password)
        return pwd == stored_password_hash

auth1 = SimpleAuthenticator()
print(auth1.authenticate("admin", "!Password123"))

auth2 = SecureAuthenticator()
print(auth2.authenticate("test", "test"))

auth2 = SecureAuthenticator()
print(auth2.authenticate("admin", "test"))
