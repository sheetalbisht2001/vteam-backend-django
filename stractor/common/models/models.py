from django.utils.translation import ugettext_lazy as _
from stractor.constants.fields import UuidPKField, CreatedAtField, UpdatedAtField
from django.db import models


class Distributor(models.Model):
    id = UuidPKField()
    name = models.CharField(max_length=255)
    vid = models.CharField(max_length=255)
    upline =models.ForeignKey('self', on_delete=models.SET_NULL, Null=True, blank=True, related_name='downlines')
    address = models.CharField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=255,null=True, blank=True)
 

    class Meta:
        db_table = 'distributor'
        verbose_name = _('Distributor')
        verbose_name_plural = _('Distributors')
        ordering = ['-created_at']

    def __str__(self):
        return '%s (%s)' % (self.__class__.__name__, self.id)


