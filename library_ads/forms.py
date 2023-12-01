from django import forms

class BorrowBookForm(forms.Form):
    borrow_quantity = forms.IntegerField(min_value=1, label='Quantidade para Empréstimo')

class ReturnBookForm(forms.Form):
    return_quantity = forms.IntegerField(min_value=1, label='Quantidade para Devolução')