from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import URLForm
from .models import LongToShort
from django.contrib.gis.geoip2 import GeoIP2
import geoip2.database
import secrets
from django.template import  RequestContext

def home(request):
    return HttpResponse('Hello.')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def shorten(request):
    if request.method == 'POST':
        userform = URLForm(request.POST)
        ip_longurl = userform.data['longurl']
        ip_customname = userform.data['custom_name']
        if ip_customname == '':
            gen_shorturl = secrets.token_hex(3)
            final_url = gen_shorturl
            g = GeoIP2('./geoip')
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            reader = geoip2.database.Reader('./geoip/GeoLite2-City.mmdb')
            response = reader.city(ip)
            obj = LongToShort(longurl = ip_longurl, shorturl = final_url, city = response.city.name, long = response.location.longitude, lat = response.location.latitude, ip_address = ip)
            obj.save()
        else:
            entries = LongToShort.objects.filter(shorturl = ip_customname)
            if len(entries) == 0:
                final_url = ip_customname
                g = GeoIP2('./geoip')
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                reader = geoip2.database.Reader('./geoip/GeoLite2-City.mmdb')
                response = reader.city(ip)
                obj = LongToShort(longurl = ip_longurl, shorturl = final_url, city = response.city.name, long = response.location.longitude, lat = response.location.latitude, ip_address = ip)
                obj.save()
            else:
                return HttpResponse('Invalid link.')

        return HttpResponse('Your shorturl is ' + 'https://abhishek-shortenurl.herokuapp.com/redirect/' + final_url)
    else:
        myform = URLForm()
        return render(request, 'form.html', {'form': myform})

def redirect_url(request, link):
    try:
        obj = LongToShort.objects.get(shorturl = link)
        req_longurl = obj.longurl
        obj.visit_count += 1
        obj.save()
        return redirect(req_longurl)
    except Exception as e:
        print(e)
        return HttpResponse('Invalid short url.')

def get_analytics(request):
    rows = LongToShort.objects.all(),
    return render(request, 'analytics.html', {'data': rows})

