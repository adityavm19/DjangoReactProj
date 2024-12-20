from django.contrib import admin
from .models import UserAccount
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'first_name','last_name','username')
    fieldsets = (
        ('Users Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','username')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name', 'password1', 'password2','username'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(UserAccount, UserModelAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.


# Register your models here.
