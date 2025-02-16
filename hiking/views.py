from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Route, Event, Comment
from .forms import CommentForm, EventForm, RouteForm


def home(request):
    routes = Route.objects.all()
    return render(request, 'hiking/home.html', {'routes': routes})


def route_detail(request, route_id):
    route = Route.objects.get(id=route_id)
    comments = Comment.objects.filter(route=route)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.route = route
            comment.user = request.user
            comment.save()
            return redirect('route_detail', route_id=route_id)
    else:
        form = CommentForm()
    return render(request, 'hiking/route_detail.html', {'route': route, 'comments': comments, 'form': form})

@login_required
def create_event(request, route_id):
    route = Route.objects.get(id=route_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.route = route
            event.organizer = request.user
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'hiking/create_event.html', {'form': form, 'route': route})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # 添加成功后跳转到主页
    else:
        form = RouteForm()
    return render(request, 'hiking/add_route.html', {'form': form})