from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from .models import AnalysisDeets

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block mt-1 w-full text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            self.fields[field].widget.attrs['placeholder'] = field


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block mt-1 w-full text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            self.fields[field].widget.attrs['placeholder'] = field

class AnalysisDeets_Form(ModelForm):
    class Meta:
        model = AnalysisDeets
        fields = '__all__'
        exclude=('prediction',)
    def __init__(self, *args, **kwargs):
        super(AnalysisDeets_Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block px-4 py-3 mb-3 w-full leading-tight text-gray-700 bg-gray-200 rounded border border-blue-500 appearance-none focus:outline-none focus:bg-white'
          
            self.fields[field].widget.attrs['placeholder'] = field
    def updateField(self,pred):
        value = self.cleaned_data.get("prediction")
        value2 = self.cleaned_data.get("patient_id")
        try:
            value2='hey man'

            if pred==1:
                value='M'
            else:
                value='B'
           

        except:
            print("There is an issue in updating the prediction")

        

          