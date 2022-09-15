from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)


    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=256)
    price = models.FloatField()  # models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    description = models.TextField(blank=True)
    # description_short = models.CharField(max_length=50)
    # description_long = models.TextField()

    stock = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True) # if the product is not active to but, for example out of stock

    image = models.ImageField(upload_to='product_images/') # maybe should be char or text, to give the ability for the seller to upload 
    # slug = models.SlugField(max_length=256) # to have the ability to write the product name in the url directly
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',) # descending order, the last item that is added to the database is shown first

    def __str__(self):
        return self.title



class Order:
    pass

class Cart:
    pass

class Payment:
    pass

