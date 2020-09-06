from django.contrib import admin

# Register your models here.
from caesar_cipher.models import (
    Article,
    Statistic,
    CapitalWord
)

admin.site.register(Article)
admin.site.register(Statistic)
admin.site.register(CapitalWord)