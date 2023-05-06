from django.shortcuts import redirect, render

from reducer.shorter.models import UrlRedirect


def redirecter(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destiny)
