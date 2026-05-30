try:
    import webview
except ImportError:
    webview = None

import secrets
import string

class Apibackend:
    def generativePassword(self, length, use_uppercase, use_numbers, use_symbols):
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    def require_webview(self):
        if webview is None:
            raise ImportError(
                "La librería 'pywebview' no está instalada. Instale con: python -m pip install pywebview"
            )
        return webview