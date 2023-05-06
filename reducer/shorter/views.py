from django.shortcuts import redirect, render

from reducer.shorter.models import UrlRedirect


def reports(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    shortened_url = request.build_absolute_uri(f'/{slug}')
    context = {'reduce': url_redirect, 'shortened_url': shortened_url}
    return render(request, 'shorter/report.html', context)


def redirecter(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destiny)
