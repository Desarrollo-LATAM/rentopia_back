from django.contrib.auth.models import User
from django.db import models


class MessageModel(models.Model):
    """Model definition for MessageModel."""

    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado',default = True)
    created = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    updated = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False, null=True)
    sender= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sent_messages') 
    receiver= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='received_messages')     
    message_content = models.CharField('Contenido del mensaje', max_length=100, blank=False, null=False, unique=True)

    
    class Meta:
        """Meta definition for MessageModel."""
        ordering = ["id"]
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        """Unicode representation of MessageModel."""
        return f"De {self.sender} para {self.receiver}: {self.message_content}"


# TODO: cambiar por el usuario de app users