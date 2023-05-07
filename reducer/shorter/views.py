from django.shortcuts import redirect, render
from django.db.models.functions import TruncDate
from django.db.models import Count

from reducer.shorter.models import UrlLog, UrlRedirect


def reports(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    shortened_url = request.build_absolute_uri(f'/{slug}')
    redirects_by_date = list(
        UrlRedirect.objects.filter(
            slug=slug
        ).annotate(
            date=TruncDate('logs__created_at')
        ).annotate(
            clicks=Count('date')
        ).order_by('date')
    )

    context = {
        'reduce': url_redirect,
        'shortened_url': shortened_url,
        'redirects_by_date': redirects_by_date,
        'total_clicks': sum(redirect.clicks for redirect in redirects_by_date)
    }
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
