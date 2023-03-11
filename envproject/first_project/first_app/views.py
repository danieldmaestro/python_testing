from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic
# from django.template import loader
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, "first_app/index.html", context=date_dict)

# def index(request):
#      template = loader.get_template('first_app/index.html')
#      context = {}
#      return HttpResponse(template.render(context, request))
