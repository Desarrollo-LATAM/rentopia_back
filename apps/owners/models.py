import os

from django.db import models

from apps.users.models import User


def get_upload_path(instance, filename):
    """
    This function is used to create a unique filename for each image uploaded to the server.
    :param instance: The instance parameter is the model instance that the file is attached to.
    :param filename: The filename parameter is the name of the file that was uploaded.
    :return: The function returns a string containing the path where the file will be saved.
    """
    return os.path.join("fotos", "perfiles", str(instance.pk), filename)


# Create your models here.
class Owner(models.Model):
    """
     The Owner is extended user data.

    Args:
        user_id ( str ): related with user model
        is_producer ( coolean ): productor or user
        qualifications ( float ): average of the grades obtained
        is_active ( boolean ): logic delete.
    """

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    rating_user = models.PositiveIntegerField(default=0)
    photo = models.ImageField(
        "Profiles",
        upload_to=get_upload_path,
        default="perfil.jpg",
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Propietario"
        verbose_name_plural = "Propietarios"
