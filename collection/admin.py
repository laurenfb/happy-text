from django.contrib import admin

# Register your models here.
from collection.models import User, Quote

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('name', 'id',)
    prepopulated_fields = {'slug': ('name',)}

class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ('author', 'text',)
    prepopulated_fields = {'slug': ('author',)}


admin.site.register(User, UserAdmin)
admin.site.register(Quote, QuoteAdmin)
