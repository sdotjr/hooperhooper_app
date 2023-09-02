from django.contrib import admin
from .models import PlayerProfile

class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'position', 'experience_level', 'availability', 'preferred_game_type')
    search_fields = ('username', 'position', 'experience_level')
    list_filter = ('experience_level', 'preferred_game_type', 'position')
    ordering = ('username',)

    # If you have many-to-many fields or foreign keys, consider using this to improve performance:
    # raw_id_fields = ('related_field_name',)

admin.site.register(PlayerProfile, PlayerProfileAdmin)
