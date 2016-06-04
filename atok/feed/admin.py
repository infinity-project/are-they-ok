from django.contrib import admin
from .models import Update, Verify

# Register your models here.

class VerifyInline(admin.TabularInline):
	model = Verify
	extra = 3
	
class UpdateDebug(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['update_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		]
	inlines = [VerifyInline]
		
admin.site.register(Update, UpdateDebug)
admin.site.register(Verify)