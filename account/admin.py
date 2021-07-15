from django.contrib import admin
from .models import Doctor, Patient, Post

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','slug','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)