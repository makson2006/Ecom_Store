from django.shortcuts import render


def cart_summary(request):
    return render(request, 'cart_summary.html', {})

def delete(request):
    pass
def add(request):
    pass
def update(request):
    pass