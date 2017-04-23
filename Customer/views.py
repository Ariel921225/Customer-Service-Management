from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from login.views import *

# Create your views here.
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customerID', 'fName', 'lName', 'joinDate', 'primaryEmailID', 'preferEmail', 'emailNotification',
              'billType', 'contactNo','password']

def index(request, template_name='customer/index.html'):

    ctx = {}

    return render(request, template_name, ctx)





class CustomerCreate(CreateView):
    model = Customer
    fields = ['customerID', 'fName', 'lName', 'joinDate', 'primaryEmailID', 'preferEmail', 'emailNotification',
              'billType', 'contactNo', 'password']


def customer_view(request, pk):
    customers = Customer.objects.filter(customerID=pk)
    ctx = {}
    ctx["customers"] = customers
    return render(request, 'customer/book_view.html', ctx)


def customer_create(request, template_name='customer/book_form.html'):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return customer_view(request,form.cleaned_data['customerID'])
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def customer_update(request, pk, template_name='customer/book_form.html'):
    customer = get_object_or_404(Customer, customerID=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return customer_view(request,pk)
    ctx = {}
    ctx["form"] = form
    ctx["customer"] = customer
    return render(request, template_name, ctx)


def customer_delete(request, pk, template_name='customer/book_confirm_delete.html'):
    customer = get_object_or_404(Customer, customerID=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('login:login')
    ctx = {}
    ctx["object"] = customer
    ctx["customer"] = customer
    return render(request, template_name, ctx)
