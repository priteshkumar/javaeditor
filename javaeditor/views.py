from django.shortcuts import render
import sys
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import requests
sys.path.append("/home/mavixk/PycharmProjects")
# Create your views here.

def index(request):
    print("get home page")
    return render(request,"javaeditor/editor.html")



@csrf_exempt
def compile(request):
    print("Compilation post api");
    #print(list(request.POST.items()))
    #print(request.body.decode("utf-8"))
    print(request.body.decode("utf-8"))
    queryURL = "https://api.jdoodle.com/v1/execute/";
    jdoodleparams = {
        "clientId": "897ecf21be30faf3b108e047795e8ee3",
        "clientSecret": "a4195f2f8e03cde574d313c70c9708eb9791ebb0789e13d41b7fc430c1b1354",
        "script": request.body.decode("utf-8"),
        "language": "java",
        "versionIndex": "0"
    }

    r = requests.post(queryURL,json=jdoodleparams)
    print(r.json())
    if(r.status_code == 200):
        return JsonResponse(r.json())
    return JsonResponse({"output":"Error occured"})
