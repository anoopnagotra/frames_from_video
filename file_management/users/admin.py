# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# # Unregister the provided model admin
# admin.site.unregister(UserGroup)

# # Register out own model admin, based on the default UserAdmin
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     pass

# admin.site.unregister(Group)

from django.apps import apps

# # admin.site.register(User, UserAdmin)
# Bookmark
models = apps.get_models()

# for model in models:
# 	# print("=======================")
# 	# print(model)
# 	# if "User" in model:
# 	try:
# 		admin.site.register(model)
# 	except admin.sites.AlreadyRegistered:
# 		pass



from django.contrib import admin
# Need to import this since auth models get registered on import.
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
from .models import User, MyVideo

# admin.site.unregister(User)
admin.site.unregister(auth.models.Group)



from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ('username',)
#     # username = forms.EmailField(max_length=64, help_text="The person's email address.")
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         return email


# class UserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = User
#     list_display = ['email', 'name',]

# admin.site.register(User, UserAdmin)




# Third Party Stuff
# from django.conf import settings
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
# from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
# from django.contrib.admin.actions import delete_selected as admin_delete_selected
# from rangefilter.filter import DateTimeRangeFilter

# # Electric_Soul Stuff
# from electric_soul.auth import services
# from electric_soul.base.models import ElasticSearchWrapper
# from .models import User, UserActivationKey, UserFollow, Device


# # Forms
# # ----------------------------------------------------------------------------
# class MyUserCreationForm(DjangoUserCreationForm):
#     class Meta:
#         model = User
#         fields = ("email", "username")


# class MyUserChangeForm(DjangoUserChangeForm):
#     class Meta:
#         model = User
#         fields = '__all__'


# # ModelAdmins
# # ----------------------------------------------------------------------------
# @admin.register(User)
# class UserAdmin(AuthUserAdmin):
#     add_form_template = 'admin/auth/user/add_form.html'
#     model = User
#     fieldsets = (
#         (None, {'fields': ('email', 'username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'cover_image', 'country','role',)}),
#         ('Facebook info', {'fields': ('fb_id', 'fb_auth_token', 'fb_data', 'fb_invite_image')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                     'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'password1', 'password2'),
#         }),
#     )
#     readonly_fields = ('date_joined', 'last_login')
#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#     list_display = ('email', 'username', 'first_name', 'last_name','is_active')
#     list_filter = (('date_joined', DateTimeRangeFilter), 'is_superuser', 'is_active', 'country')
#     search_fields = ('first_name', 'last_name', 'email', 'username')
#     ordering = ('email', '-date_joined')
#     actions = ['delete_selected', 'resend_activation']



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(role = 'user')

    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email','name','mobile_number', 'address', 'city', 'country','postal_code','is_active')
    # list_filter = ('name', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('name','mobile_number','role', 'state', 'city', 'country','postal_code',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active')}
        ),
    )
    search_fields = ('email',)
    list_filter = ('state',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)


class TOCUser(User):
    class Meta:
        proxy = True


def send_account_details(modeladmin, request, queryset):
    # Your email sending code here.
    # The queryset contains selected users
    print("I am here")
    return True

class TOCUserAdmin(UserAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(role = 'toc')

    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email','name','role', 'state', 'country','is_active')
    # list_filter = ('name', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('name', 'role','mobile_number', 'state', 'city', 'country','postal_code',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2', 'state', 'role', 'is_active')}
        ),
    )
    # search_fields = ('email',)
    search_fields = ('username', 'name', 'email')
    list_filter = ('state',)
    ordering = ('email',)
    actions = ['send_account_details']
   

    # def save_model(self, request, obj, form, change):
    #     super(TOCUserAdmin, self).save_model(request, obj, form, change)
    #     obj.user = request.user
    #     # obj.profile.email_confirmed = True
    #     # obj.profile.save()
    #     print(obj)
    #     # if not change:
    #     #     current_site = get_current_site(request)
    #     #     subject = 'Your Account Login Details'
    #     #     message = render_to_string('accounts/email/account_detail_email.html', {
    #     #         'user': obj.user,
    #     #         'domain': current_site.domain,
    #     #     })
    #     #     obj.user.email_user(subject, message)



class MyVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status','full_path')
    list_display_links = ('id','title')


admin.site.register(MyVideo, MyVideoAdmin)
admin.site.register(TOCUser, TOCUserAdmin)