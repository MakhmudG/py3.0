from django.shortcuts import render

# Create your views here.
from django.views import View


class MainViev(View):

    def get(self, request):
        return render(request, 'main.html')


class DepartureViev(View):

    def get(self, request, departure):
        return render(request, 'departure.html')


class TourViev(View):

    def get(self, request, id):
        context = {}
        return render(request, 'tour.html', context=context)