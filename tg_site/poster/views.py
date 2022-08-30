from django.shortcuts import render
from .channel_lister import *
from .models import Channel

def main_page(request):
    channels=Channel.objects.all().values_list('name', flat=True)
    print(channels)
    context = {
        "channel_ids":channels
    }
    return render(template_name='poster/index.html', context=context, request=request)

