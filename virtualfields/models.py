from django.db import models
from django.core.exceptions import ValidationError
from fields import VirtualTextField



class ModelWithVirtual(models.Model):

    def clean(self):
        for field in self._meta.virtual_fields:
            field.clean(self)

    class Meta:
        abstract = True



class Test(ModelWithVirtual):
    store = models.TextField()
    vtf = VirtualTextField()
