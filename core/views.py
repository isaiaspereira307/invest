from django.shortcuts import render, redirect
from core.models import Acao, AcaoForm
from django.views.generic import FormView, UpdateView, ListView
from django.core.paginator import Paginator

def index(request):
    return render(request, 'core/index.html')


class AcaoCreate(FormView):
    model = Acao
    template_name = 'core/form.html'
    form_class = AcaoForm
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = AcaoForm(data=request.POST)
            if form.is_valid():
                form.save()
                form.cleaned_data
                form = AcaoForm()
                return render(request, 'core/form.html', {'form': form})
        return render(request, 'core/form.html', {'form': form})


class AcaoUpdate(UpdateView):
    model = Acao
    template_name = 'core/form.html'
    form_class = AcaoForm

def deletar(request, pk):
    post = Acao.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'core/delete.html', {'post': post})

class Index(ListView):
    def get(self, request, *args, **kwargs):
        posts = Acao.objects.all()
        search = request.GET.get('search')
        if search:
            posts = Acao.objects.filter(acao__icontains=search)
        context = {'posts':posts}
        return render(request, 'core/index.html', context)  
