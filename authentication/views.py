from django.shortcuts import render, redirect
from django.urls import reverse


def first_page(request):
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))

    context = {}
    return render(request, "first_page.html", context=context)
