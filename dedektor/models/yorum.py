from django.db import models
from django.contrib.auth.models import User
from dedektor.models import YazilarModel

class YorumModel(models.Model):
    
    #Yorumu yazanı bir user ile eşleştirdim daha sonra bu User'in üzerinden bu kullanıcının yorumlarına erişebileyim
    yazan = models.ForeignKey(User, on_delete=models.CASCADE,related_name='yorum') #yazanin yorumlarina erismek icin . aynı azamanda bu bir User objesi

    #Yazıyı bir YazıModel ile eşleştirdim daha sonra bu Yazı üzerinden bu yazının yorumlarına erişebileyim
    yazi = models.ForeignKey(YazilarModel,on_delete=models.CASCADE,related_name='yorumlar') #yazinin yorumlarina erismek icin

    yorum = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'yorum'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
    
    def __str__(self):
        return self.yazan.username
