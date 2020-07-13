from django.shortcuts import render , redirect
from .models import Commands
# Create your views here.
def first_page(request):
    if request.method == "GET":
        return render(request, "welcome_page.html")

def exercise_number_1(request):
    if request.method == "GET":
        return render(request, "lesson1.html")

def exercise_number_2(request):
    if request.method == "GET":
        return render(request, "lesson2.html")

def exercise_number_3(request):
    if request.method == "GET":
        return render(request, "lesson3.html")

def exercise_number_4(request):
    if request.method == "GET":
        return render(request, "lesson4.html")

def exercise_number_5(request):
    if request.method == "GET":
        return render(request, "lesson5.html")

def exercise_number_6(request):
    if request.method == "GET":
        return render(request, "lesson6.html")

def exercise_number_7(request):
    if request.method == "GET":
        return render(request, "lesson7.html")

def exercise_number_8(request):
    if request.method == "GET":
        return render(request, "lesson8.html")

def exercise_number_9(request):
    if request.method == "GET":
        return render(request, "lesson9.html")

def exercise_number_10(request):
    if request.method == "GET":
        return render(request, "lesson10.html")

def exercise_number_11(request):
    if request.method == "GET":
        return render(request, "lesson11.html")

def exercise_number_12(request):
    if request.method == "GET":
        return render(request, "lesson12.html")

def exercise_number_13(request):
    if request.method == "GET":
        return render(request, "lesson13.html")

def exercise_number_14(request):
    if request.method == "GET":
        return render(request, "lesson14.html")

def exercise_number_15(request):
    if request.method == "GET":
        return render(request, "lesson15.html")

def exercise_number_16(request):
    if request.method == "GET":
        return render(request, "lesson16.html")

def exercise_number_17(request):
    if request.method == "GET":
        return render(request, "lesson17.html")

def main_page(request):
    if request.method == "GET":
        return render(request, "form.html")
        #return redirect('ali')
"""def nameresult(request):
    if request.method == "POST":
        data2 = request.POST.get('city')
        Commands.objects.create(data2=data2)
        if data2=="tehran" :
            return render(request, "tehran.html")
        if data2=="shiraz" :
            return render(request, "shiraz.html")
        if data2=="shiraz" :
            return render(request, "esfahan.html")"""

def check_command(request):
    if request.method == "POST":
        command1 = request.POST.get('command1') 
        command2 = request.POST.get('command2') 
        # Commands.objects.create(command1 = command1 , command2=command2 , )
        command = Commands.objects.get(lesson='1')
        if command.command1 == command1 and command.command2 == command2 :
            return redirect(request,'/home') 
        else:
            return render(request, "lesson1.html")
#def showing_exercise(request):
#v=request.GET.get(s) s=variable male search
#t=esmeclass.objects.filter(name=v) #hamaro migire # get = yedone migire
#return render(request,"h.html",context={"t":t})
  