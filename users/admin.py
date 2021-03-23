from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import NewUser

UserAdmin.list_display = ('email','username','phone_number','gender','profile_image','last_login')
UserAdmin.ordering = ('-last_login',)
UserAdmin.fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_seller')}),
        ('Personal', {'fields': ('about','phone_number','profile_image')}),
    )

admin.site.register(NewUser, UserAdmin)
