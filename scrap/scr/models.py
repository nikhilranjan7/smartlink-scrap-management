from django.db import models


Department = (
    ('rma','RMA'),
    ('production', 'PRODUCTION'),
    ('warehouse', 'WAREHOUSE'),
    ('maintenance', 'MAINTENANCE'),
)

Type = (
    ('hazardous', 'HAZARDOUS'),
    ('e-waster', 'E-WASTE'),
    ('metals', 'METALS'),
    ('paper', 'PAPER'),
    ('plastic', 'PLASTIC'),
)

class Category(models.Model):
  department = models.CharField(max_length=14, choices=Department,
                 default='rma')
  waste_type = models.CharField(max_length=14, choices=Type,
                 default='paper')
  description = models.CharField(max_length=100)

  class Meta:
      verbose_name_plural = 'Categories'

  def __str__(self):
      return self.waste_type
