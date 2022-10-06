from distutils.command.upload import upload
from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
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
    full_name = models.CharField(_("full name"), max_length=255)
    email = models.EmailField(_("email address"), unique=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_staff = models.BooleanField(("staff status"),default=False)
    is_active = models.BooleanField(("active"),default=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        

class Image(models.Model):
    nameImage = models.CharField(max_length=20, blank=False, null=False) 
    image = models.FileField(upload_to="media")
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name = 'Usuario')


    def save(self, *args, **kwargs):
        
        self.image.name = f'{self.user.id}/{self.nameImage}.%s' % self.image.name.split('.')[1]

        super(Image, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nameImage






