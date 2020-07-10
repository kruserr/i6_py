import string
import secrets


class crypto():
    """
        Class for standardized cryptography tools.

        Example:
        ```
        i6.crypto.password()
        ```
    """

    def password(length = 32):
        """
            Generate a random password

            Example:
            ```
            i6.crypto.password()
            ```
        """

        if (length < 8) or (not isinstance(length, int)):
            raise ValueError('Password length must be larger than 8')

        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 3):
                break
        
        return password
        