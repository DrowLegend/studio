from django.db import models

# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True, null=True, default=None)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True, default=None)


class Photofon(models.Model):
    #type = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='fotofon/', blank=False)
    price = models.IntegerField(default=0)
    short_description = models.CharField(max_length=300, blank=False, default=0)

    class Meta:
        verbose_name = 'Фотофон'
        verbose_name_plural = 'Фотофоны'

    def __str__(self):
        self.name = self.color + ',' + self.size
        return self.name


class Mirror(models.Model):
    #type = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='mirror/', blank=False)
    price = models.IntegerField(default=0)
    short_description = models.CharField(max_length=300, blank=False, default=0)

    class Meta:
        verbose_name = 'Зеркало'
        verbose_name_plural = 'Зеркала'

    def __str__(self):
        self.name = self.color + ',' + self.size
        return self.name



#
# class Order(models.Model):
#     type = models.OneToOneField(Mirror, on_delete=models.CASCADE)
#     color =