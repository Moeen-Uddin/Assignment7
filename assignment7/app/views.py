from django.shortcuts import render


# Create your views here.
def home(request):
    numbers = [1,2,3,4,5,6,7,8,9,10]
    def even(x):
        if x % 2 :
            return x
    odd_list = list(filter(even,numbers))
    dic ={
        'odd_list' : odd_list,
        'title'    : "Home"
    }
    return render(request,'home.html',dic)