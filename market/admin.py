from django.contrib import admin

from .models import Product  , Order


# tis class below will give us more details IN THE ADMIN PANNEL 
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product)
admin.site.register(Order)

admin.site.site_header = 'Hani Store Administration'                         
admin.site.site_title = 'Hani Store Administration' 