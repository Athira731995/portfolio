from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    pass
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Post,PostAdmin)
# Register your models here.
