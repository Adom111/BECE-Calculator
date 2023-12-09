from operator import itemgetter
from urllib import request, response
from django.shortcuts import render
from .models import Becedb



# Create your views here.
name = "Aaron"

def index(request):
    return render(request,'index.html')


def bece(request):
    pointer = Becedb.objects.all()
    
    core_grade = 0
    elect_grade = 0
    t_grade = 0
    elect = {}


    if request.method == "POST":
        
        ls = request.POST.get("subject", "default") + " " + request.POST.get("grade", default="1" )

        
        if request.POST.get("add"):

            for item in pointer:  
                match request.POST.get("subject"):
                    case item.subj_name:
                        item.subj_grade = int(request.POST.get("grade"))
                        item.subj_add = request.POST.get("add")
                        item.save()

                    

        if request.POST.get("remove"):

            for item in pointer:
                if request.POST.get("remove"+str(item.id)) == "remove":
                    item.subj_grade = 0
                    item.subj_add = False
                    item.save()



        if request.POST.get("calculate"):

            
            for item in pointer:
                if item.subj_add:
                    if item.subj_type == "core":
                        core_grade += item.subj_grade

                    else:
                        elect[item.subj_name] = item.subj_grade

        elect = dict(sorted(elect.items(),key=itemgetter(1))[:2])

        for x in elect.values():
            elect_grade += x

        t_grade = core_grade + elect_grade

        
        if request.POST.get("clean"):
            for item in pointer:
                item.subj_grade = 0
                item.subj_add = False
                item.save()



        return render(request,"bece.html", {"pointer":pointer,"ls":ls,"core_grade":core_grade,"elect_grade":elect_grade,"t_grade":t_grade,"elect":elect})


    return render(request,"bece.html", {"pointer":pointer})
