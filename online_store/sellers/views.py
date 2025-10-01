from .models import SellerProfile
from django.shortcuts import render, get_object_or_404

def seller_profile_detail(request, id):
    seller = get_object_or_404(SellerProfile, id=id)
    return render(request, 'sellers/seller_detail.html', {'seller': seller})
