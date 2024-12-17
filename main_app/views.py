from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Reflection
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ResponseForm
from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipRequest, Block
from django.db.models import Q

# Create your views here.
def about(request):
    return render(request, 'about.html')

@login_required
def reflections_index(request):
    reflections = Reflection.objects.filter(user=request.user)
    return render(request, 'reflections/index.html', {'reflections': reflections})

@login_required
def reflection_detail(request, reflection_id):
    reflection = Reflection.objects.get(id=reflection_id)
    response_form = ResponseForm()
    return render(request, 'reflections/detail.html', {'reflection': reflection, 'response_form': response_form})

class ReflectionCreate(LoginRequiredMixin, CreateView):
    model = Reflection
    fields = ['name', 'description', 'media', 'date']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReflectionUpdate(LoginRequiredMixin, UpdateView):
    model=Reflection
    fields='__all__'

class ReflectionDelete(LoginRequiredMixin, DeleteView):
    model=Reflection
    success_url='/reflections/'

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reflections_index)
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def add_response(request, reflection_id):
    form = ResponseForm(request.POST)
    if form.is_valid():
        new_response = form.save(commit=False)
        new_response.reflection_id = reflection_id
        new_response.user = request.user
        new_response.save()
    return redirect('reflection-detail', reflection_id=reflection_id)

# def index_friends(request):
#     friends = Friend.objects.friends(request.user)
#     pending_requests = FriendshipRequest.objects.filter(to_user=request.user)
#     search_results = []
#     query = None

#     if request.method == 'GET':
#         query = request.GET.get('search', '').strip()
#         if query:
#             search_results = User.objects.filter(
#                 Q(username__icontains=query)
#             ).exclude(id=request.user.id)

#     if request.method == 'POST' and 'send_request' in request.POST:
#         recipient_id = request.POST.get('recipient_id')
#         recipient = get_object_or_404(User, id=recipient_id)
#         Friend.objects.add_friend(
#             request.user,
#             recipient,
#             message='Hey, lets connect!'
#         )
#         return redirect('index-friends')

#     return render(request, 'friends/index.html', {
#         'friends': friends,
#         'pending_requests': pending_requests,
#         'search_results': search_results,
#         'query': query,
#     })
# 
# # Reject the friend request
# def reject_request(request, request_id):
#     friendship_request = get_object_or_404(FriendshipRequest, id=request_id, to_user=request.user)
#     friendship_request.delete()
#     return redirect('index_friends')