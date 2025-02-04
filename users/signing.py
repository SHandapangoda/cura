from django.core import signing
from django.urls import reverse
from django.conf import settings

def generate_verification_token(user):
    # Create a signed token containing the user's ID
    return signing.dumps({'user_id': user.id})

def verify_verification_token(token):
    try:
        # Verify and decode the token
        data = signing.loads(token, max_age=settings.EMAIL_VERIFICATION_TOKEN_MAX_AGE)
        return data['user_id']
    except (signing.BadSignature, signing.SignatureExpired):
        return None