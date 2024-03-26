from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib import messages
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
            
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)

# Create your views here.
'''def blog(request):
    #return HttpResponse("<h1>Wellcome</h1>")
    data = {
        "posts":Post.objects.all()
    }
    return render(request,'blog.html',data)'''

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView,LoginRequiredMixin):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        messages.success(self.request,"Post Created Successfully")
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    login_url = '/login/'
    redirect_field_name = 'login'
    
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'content']  

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,'Post Updated Successfully!!!')
        return super().form_valid(form)  

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False   
     
class PostDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    login_url = '/login/'
    redirect_field_name = 'login'

    model = Post
    template_name = 'post_delete.html'
    success_url = '/'

    def test_func(self):
        messages.success(self.request,'Post Deleted Successfully')
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
