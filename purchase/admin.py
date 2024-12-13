from django.contrib import admin
from .models import MyUser, PurchaseRequest


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'balance')  # Fields to display in the admin list view
    search_fields = ('username',)  # Add search functionality for the username field
    ordering = ('id',)  # Order by ID in the list view


@admin.register(PurchaseRequest)
class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'coin_name', 'quantity', 'dollar_value', 'created_at')
    search_fields = ('coin_name', 'user__username')  # Search by coin name and username
    ordering = ('-created_at',)  # Order by creation date in descending order
