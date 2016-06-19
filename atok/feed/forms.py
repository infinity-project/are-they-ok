from django import forms

from .models import Update, Verify

class UpdateForm(forms.Form):
	Choices = (
		('Stable', 'Unstable', 'Emergency', 'Unknown'),
	)
	update_status = forms.ChoiceField(choices=Choices, required=True, label='Current Status')