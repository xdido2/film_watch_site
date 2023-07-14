from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import CharField, EmailField, BooleanField, DateTimeField, ImageField, ForeignKey, CASCADE, \
    ManyToManyField
from django.utils.translation import gettext_lazy as _

from apps.shared.models import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    avatar = ImageField(upload_to='users/avatars/')
    username = CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    email = EmailField(_("email address"), blank=True, unique=True)
    is_staff = BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = DateTimeField(_("date joined"), default=datetime.now)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        swappable = "AUTH_USER_MODEL"


User._meta.get_field('groups').related_name = 'user_set_custom'
User._meta.get_field('user_permissions').related_name = 'user_set_custom_permissions'
