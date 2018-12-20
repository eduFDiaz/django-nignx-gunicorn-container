from django.contrib import admin
from .models import Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # better customization of Posts in Admin site
    list_display = ('title', 'published_date', 'author')
    ordering = ['-published_date']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
