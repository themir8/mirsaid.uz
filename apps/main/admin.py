from django.contrib import admin
from main.models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
	list_display = ('id', 'ip', 'url')
	list_display_links = ('ip',)
	readonly_fields = ('ip', 'url')
	save_as = True
