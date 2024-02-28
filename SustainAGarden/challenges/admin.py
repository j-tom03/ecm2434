from django.contrib.auth.admin import UserAdmin

from .forms import UserForm
from .models import User

# Register your models here.
from django.contrib import admin


class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["challenge", "coins"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["registration_required", "template_name"],
            },
        ),
    ]


class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    model = User
    list_display = ["username", "email", "setter", "institution"]
    list_filter = ["setter", "institution"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email",)}),
        ("Permissions", {"fields": ("setter", "institution")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2", "setter", "institution"),
            },
        ),
    )
    search_fields = ["username"]
    ordering = ["username"]


admin.site.register(User, CustomUserAdmin)
