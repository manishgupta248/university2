from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.core.paginator import Paginator

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm

# Course Views
def course_list_create_update(request, pk=None):
    # Handle course retrieval for editing
    if pk:
        course = get_object_or_404(Course, pk=pk)
    else:
        course = None

     # Handle form submission
    if request.method == 'POST':
        if course:
            form = CourseForm(request.POST, instance=course)
        else:
            form = CourseForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('course_list_create_update')
    else:
        form = CourseForm(instance=course) if course else CourseForm()

    # Retrieve all courses and paginate
    courses = Course.objects.all()
    paginator = Paginator(courses, 10)  # Show 10 courses per page
    page_number = request.GET.get('page')  # Get the current page number from the query string
    page_obj = paginator.get_page(page_number)

    # Render the template with pagination
    return render(request, 'academic/course_list_create_update.html', {
        'form': form,
        'page_obj': page_obj,
        'edit_course': course,
        'courses': courses,
    })

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "academic/course_delete.html"
    success_url = reverse_lazy('course_list_create_update')