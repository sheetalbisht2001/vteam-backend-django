from django.utils.translation import ugettext_lazy as _
from stractor.constants.fields import UuidPKField, CreatedAtField, UpdatedAtField
from django.db import models


class Distributor(models.Model):  #representing a database table here
    id = UuidPKField()     
    registration_date = models.DateField(null=True, blank=True)
    designation = models.CharField(max_length=255,null=True, blank=True)
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    prev_cumpv = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    exclusive_pv = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    self_pv = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    group_pv = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    total_pv = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    short_points = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    next_level_percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    vid = models.CharField(max_length=255)
    upline =models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='downlines')
    address = models.CharField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=255,null=True, blank=True)
 

    class Meta:
        db_table = 'distributor'
        verbose_name = _('Distributor')
        verbose_name_plural = _('Distributors')

    def __str__(self):
        return '%s (%s)' % (self.__class__.__name__, self.id)


