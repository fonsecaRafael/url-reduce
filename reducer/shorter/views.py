from django.shortcuts import redirect, render


def redirecter(request, slug):
    return redirect('http://google.com')
