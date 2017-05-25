#from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


# def dashboard(request):
#     return HttpResponse("Dashboard")


def dashboard(request):
    template = loader.get_template('photos/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    return HttpResponse(template.render(None, request))
    # return HttpResponse(template.render(context, request))
