from django.shortcuts import render

    def show_maps_html(request):
  return render(request, 'show_maps.html')

def show_maps_css(request):
  return render(request, 'show_maps.css')

def show_maps_js(request):
  return render(request, 'show_maps.js')