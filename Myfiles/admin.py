from django.contrib import admin
from Myfiles.models import *
# Register your models here.
class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']
class AdminPro(admin.ModelAdmin):
    list_display = ['id','nomi','narxi','tur','malumot','rasm1','rasm2','rasm3']

class AdminNew(admin.ModelAdmin):
    list_display = ['id','nomi','malumot','rasm']

admin.site.register(New,AdminNew)

class AdminSotib(admin.ModelAdmin):
    list_display = ['id','mijoz_id','tel','mijoz_username','nomi','narxi','miqdori','vaqt',]

class AdminMurojat(admin.ModelAdmin):
    list_display = ['id','ism','mail','tel','matn']

class AdminComment(admin.ModelAdmin):
    list_display = ['id','ism','tur','mail','tel','matn']

class AdminAnketa(admin.ModelAdmin):
    list_display = ['id','ism','username','fam','jins','tel','shaxar','yosh',]

admin.site.register(Anketa,AdminAnketa)
admin.site.register(Murojatlar,AdminMurojat)

admin.site.register(Comment,AdminComment)
admin.site.register(Sotib_olingan_maxsulotlar,AdminSotib)


admin.site.register(Type,AdminTur)
admin.site.register(Product,AdminPro)