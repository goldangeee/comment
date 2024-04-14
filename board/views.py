from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from .models import Item
from django.urls import reverse_lazy
from .forms import CommentForm
from django.http import HttpResponse

class ItemLV(ListView):
    model = Item    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = 'Tiger'
        return context    

class ItemDV(DetailView):
    model = Item    

class ItemCV(CreateView):
    model = Item
    success_url = reverse_lazy('spring:index')
    fields = ['title','content']

def content_comment(request,pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.save()
        elif request.method == "GET":
            form = CommentForm()
        return render(request, 'board/item_detail.html',{'object':item,'form':form})
    
class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('spring:index')

def itemLV(request):
    object = Item.objects.all()
    name = "Lion"
    context = {
        'object_list' : object,
        'name' : name
    }
    return render(request=request,template_name='board/item_list.html',context = context)

def test(request):
    return HttpResponse("요청 잘 받았어")

def test1(request,pk):
    return HttpResponse(f"tes1 pk : {pk} 이야")