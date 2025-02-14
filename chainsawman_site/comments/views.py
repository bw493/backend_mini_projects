from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CommentForm
from .models import Comment

def comment_view(request):
    """
    Handle GET and POST requests for creating and viewing comments.
    """
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been submitted.')
            return redirect('comment_view')  # Redirect back to the same page
        else:
            messages.error(request, 'There was an error submitting your comment.')
    else:
        form = CommentForm()

    # Retrieve and sort comments (latest first)
    comments = Comment.objects.all().order_by('-created_at')
    
    context = {
        'form': form,
        'comments': comments,
    }
    return render(request, 'comments/comment_form.html', context)