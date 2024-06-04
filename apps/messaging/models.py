from django.db import models

from apps.abstracts.models import AbstractModel
from apps.properties.models import Property
from apps.users.models import User


class MessageModel(AbstractModel):
    """Model definition for MessageModel."""
    deleted_date = models.DateTimeField('Fecha de Eliminación', auto_now=True, auto_now_add=False, null=True)
    sender= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender') 
    receiver= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='receiver', blank=True)  # Se permite blank=True   
    property = models.ForeignKey(Property, related_name='property', null=True, on_delete=models.CASCADE)  
    message_content = models.CharField('Contenido del mensaje', max_length=200, blank=False, null=False)    
    
    
    class Meta:
        """Meta definition for MessageModel."""
        ordering = ["id"]
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        """Unicode representation of MessageModel."""
        return f"De {self.sender} para {self.receiver}: {self.message_content}"
    
    def save(self, *args, **kwargs):
        if not self.receiver:
            self.receiver = self.property.owner
        super(MessageModel, self).save(*args, **kwargs)


