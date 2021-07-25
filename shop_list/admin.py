from django.contrib import admin

from .models import Tag, Item

# Register your models here.

class TagAdmin(admin.ModelAdmin):
  list_display = ("tag_name",)

class ItemAdmin(admin.ModelAdmin):
  list_filter = ("item_tag",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Item, ItemAdmin)