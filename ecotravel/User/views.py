from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,View


class DestinationView(TemplateView):
    def get(self,request):
        return render(request,"index.html")