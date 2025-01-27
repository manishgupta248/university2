from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.core.paginator import Paginator
from .resources import CourseResource
from tablib import Dataset
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Course Views

@login_required
def course_list_create_update(request, pk=None):
    # Handle course retrieval for editing
    if pk:
        course = get_object_or_404(Course, pk=pk)
    else:
        course = None

   # Handle form submission
    if request.method == 'POST':
        if 'import_file' in request.FILES:
            # Handle import
            import_file = request.FILES['import_file']
            if import_file.name.endswith('.xlsx') or import_file.name.endswith('.csv'):
                dataset = Dataset()
                imported_data = dataset.load(import_file.read(), format=import_file.name.split('.')[-1])
                resource = CourseResource()
                result = resource.import_data(dataset, dry_run=True)  # Test the import
                if not result.has_errors():
                    resource.import_data(dataset, dry_run=False)  # Actually import now
            return redirect('course_list_create_update')
        else:
            form = CourseForm(request.POST, instance=course)
            if form.is_valid():
                form.save()
                if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                    return JsonResponse({'status': 'success'})
                return redirect('course_list_create_update')  # Redirect to the same view after saving
            else:
                if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                    return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = CourseForm(instance=course)

    # Handle search query
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by', 'name')  # Default sort by name
    if query:
        courses = Course.objects.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query) |
            Q(category__icontains=query) |
            Q(type__icontains=query) |
            Q(cbcs_category__icontains=query)
        ).order_by(sort_by)
    else:
        courses = Course.objects.all().order_by(sort_by)
    # Retrieve all courses and paginate
    
    paginator = Paginator(courses, 10)  # Show 10 courses per page
    page_number = request.GET.get('page')  # Get the current page number from the query string
    page_obj = paginator.get_page(page_number)

    # Render the template with pagination
    return render(request, 'academic/course_list_create_update.html', {
        'form': form,
        'page_obj': page_obj,
        'edit_course': course,
        'query': query,
        'sort_by': sort_by
    })


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "academic/course_delete.html"
    success_url = reverse_lazy('course_list_create_update')

def course_import(request):
    if request.method == 'POST' and 'import_file' in request.FILES:
        import_file = request.FILES['import_file']
        if import_file.name.endswith('.xlsx') or import_file.name.endswith('.csv'):
            dataset = Dataset()
            imported_data = dataset.load(import_file.read(), format=import_file.name.split('.')[-1])
            resource = CourseResource()
            result = resource.import_data(dataset, dry_run=True)  # Test the import
            if not result.has_errors():
                resource.import_data(dataset, dry_run=False)  # Actually import now
    return redirect('course_list_create_update')

def course_export(request):
    resource = CourseResource()
    dataset = resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="courses.xlsx"'
    return response

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'academic/course_detail.html', {'course':course})