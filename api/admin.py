from django.contrib import admin
from .models import *
# Register your models here.

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality','current_club','age')
    list_filter = ('nationality','current_club')

class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'team','competition','season')
    list_filter = ('team','competition','season')

admin.site.register(Players,PlayersAdmin)
admin.site.register(Player_Stats,PlayerStatsAdmin)
