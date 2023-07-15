from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import request, response, HttpResponseRedirect
from .models import News, Comments
from django.urls import reverse_lazy
from welcome.forms import NewsForm, ComentCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    template_name = 'welcome/index.html'
    context_object_name = 'mainpage'

    def get(self, request):
        name = "Hay"
        return render(request, self.template_name, {'hello': name})
    
class NewsDetail(LoginRequiredMixin, generic.ListView):
    template_name = 'welcome/news_detail.html'
    context_object_name = 'news_detail_page'
    success_url = reverse_lazy('welcome:news')

    def get(self, request, pk):
        TheNews = News.objects.get(id=pk)
        TheComments = Comments.objects.filter(topic=TheNews)
        form = ComentCreateForm()
        form.fields['topic'].initial = News.objects.get(id=pk)
        ctx = {
            'news_info': TheNews,
            'news_comments': TheComments,
            'form': form
               }
        return render(request, self.template_name, ctx)
    
    def post(self, request, pk):
        form = ComentCreateForm(request.POST)
        
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        comment = form.save()
        return redirect(self.success_url+str(pk)+'/detail')
    
class NewsView(LoginRequiredMixin, generic.ListView):
    template_name='welcome/news.html'
    context_object_name = 'newspage'

    def get(self, request):
        news = News.objects.all()
        return render(request, self.template_name, {'newss': news})
    
class NewsAdd(LoginRequiredMixin, View):
    template = 'welcome/create_news_form.html'
    success_url = reverse_lazy('welcome:news')

    def get(self, request):
        form = NewsForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)
    
    def post(self, request):
        form = NewsForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        news = form.save()
        return redirect(self.success_url)







class NewsDelete(LoginRequiredMixin, View):
    model = News
    success_url = reverse_lazy('welcome:news')
    template = 'welcome/news_confirm_delete.html'

    def get(self, request, pk):
        news = get_object_or_404(self.model, pk=pk)
        ctx = {'news': news}
        return render(request, self.template, ctx)
    
    def post(self, reuest, pk):
        news = get_object_or_404(self.model, pk=pk)
        news.delete()
        return redirect(self.success_url)

# Create your views here.
