from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import Http404

"""
def post_list(request):
    all_post = Post.objects.all().order_by('id')
    paginator = Paginator(all_post, 2, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'home.html', {'page_obj': page_obj})

"""

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['id']
    paginate_by = 2
    paginate_orphans = 0

    def get_context_data(self,*args, **kwargs):
        try:
            return super(PostListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).get_context_data(*args, **kwargs)

