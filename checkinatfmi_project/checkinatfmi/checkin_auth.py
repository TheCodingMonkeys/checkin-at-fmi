from django.contrib.auth.models import User

class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            user = User.objects.get(email=username)
        else:
            user = User.objects.get(username=username)

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
