from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html

from .models import *

class ProductOrder(admin.ModelAdmin):
    ordering = ['brand']
    readonly_fields = ['img_preview']
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['name','image_tag',]


class ShopOrder(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.product.image.url))

    list_display = ['product','image_tag',]


# Register your models here.

admin.site.register(product, ProductOrder)
admin.site.register(company)
admin.site.register(brand)
admin.site.register(shops_SPB)
admin.site.register(supermarkets_SPB)

@admin.register(perek_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.product.image.url))

    list_display = ['product','image_tag',]
    pass

@admin.register(peterechka_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(briz_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(vkuster_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(plovdiv_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(rosneft_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(dixy_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(prisma_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(vernyi_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(magnit_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(lenta_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(auchan_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(ok_spb)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass