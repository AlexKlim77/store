# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# for work with Out-Mail-Server
EMAIL_HOST = ''  # for smtp/imap - out
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None