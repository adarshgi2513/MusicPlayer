from django import forms
from .models import song

class Dataform(forms.ModelForm):
    class Meta:
        model = song
        fields = ['title', 'artist','image','audio_file','audio_link','duration']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'artist':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'audio_file':forms.FileInput(attrs={'class':'form-control'}),        
            'audio_link':forms.TextInput (attrs={'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control'}),
       }