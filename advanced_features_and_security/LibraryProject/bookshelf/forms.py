from django import forms


# --------------------------------------------------
# ALX-Required ExampleForm
# --------------------------------------------------
class ExampleForm(forms.Form):
    """
    Example form required by ALX checker.
    """
    name = forms.CharField(max_length=100, required=True)


# --------------------------------------------------
# Secure Search Form for Books
# --------------------------------------------------
class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label="Search",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )
