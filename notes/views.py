from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Note, Subject
from .forms import NoteForm, SimpleUserCreationForm, SubjectForm

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

from django.core.paginator import Paginator

@login_required
def note_list(request):
    subject_id = request.GET.get('subject')
    subjects = Subject.objects.filter(user=request.user)
    
    if subject_id:
        notes = Note.objects.filter(user=request.user, subject_id=subject_id).order_by('-created_at')
        current_subject = get_object_or_404(Subject, id=subject_id, user=request.user)
    else:
        notes = Note.objects.filter(user=request.user).order_by('-created_at')
        current_subject = None
    
    # Set up pagination
    paginator = Paginator(notes, 10)  # Show 10 notes per page
    page_number = request.GET.get('page', 1)
    notes = paginator.get_page(page_number)
    
    return render(request, 'notes/note_list.html', {
        'notes': notes,
        'subjects': subjects,
        'current_subject': current_subject,
        'subjects': subjects,
        'current_subject': current_subject
    })

@login_required
def note_create(request):
	subject_id = request.GET.get('subject')
	initial = {}
	current_subject = None
	
	if subject_id:
		current_subject = get_object_or_404(Subject, id=subject_id, user=request.user)
		initial = {'subject': current_subject}
		
	if request.method == 'POST':
		form = NoteForm(request.POST, user=request.user)
		if form.is_valid():
			note = form.save(commit=False)
			note.user = request.user
			
			# If we're creating from a subject page and no subject is selected,
			# use the current subject from the URL
			if not note.subject and current_subject:
				note.subject = current_subject
				
			note.save()
			if note.subject:
				return redirect('subject_detail', pk=note.subject.id)
			return redirect('note_list')
	else:
		form = NoteForm(user=request.user, initial=initial)
	
	context = {
		'form': form,
		'current_subject': current_subject
	}
	
	return render(request, 'notes/note_form.html', context)

@login_required
def subject_list(request):
	subjects = Subject.objects.filter(user=request.user)
	
	# Create a dictionary with note counts and preview notes for each subject
	subject_note_counts = {}
	subject_preview_notes = {}
	
	for subject in subjects:
		notes = Note.objects.filter(user=request.user, subject=subject).order_by('-updated_at')
		subject_note_counts[subject.id] = notes.count()
		subject_preview_notes[subject.id] = notes[:3]  # Get up to 3 notes for preview
	
	return render(request, 'notes/subject_list.html', {
		'subjects': subjects,
		'subject_note_counts': subject_note_counts,
		'subject_preview_notes': subject_preview_notes
	})

@login_required
def subject_detail(request, pk):
	subject = get_object_or_404(Subject, pk=pk, user=request.user)
	notes = Note.objects.filter(user=request.user, subject=subject).order_by('-updated_at')
	
	return render(request, 'notes/subject_detail.html', {
		'subject': subject,
		'notes': notes
	})

@login_required
def subject_create(request):
    try:
        if request.method == 'POST':
            form = SubjectForm(request.POST)
            if form.is_valid():
                subject = form.save(commit=False)
                subject.user = request.user
                subject.save()
                return redirect('subject_list')
        else:
            form = SubjectForm()
        return render(request, 'notes/subject_form.html', {'form': form})
    except Exception as e:
        # Add error to form
        form = SubjectForm(request.POST if request.method == 'POST' else None)
        form.add_error(None, f"An error occurred: {str(e)}")
        return render(request, 'notes/subject_form.html', {'form': form})

@login_required
def subject_edit(request, pk):
	subject = get_object_or_404(Subject, pk=pk, user=request.user)
	if request.method == 'POST':
		form = SubjectForm(request.POST, instance=subject)
		if form.is_valid():
			form.save()
			return redirect('subject_list')
	else:
		form = SubjectForm(instance=subject)
	return render(request, 'notes/subject_form.html', {'form': form})

@login_required
def subject_delete(request, pk):
	subject = get_object_or_404(Subject, pk=pk, user=request.user)
	
	if request.method == 'POST':
		# Get all notes associated with this subject
		associated_notes = Note.objects.filter(subject=subject)
		
		# Update the notes to have no subject (instead of deleting them)
		for note in associated_notes:
			note.subject = None
			note.save()
			
		# Now delete the subject
		subject.delete()
		return redirect('subject_list')
		
	return render(request, 'notes/subject_confirm_delete.html', {'subject': subject})

@login_required
def note_edit(request, pk):
	note = get_object_or_404(Note, pk=pk, user=request.user)
	if request.method == 'POST':
		form = NoteForm(request.POST, instance=note, user=request.user)
		if form.is_valid():
			updated_note = form.save()
			if updated_note.subject:
				return redirect('subject_detail', pk=updated_note.subject.id)
			return redirect('note_list')
	else:
		form = NoteForm(instance=note, user=request.user)
	return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
	note = get_object_or_404(Note, pk=pk, user=request.user)
	subject = note.subject  # Store the subject before deleting the note
	
	if request.method == 'POST':
		note.delete()
		if subject:
			# If the note had a subject, redirect back to that subject's detail page
			return redirect('subject_detail', pk=subject.id)
		else:
			# Otherwise go to the main note list
			return redirect('note_list')
			
	return render(request, 'notes/note_confirm_delete.html', {'note': note})

# Create your views here.
