from django.contrib import admin
from .models import Post , Category

class PostAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    emty_values_display = 'empty'
    list_display = ('title','author', 'counted_views', 'status', 'published_date')
    list_filter = ['status']
    search_fields = ['title', 'content']
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
