from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from login.models import  User
from django import forms
from Customer.views import customer_update
from Customer.models import Customer

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='customerID',max_length=50)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            customer = Customer.objects.filter(customerID__exact = username,password__exact = password)
            if customer:
                return render_to_response('../../Customer/templates/customer/book_view.html',{'customers':customer})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    print(request)
    return render_to_response('login.html',{'uf':uf})