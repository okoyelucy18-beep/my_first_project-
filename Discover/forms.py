from django import forms

from .models import PrayerIntent, RetreatRequest


class PrayerIntentForm(forms.ModelForm):
    class Meta:
        model = PrayerIntent
        fields = ['name', 'email', 'phone', 'monastery', 'intention_type', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name or family'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+234 ...'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your prayer intention here...'}),
        }


class RetreatRequestForm(forms.ModelForm):
    class Meta:
        model = RetreatRequest
        fields = ['name', 'email', 'phone', 'monastery', 'stay_type', 'arrival_date', 'duration_days', 'notes']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about your retreat preference or group needs.'}),
        }
