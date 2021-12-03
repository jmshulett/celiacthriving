from django.shortcuts import render, get_object_or_404
from .models import ShopTips

def tips_list(request):
    #tip = None
    tips = ShopTips.objects.all()
    return render(request,
                  'tips/list.html',
                  {'tip': ShopTips,
                   'tips': tips})

def tips_detail(request, id, slug):
    tips = get_object_or_404(ShopTips,
                                id=id,
                                slug=slug)
    return render(request,
                  'tips/detail.html',
                  {'tips': tips})