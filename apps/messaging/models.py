from django.db import models
from django.contrib.auth.models import User


class MessageModel(models.Model):
    """Model definition for MessageModel."""

    id = models.AutoField(primary_key = True)
    # state = models.BooleanField('Estado',default = True)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)
    sender= models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    # TODO: cambiar por el usuario de app users y agregar reciever
    content = models.CharField('Contenido del mensaje', max_length=100, blank=False, null=False, unique=True)

    
    class Meta:
        """Meta definition for MessageModel."""
        ordering = ["id"]
        verbose_name = 'Message Model'
        
    def __str__(self):
        """Unicode representation of MessageModel."""
        return self.content
