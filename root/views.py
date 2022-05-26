from django.views.generic import (
    View,
)
from django.shortcuts import render


class LandingPage(View):
    http_method_names = [
        "get",
        "head",
        "options",
    ]

    def get(self,request):
        return render(
            request,
            'root/landing-page.html'
        )



