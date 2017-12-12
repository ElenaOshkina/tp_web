from django.http import HttpResponse


def index(request):
    price_lte="empty"
    if request.method == 'GET':
        price_lte = request.GET['price_lte']
    elif request.method == 'POST':
        #price_lte = request.POST['price_lte']
        for key in request.POST:
            print(key)
            value = request.POST[key]
            print(value)
    #password=request.POST['num']
    message="Hello, world. You're at the ask index TEST.\n"+"GET parametrs:"+price_lte+" Post_Parametrs:"
    return HttpResponse(message)