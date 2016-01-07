CARTOVIEW_VERSION = (1, 0, 0, 'final', 0)  # major.minor.build.release (PEP standard)

VERSION = (1, 0, 0, 'final', 0)  # major.minor.build.release (PEP standard)


# Note: cartoview does not check for version.

def get_cartoview_version(*args, **kwargs):  # carto compatible version
    # Don't litter django/__init__.py with all the get_version stuff.
    # Only import if it's actually called.
    from django.utils.version import get_version
    return get_version(version=CARTOVIEW_VERSION)


def get_version(*args, **kwargs):
    # Don't litter django/__init__.py with all the get_version stuff.
    # Only import if it's actually called.
    from django.utils.version import get_version
    return get_version(version=VERSION)


"""
Define actions urls that should be appeared in apps list page.This urls will be added beside explorer buttons.
There are three predefined groups of users to assign them actions{ admin, logged_in, anonymous}, groups names are self
explanatory.
urls dict must be as follows
urls_dict = {
    'admin':{'<url_name>':'<label>','<another_url_name>':'<another_label>'},
    'logged_in:{'<url_name>':'<label>','<another_url_name>':'<another_label>'},
    'anonymous:{'<url_name>':'<label>','<another_url_name>':'<another_label>'},
}
"""

urls_dict = {
    'admin': {'cartoview_basic_viewer.new': 'Create new'},
}
