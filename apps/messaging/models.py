from django.contrib.auth.models import User
from django.db import models

from apps.abstracts.models import AbstractModel


class MessageModel(AbstractModel):
    """Model definition for MessageModel."""

    #is_active = models.BooleanField('Estado', default = True)    
    deleted_date = models.DateTimeField('Fecha de Eliminación', auto_now=True, auto_now_add=False, null=True)
    sender= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender') 
    receiver= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='receiver')     
    message_content = models.CharField('Contenido del mensaje', max_length=100, blank=False, null=False, unique=True)    
    
    
    class Meta:
        """Meta definition for MessageModel."""
        ordering = ["id"]
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        """Unicode representation of MessageModel."""
        return f"De {self.sender} para {self.receiver}: {self.message_content}"


# TODO: cambiar por el usuario de app users. id de sender y receiver con uuid. como hacer como modo conversación

    


    #id = models.AutoField(primary_key = True)
    # created = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    # updated = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
