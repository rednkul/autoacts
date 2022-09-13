from django.contrib import admin
from django.contrib.auth import get_user_model




#from .forms import CustomUserCreationForm, CustomUserChangeForm



@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = get_user_model()
    list_display = ('id', 'email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)




