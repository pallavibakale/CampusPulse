from typing import Any
from django.views import generic
from django.urls import reverse
from ..models import Category

class CategoryListView(generic.ListView):
    model = Category
    
class CategoryDetailView(generic.DetailView):
    model = Category
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context["category"].type = "Category"
        context["category"].events = context["category"].event_set.all()
        
        return context
    
class CategoryCreateView(generic.CreateView):
    model = Category
    fields = "__all__"
    
    def get_success_url(self) -> str:
        return reverse('category-list')
    
class CategoryUpdateView(generic.UpdateView):
    model = Category
    
class CategoryDeleteView(generic.DeleteView):
    model = Category