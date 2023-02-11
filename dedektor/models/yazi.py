from django.db import models
from autoslug import AutoSlugField
from dedektor.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class YazilarModel(models.Model):
    resim=models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    olusuturulma_tarihi = models.DateTimeField(auto_now_add=True) #olusuturlma tarihi otomotik dolacak 
    duzenlenme_tarihi = models.DateTimeField(auto_now=True) # değiştirilme otomotik 
    slug = AutoSlugField(populate_from='baslik',unique=True)

    # bir yazi birden fazla kategoriye atanbabilsin diye manytomany,
    #ayrıca bir kategorinin bütün yazılarına erişmek için de related_name
    # Mnay to mayn fielddan dolay "Yazi_kategoriler diye bir tablo daha oluştu"
    kategoriler = models.ManyToManyField(KategoriModel,related_name='yazi') 
    #yazarı djangodaki gömülü User tablosuna ekledik
    yazar = models.ForeignKey(User, on_delete=models.CASCADE,related_name='yazilar')

    class Meta:
        db_table='Yazi'
        verbose_name = 'Yazi'
        verbose_name_plural='yazilar'
    
    def __str__(self):
        return self.baslik
    
