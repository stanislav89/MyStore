from django.contrib import admin
from StoreApp.models import Articles, User, Purchase
from django.contrib.auth import get_user_model

# Register your models here.
admin.site.register(Articles)
admin.site.register(User)
admin.site.register(Purchase)
