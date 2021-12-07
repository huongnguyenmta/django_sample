from django import forms
import datetime

from .models import Author, Book


class CreateBookForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Book name: ",
        max_length=255,
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"}),
        label="Book description: ",
        required=False,
    )
    published_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="Published date: ",
    )
    author = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Author: ",
        queryset=Author.objects.all(),
    )
    cover_img = forms.ImageField(
        widget=forms.FileInput(attrs={"type": "file", "class": "form-control-file"}),
        label="Cover image: ",
    )
    created_at = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="Created at: ",
        initial=datetime.date.today(),
    )

    class Meta:
        model = Book
        fields = (
            "name",
            "description",
            "published_date",
            "author",
            "created_at",
            "cover_img",
        )
