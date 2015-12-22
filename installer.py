from django.contrib.contenttypes.models import ContentType

info = {
    "title": "ESRI Basic Viewer",
    "description": ''' Basic Viewer is a configurable application template used to display a web map with a specified
                        set of commonly used tools and options.''',
    "author": 'Cartologic',
    "tags": ['Maps'],
    "licence": 'BSD',
    "author_website": "http://www.cartologic.com",
    "single_instance": False
}


def install():
    pass


def uninstall():
    ContentType.objects.filter(app_label="cartoview_basic_viewer").delete();
