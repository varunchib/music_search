from django.shortcuts import render
import requests

def search_form(request):
    return render(request, 'music/search_form.html')

def search_results(request):
    search_term = request.GET.get('search_term')
    url = f'https://itunes.apple.com/search?term={search_term}&media=music&entity=album'
    response = requests.get(url)
    results = response.json()['results']
    context = {'results': results}
    return render(request, 'music/search_results.html', context)
