# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils.text import slugify
# from django.conf import settings


# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product_creator"
    )
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=256)
    price = models.FloatField()
    # models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    description = models.TextField(blank=True)
    # description_short = models.CharField(max_length=50)
    # description_long = models.TextField()

    stock = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(
        default=True
    )  # if the product is not active to but, for example out of stock

    image = models.ImageField(
        upload_to="product_images/"
    )  # maybe should be char or text, to give the ability for the seller to upload
    # slug = models.SlugField(max_length=256) # to have the ability to write the product name in the url directly
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = "Products"
        ordering = (
            "-created",
        )  # descending order, the last item that is added to the database is shown first

    def __str__(self):
        return self.title




class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name,
                                     self.created_at,
                                     self.updated_at)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.user,
                                               self.item,
                                               self.quantity,
                                               self.created_at,
                                               self.updated_at)



# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     ref_code = models.CharField(max_length=20)
#     products = models.ManyToManyField(Cart)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)


#     def __str__(self):
#         return self.user.username

#     def get_total(self):
#         total = 0
#         for order_item in self.products.all():
#             total += order_item.get_total_item_price()
#         return total

# class Address(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     street_address = models.CharField(max_length=100)
#     apartment_address = models.CharField(max_length=100)
#     country = CountryField(multiple=False)
#     zip = models.CharField(max_length=100)
#     address_type = models.CharField(max_length=1)
#     default = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

#     class Meta:
#         verbose_name_plural = 'Addresses'


# class Payment(models.Model):
#     stripe_charge_id = models.CharField(max_length=50)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.SET_NULL, blank=True, null=True)
#     amount = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username
       

# class Cart(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} of {self.product.title}"    

#     def get_total_item_price(self):
#         return self.quantity * self.product.price