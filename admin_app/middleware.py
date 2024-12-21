from cryptography.fernet import Fernet
from django.conf import settings

# Generate this key once and save it somewhere safe
# Key = Fernet.generate_key()
# Store the key in the Django settings (or a secure environment variable)
KEY = settings.SECRET_KEY

class EncryptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Encrypt the message before sending
        if hasattr(request, 'message'):
            fernet = Fernet(KEY)
            encrypted_message = fernet.encrypt(request.message.encode())
            request.message = encrypted_message
        return response

class DecryptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Decrypt the message when received
        if hasattr(response, 'message'):
            fernet = Fernet(KEY)
            decrypted_message = fernet.decrypt(response.message).decode()
            response.message = decrypted_message
        return response
