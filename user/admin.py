from django.contrib import admin

# Register your models here.
from user.models import CustomUser, ActivityDetail


@admin.register(CustomUser)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(ActivityDetail)
class BookAdmin(admin.ModelAdmin):
    pass
