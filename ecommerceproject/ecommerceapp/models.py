from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='category')
    class Meta:
        ordering=['name',]
        verbose_name='category'
        verbose_name_plural='categorys'

    def get_url(self):
        return reverse('ecommerceapp:product_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='product')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField(default=True)
    class Meta:
        ordering=['name',]
        verbose_name='product'
        verbose_name_plural='products'

    def get_url(self):
        return reverse('ecommerceapp:product_detail',args=[self.category.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.name)