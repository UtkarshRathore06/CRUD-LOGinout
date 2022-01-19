from django.shortcuts import render
from django.http import *
from myapp.forms import *

# Create your views here.

def show_choice_page(request):
          
          return render(request,'Choicepage.html',)

def save_user_regis_data(request):

          if request.method=='POST':
                    udata=User(request.POST)

                    if udata.is_valid():
                              udata.save()
                              return HttpResponse("NEW USER REGISTERED !!! ")
          else:
                    udata=User()

          return render(request,'Regis.html',{'record':udata})


def showlogin(request):
          

          alldata=NewUser.objects.all()
          if request.method=='POST':
                    tempdata=CheckUser(request.POST)
                    if tempdata.is_valid():
                              tempdata.save()

                    currentdata=CheckNewUser.objects.all()
                    if currentdata in alldata:
                              return HttpResponse("WELCOME USER !! ")
                    else:
                              return HttpResponse("ACCOUNT DOSENT EXIST !!")
                              
                              
                    
                    '''else:
                              return render(request,'check.html',{'data':tempdata})'''
          else:
                    tempdata=User()
          
          
          return render(request,'Login.html',{'record':tempdata})
                    
                                                  










                    

















