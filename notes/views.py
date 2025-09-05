from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Note
from .forms import NoteForm, SimpleUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = SimpleUserCreationForm()
    return render(request, 'notes/register.html', {'form': form})

from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('note_list')
    else:
        form = AuthenticationForm()
    return render(request, 'notes/login.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('login')

@login_required
def note_list(request):
	notes = Note.objects.filter(user=request.user).order_by('-updated_at')
	return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_create(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			note = form.save(commit=False)
			note.user = request.user
			note.save()
			return redirect('note_list')
	else:
		form = NoteForm()
	return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_edit(request, pk):
	note = get_object_or_404(Note, pk=pk, user=request.user)
	if request.method == 'POST':
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			return redirect('note_list')
	else:
		form = NoteForm(instance=note)
	return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
	note = get_object_or_404(Note, pk=pk, user=request.user)
	if request.method == 'POST':
		note.delete()
		return redirect('note_list')
	return render(request, 'notes/note_confirm_delete.html', {'note': note})

# Create your views here.
