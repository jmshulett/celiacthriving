from django.contrib import admin
from .models import ShopTips

@admin.register(ShopTips)
class TipsAdmin(admin.ModelAdmin):
    list_display = ['name', 'tip_desc', 'slug']
    prepopulated_fields = {'slug': ('name',)}

