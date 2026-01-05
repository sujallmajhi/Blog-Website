from .models import Category


'''context processor to get categories for all templates defined in settings.py middleware'''
def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)