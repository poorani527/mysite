from django import forms

class ContactForm(forms.Form):
    start_Date_Roll = forms.DateField(label='Start Date:',widget=forms.SelectDateWidget) 
    end_Date_Roll = forms.DateField(label='End Date:',widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    start_Date_Delta = forms.DateField(label='Start Date:',widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    end_Date_Delta = forms.DateField(label='End Date:',widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        start_Date_Roll = cleaned_data.get('start_Date_Roll')
        end_Date_Roll = cleaned_data.get('end_Date_Roll')
        start_Date_Delta = cleaned_data.get('start_Date_Delta')
        end_Date_Delta = cleaned_data.get('end_Date_Delta')

        if not start_Date_Roll and not end_Date_Roll and not start_Date_Delta and not end_Date_Delta:
            raise forms.ValidationError('You have to write something!')