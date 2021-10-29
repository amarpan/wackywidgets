from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Widget
from .forms import WidgetForm

# Add the following import
from django.http import HttpResponse

# class WidgetCreate(CreateView):
#     model = Widget
#     fields = '__all__'
#     success_url = '/'

# class WidgetDelete(DeleteView):
#     model = Widget
#     success_url = '/'

# Define the home view
def widgets_index(request):
  widgets = Widget.objects.all()
  widget_form = WidgetForm()
  return render(request, 'widgets/index.html', {
      'widgets': widgets, 'widget_form': widget_form
  })

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        # new_feeding.cat_id = cat_id
        new_widget.save()
    return redirect('index')

def delete_widget(request, widget_id):
    Widget.objects.filter(id=widget_id).delete()
    return redirect('index')

# def add_widget(request, widget_id):
#       # create the ModelForm using the data in request.POST
#     form = WidgetForm(request.POST)
#     # validate the form
#     if form.is_valid():
#         # don't save the form to the db until it
#         # has the cat_id assigned
#         new_feeding = form.save(commit=False)
#         new_feeding.cat_id = cat_id
#         new_feeding.save()
#     return redirect('detail', cat_id=cat_id)

# Create your views here.
