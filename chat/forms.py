from django.forms import ModelForm
from .models import Song


class song_form(ModelForm):
    
    class Meta:
        model = Song
        fields = "__all__"
