from django.db import models


Department = (
    ('rma','R.M.A.'),
    ('production', 'Production'),
    ('warehouse', 'Warehouse'),
    ('maintenance', 'Maintenance'),
)

Type = (
    ('hazardous', 'Hazardous'),
    ('e-waste', 'e-Waste'),
    ('metals', 'Metals'),
    ('paper', 'Paper'),
    ('plastic', 'Plastic'),
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


class quote(models.Model):
  name = models.CharField(max_length=100)
  contact_info = models.CharField(max_length=100)
  item = models.CharField(max_length=100)
  quantity = models.CharField(max_length=100)
  price = models.CharField(max_length=100)
  additional_info = models.CharField(max_length=1000)

  def __str__(self):
      return self.item
