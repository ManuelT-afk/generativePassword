try:
    import webview
except ImportError:
    webview = None

import os
import secrets
import string

class ApiBackend:
    def generate_password(self, length, use_symbols):
        try:
            length = int(length)
        except (TypeError, ValueError):
            length = 12

        length = max(8, min(64, length))
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        if use_symbols:
            characters += string.punctuation

        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    if webview is None:
        raise ImportError(
            "La librería 'pywebview' no está instalada. Instale con: python -m pip install pywebview"
        )

    api = ApiBackend()
    html_file = os.path.abspath("index.html")
    webview.create_window("Generador de contraseñas", html_file, js_api=api, width=680, height=520, resizable=False)
    webview.start()

    def require_webview(self):
        if webview is None:
            raise ImportError(
                "La librería 'pywebview' no está instalada. Instale con: python -m pip install pywebview"
            )
        return webview