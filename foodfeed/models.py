from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from datetime import *
from foodfeed.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateField(_("Date"), default=date.today)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    avatar = models.ImageField(upload_to='user_pictures', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.get_full_name()


class Picture(models.Model):

    author = models.ForeignKey(User)
    picture = models.ImageField(upload_to="user_uploads", blank=True, null=True)
    description = models.TextField()
    date_published = models.DateTimeField(default=datetime.now())

    def __str__(self):
        if str(self.author)[-1] == "s":
            return str(self.author) + "' picture"
        else:
            return str(self.author) + "'s picture"


class Rating(models.Model):

    author = models.ForeignKey(User)
    picture = models.ForeignKey(Picture)
    health_rating = models.PositiveIntegerField(default=5)
    style_rating = models.PositiveIntegerField(default=5)
    cooking_rating = models.PositiveIntegerField(default=5)


class Comment(models.Model):

    author = models.ForeignKey(User)
    picture = models.ForeignKey(Picture)
    comment = models.TextField()
