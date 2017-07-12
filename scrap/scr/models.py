from django.db import models
import datetime

Location = (
    ('goa','Goa'),
    ('mumbai','Mumbai'),
    ('bangalore','Bangalore'),
)

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
  a = datetime.datetime.now()
  a = a.strftime("%d/%m/%y")
  time = models.CharField(max_length=20, default=a)
  location = models.CharField(max_length=100, choices=Location,
               default='goa')
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
  a = datetime.datetime.now()
  a = a.strftime("%d/%m/%y")
  time = models.CharField(max_length=20, default=a)
  location = models.CharField(max_length=100, choices=Location,
               default='goa')
  name = models.CharField(max_length=100)
  contact_info = models.CharField(max_length=100)
  item = models.CharField(max_length=100)
  quantity = models.CharField(max_length=100)
  price = models.CharField(max_length=100)
  additional_info = models.CharField(max_length=1000)
  certificates = models.URLField(default='null')


  class Meta:
      verbose_name_plural = 'Quotes'

  def __str__(self):
      return self.item

class trxn_m(models.Model):
  date = models.CharField('Date Sold',max_length=100)
  location = models.CharField(max_length=100, choices=Location,
               default='goa')
  items_description = models.CharField(max_length=10000)
  purchasing_party = models.CharField(max_length=1000)
  selling_price = models.CharField(max_length=1000)

  class Meta:
      verbose_name_plural = 'Transactions'

  def __str__(self):
        return self.purchasing_party + ' ' + self.date
