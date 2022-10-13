from django_jinja import library


@library.filter
def add_class(field, css_class_name):
    """
    Filter to add custom class in form field.
    Usage: {{ field|add_class('class_name') }}.
    """
    return field.as_widget(attrs={'class': css_class_name})
