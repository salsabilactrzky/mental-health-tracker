from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275664',
        'name': 'Salsabila Caturizky Farindarmawan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)