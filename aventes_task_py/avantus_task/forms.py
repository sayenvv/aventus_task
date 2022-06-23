from django import forms

class BasicForm(forms.Form):
    master_string = forms.CharField()
    string1 = forms.CharField()
    string2 = forms.CharField()
    string3 = forms.CharField()
    string4 = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(BasicForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})