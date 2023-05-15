from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


@login_required
def paying(request):

    return render(request, 'payment/pay.html', { })
