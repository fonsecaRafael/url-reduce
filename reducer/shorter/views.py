from django.shortcuts import redirect, render

from reducer.shorter.models import UrlLog, UrlRedirect


def reports(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    shortened_url = request.build_absolute_uri(f'/{slug}')
    context = {'reduce': url_redirect, 'shortened_url': shortened_url}
    return render(request, 'shorter/report.html', context)


def redirecter(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    UrlLog.objects.create(
        origin=request.META.get('HTTP_REFERER'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        host=request.META.get('HTTP_HOST'),
        ip=request.META.get('REMOTE_ADDR'),
        url_redirect=url_redirect
    )
    return redirect(url_redirect.destiny)
