from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class VisitorAdmin(admin.ModelAdmin):
	# list_display = ('id', 'ip', 'url')
	# list_display_links = ('ip',)
	# readonly_fields = ('ip', 'url')
	# save_as = True
	pass
