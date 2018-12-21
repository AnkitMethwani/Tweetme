from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from tweets.forms import TweetModelForm
from .models import Tweet
# Create your views here.

from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = reverse_lazy("detail")


def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {
        "form": form
    }
    return render(request, 'tweets/create_view.html', context)


class TweetDetailView(DetailView):
    pass
    # template_name = "tweets/detail_view.html"
    # queryset = Tweet.objects.all()
    #
    # def get_object(self,id):
    #     return Tweet.objects.get(id=id)


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("create")
        return context


def tweet_detail_view(request, pk=None):  # pk == id
    # obj = Tweet.objects.get(pk=pk) # GET from database
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = reverse_lazy("list")


# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id) # GET from database
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, "tweets/detail_view.html", context)
#
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy("list")
