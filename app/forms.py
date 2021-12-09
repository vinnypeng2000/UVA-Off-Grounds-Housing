from .models import Review, Housing
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('housing','review', 'rating')

        widgets = {
            # 'housing' : forms.Select(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment'}),
            # 'rating': forms.Select(attrs={'class': 'form-control'}),
        }