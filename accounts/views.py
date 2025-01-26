from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm  # Import your UserUpdateForm (create this next)
from .models import CustomUser

# Create your views here.
def user_detail(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'account/user_detail.html', {'user': user})

@login_required
def user_update(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'account/user_update.html', {'form': form})