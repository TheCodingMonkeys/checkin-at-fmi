import autocomplete_light

from identifications.models import Cardowner

autocomplete_light.register(Cardowner,
    search_fields=['faculty_number'],
    autocomplete_js_attributes={'placeholder': 'faculty number'},
)
