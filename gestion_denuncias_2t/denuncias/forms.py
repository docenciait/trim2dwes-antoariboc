from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    
    
    titulo = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter title here'}),
        max_length=200
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your content here', 'rows': 5})
    )
    image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    categoria = forms.ChoiceField(
        choices=Denuncia.CATEGORIAS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    estado = forms.CharField(
        initial='pendiente',
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Denuncia
        fields = ['titulo', 'descripcion', 'image', 'categoria', 'estado']
     
    
        fields = ['titulo', 'descripcion', 'image', 'categoria', 'estado']

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.usuario = user
        if commit:
            instance.save()
        return instance