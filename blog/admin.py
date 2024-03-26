from django.contrib import admin
# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('id','author','title','content','date_posted')

admin.site.register(Post,PostAdmin)
admin.site.site_header = "Py Dj Blog Admin"
