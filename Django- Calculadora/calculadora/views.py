from django.shortcuts import render

def templateCalculadora(request):
    return render(request,"calculadora.html",{"resultado":"0"})

def calculate(request):
    try:
        int(request.GET["n1"])
        int(request.GET["n2"])
    except:
        return render(request,"calculadora.html",{"resultado":""})

    if request.GET["operation"] == "sum":
        return render(request,"calculadora.html",{"resultado":"El resultado es: "+str(int(request.GET["n1"])+int(request.GET["n2"]))})
    elif request.GET["operation"] == "rest":
        return render(request,"calculadora.html",{"resultado":"El resultado es: "+str(int(request.GET["n1"])- int(request.GET["n2"]))})
    elif request.GET["operation"] == "mul":
        return render(request,"calculadora.html",{"resultado":"El resultado es: "+str(int(request.GET["n1"])*int(request.GET["n2"]))})
    elif request.GET["operation"] == "div":
        return render(request,"calculadora.html",{"resultado":"El resultado es: "+str(int(request.GET["n1"])/int(request.GET["n2"]))})