from import_export import resources
from .models import Course

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        fields = ('name', 'code', 'category', 'type', 'cbcs_category', 'maximum_credit') 
        export_order = ('code', 'name', 'category', 'type', 'cbcs_category', 'maximum_credit') 
        import_id_fields = ('code',)  # Use 'code' as the unique identifier for imports