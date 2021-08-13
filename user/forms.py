from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50, required=True, label="Kullanıcı adı:")
    password = forms.CharField(
        max_length=20, label="Şifre", widget=forms.PasswordInput, required=True)


class RegisterForm(forms.Form):

    username = forms.CharField(
        max_length=50, required=True, label="Kullanıcı adı:")
    password = forms.CharField(
        max_length=20, label="Şifre", widget=forms.PasswordInput, required=True)
    confirm = forms.CharField(
        max_length=20, label="Şifreyi Doğrula", widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifreler Eşleşmiyor!")

        values = {
            "username": username,
            "password": password
        }
        return values
