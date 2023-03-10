from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), blank=True, unique=True)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email,
                                                           'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Підтвердження учётного запису для {self.user.username}'
        message = 'Для підтвердження облікового {} перейдіть по ссилці {}'.format(
            self.user.email, verification_link)
        send_mail(
            subject=subject,
            message=message,
            from_email='from@example.com',  # settings.EMAIL_HOST_USER
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
