from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from account.models import UserProfile
from django.contrib import admin

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0

class MyUserAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
