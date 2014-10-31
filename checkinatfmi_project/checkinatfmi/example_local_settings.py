PROJECT_ROOT= Path(__file__).ancestor(3)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #postgresql_psycopg2',
        'NAME': "database",
        #'USER': keychain.db_user,
        # 'PASSWORD': keychain.db_pass,
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT.child("static")


# Make this unique, and don't share it with anybody.
# gets the secret_key from the env (put the secretkey in bashrc for example)
SECRET_KEY = ""
