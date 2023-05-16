from django.shortcuts import render, redirect
from .models import fee
from django.contrib import messages

def index(request):
    data = fee.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        bank_code = request.POST.get('bank_code')
        query = fee(name=name, bank_code=bank_code)
        query.save()
        messages.info(request, "Data Inserted Successfully")
        return redirect("/")
    return render(request, "insert.html")

def updateData(request, id):
    if request.method == "POST":
        name = request.POST['name']
        bank_code = request.POST['bank_code']
        edit = fee.objects.get(id=id)
        edit.name = name
        edit.bank_code = bank_code
        edit.save()
        messages.warning(request, "Data Updated Successfully")
        return redirect("/")
    data = fee.objects.get(id=id)
    context = {"data": data}
    return render(request, "edit.html", context)

def deleteData(request, id):
    data = fee.objects.get(id=id)
    data.delete()
    messages.success(request, "Data deleted Successfully")
    return redirect("/")
