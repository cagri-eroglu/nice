from django.contrib import admin
from dedektor.models import KategoriModel
from dedektor.models import YazilarModel
from dedektor.models import YorumModel



admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik') # baslik ve icerige göre arama yaptık admin panelde
    list_display = ( #yazilarin üzerine kategori gibi gelsin diye verdik
        'baslik','olusuturulma_tarihi','duzenlenme_tarihi'
    )
    
class YorumAdmin(admin.ModelAdmin):
    # burada değişik bir şey yaptım . arama yazan kişinin username ine göre olacak . Yazan bir user objesi onun da username'ine eriştim
    search_fields = ('yazan__username',) 
    list_display=(
        'yazan','olusturulma_tarihi','guncellenme_tarihi'
    )


admin.site.register(YazilarModel,YazilarAdmin) # burada da ikisini ilişkilendirdik
admin.site.register(YorumModel,YorumAdmin) # burada da ikisini ilişkilendirdik
