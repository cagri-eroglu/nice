from django.contrib import admin
from dedektor.models import KategoriModel
from dedektor.models import YazilarModel


admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik') # baslik ve icerige göre arama yaptık admin panelde
    list_display = ( #yazilarin üzerine kategori gibi gelsin diye verdik
        'baslik','olusuturulma_tarihi','duzenlenme_tarihi'
    )


admin.site.register(YazilarModel,YazilarAdmin) # burada da ikisini ilişkilendirdik
