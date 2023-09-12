from django.shortcuts import render



def show_main(request):
    context = {
        'application': 'Miracle',
        'name': 'Kevin Ignatius Wijaya',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
