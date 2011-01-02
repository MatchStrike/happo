from champion_manager.models import City, Champion
from django.contrib import admin

class CityAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(City, CityAdmin)
admin.site.register(Champion)