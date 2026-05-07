from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Senior Note: المتغيرات الثابتة (Constants) تتكتب Capital
    BOOK_STATUS = (
        ('available', 'متاح'), # الأفضل نخلي الكلمة التانية بالعربي عشان لو حبينا نعرضها لليوزر
        ('rented', 'مستعار'),       
        ('sold', 'مباع'),           
    )

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    
    # Senior Note: التنظيم هنا مهم، خلينا جانجو يكريت فولدر لكل سنة وشهر عشان الموقع يفضل سريع
    photo_book = models.ImageField(upload_to='photos/books/%Y/%m/%d/', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos/author/%Y/%m/%d/', null=True, blank=True)
    
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rental_price_day = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    total_rental_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    
    # ربطنا المتغير الجديد هنا
    status = models.CharField(max_length=20, choices=BOOK_STATUS, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title