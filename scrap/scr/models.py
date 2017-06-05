from django.db import models

Company = (
    ('Smartlink Network Systems Ltd.','Smartlink Network Systems Ltd.'),
    ('Digisol Systems Ltd.', 'Digisol Systems Ltd.'),
    ('Synegra EMS Ltd.', 'Synegra EMS Ltd.'),
    ('Telesmart SCS Ltd.', 'Telesmart SCS Ltd.'),
)

Department = (
    ('hr & admin','HR & Admin'),
    ('purchase','Purchase'),
    ('rm stores','RM Stores'),
    ('synegra production', 'Synegra Production'),
    ('logistics & warehouse', 'Logistics & Warehouse'),
    ('commercial', 'Commercial'),
    ('accounts','Accounts'),
    ('legal','Legal'),
    ('s-tac','S-TAC'),
    ('it','IT'),
    ('qa','QA'),
    ('engineering','Engineering'),
    ('telesmart-production','Telesmart-Production'),
)

Type = (
    ('aging material','Aging Material'),
    ('hazardous', 'Hazardous'),
    ('e-waste', 'E-Waste'),
    ('metals', 'Metals'),
    ('paper', 'Paper'),
    ('plastic', 'Plastic'),
    ('furniture','Furniture'),
    ('machinery','Machinery'),
)

class Category(models.Model):
  company = models.CharField(max_length=100, choices=Company,
               default='it')
  department = models.CharField(max_length=100, choices=Department,
                 default='it')
  waste_type = models.CharField(max_length=100, choices=Type,
                 default='paper')
  description = models.CharField(max_length=1000)

  class Meta:
      verbose_name_plural = 'Categories'

  def __str__(self):
      return self.waste_type


class Quote(models.Model):
  name = models.CharField(max_length=100)
  contact_info = models.CharField(max_length=100)
  item = models.CharField(max_length=100)
  quantity = models.CharField(max_length=100)
  price = models.CharField(max_length=100)
  additional_info = models.CharField(max_length=1000)

  class Meta:
      verbose_name_plural = 'Quotes'

  def __str__(self):
      return self.item

class Random_m(models.Model):
    fill = models.CharField(max_length=100)
    def __str__(self):
        return self.fill
