from django.http import HttpResponse
from django.template import loader

# Create your views here.
def ourteam(request):
    template = loader.get_template('ourteam.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
