from django.shortcuts import render
from .forms import ExampleForm

# Create your views here.


def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'form': form})  # Успешный ответ
        else:
            return render(request, 'form_page.html', {'form': form})  # Ответ с ошибками
    else:
        form = ExampleForm()
    return render(request, 'form_page.html', {'form': form})
