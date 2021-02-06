from django.contrib import admin
from main.models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
	list_display = ('id', 'ip')
	save_as = True
