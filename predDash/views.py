from django.shortcuts import render,redirect
from .forms import AnalysisDeets_Form,CreateUserForm,LoginUserForm
import pandas as pd
from .loadModel import loadModel,makepred
from .models import AnalysisDeets
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
            else:
                print(str(form))

    

    context = {'form': form}

    return render(request, 'predDash/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginUserForm()

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

          

            if user is not None:
                login(request, user)
                messages.info(request, 'Login Successful')
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {'form': form}
        return render(request, 'predDash/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    # messages.success(request, 'Logout Successful')
    return redirect('login')

@login_required(login_url='login')
def home(request):
    predsList = AnalysisDeets.objects.all()
    
    

    

    context = {'predlist': predsList}
    for preds in predsList:
        print(preds.patient_id)
    print(predsList)

 
    return render(request,'predDash/home.html',context)

@login_required(login_url='login')
def addUtils(request):
    form = AnalysisDeets_Form()
    if request.method == 'POST':
    
        form = AnalysisDeets_Form(request.POST)

        if form.is_valid():
            form.save()
            pred_value = AnalysisDeets.objects.all().get(patient_id= form.cleaned_data['patient_id'])
            df = pd.DataFrame([form.cleaned_data])
            df.drop(["patient_id"], axis=1, inplace=True)
          
            #Loading the model
            x=loadModel()
            #pass data to the model to make a prediction
            pred=makepred(x,df)

            #Update prediction column in data data based on the  model's prediction
           
            if pred==1:
                pred_value.prediction='M'
         
            else:
                pred_value.prediction='B'
            
           
           
            
            pred_value.save()
            

            return redirect('home')
        else:
            print(str(form))

    

    context = {'form': form}

    return render(request,'predDash/addutils.html',context)