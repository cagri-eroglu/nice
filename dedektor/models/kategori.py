from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30,blank=False,null=False)
    slug = AutoSlugField(populate_from='isim',unique=True)

    class Meta: #bu tablonun sqlite içindeki adını seçiyorum
        db_table= 'kategori'
        verbose_name_plural='kategoriler' #tablonun databasede görünen ismi
        verbose_name = 'Kategori' # 'Select "Kategori" to change kısmı (üstteki)'
    
    def __str__(self):
        return self.isim
