import json
import os
import re
from string import rstrip
from urlparse import urljoin

from django.http import HttpResponseRedirect
from django.shortcuts import render

from cartoview.app_manager.models import *
from forms import NewForm
from django.conf import settings
from .models import *

dirname, filename = os.path.split(os.path.abspath(__file__))
APP_NAME = 'cartoview_basic_viewer'
VIEW_TPL = "%s/index.html" % APP_NAME
NEW_EDIT_TPL = "%s/new.html" % APP_NAME

HELP_TPL = "%s/help.htm" % APP_NAME
CONFIG_TPL = "%s/config.js" % APP_NAME

# Regular expression for comments
comment_re = re.compile(
        '(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?',
        re.DOTALL | re.MULTILINE
)


def remove_json_comments(json_string):
    """ Parse a JSON file
        First remove comments and then use the json module package
        Comments look like :
            // ...
        or
            /*
            ...
            */
    """

    content = json_string  # ''.join(json_string)

    ## Looking for comments
    match = comment_re.search(content)
    while match:
        # single line comment
        content = content[:match.start()] + content[match.end():]
        match = comment_re.search(content)

    # Return json
    return content


def view(request, resource_id):
    basicviewer_obj = BasicViewer.objects.get(pk=resource_id)
    config_json = json.loads(remove_json_comments(basicviewer_obj.config))
    config_json['webmap'] = str(basicviewer_obj.web_map_id)
    config_json['title'] = basicviewer_obj.title
    config_json['description'] = basicviewer_obj.abstract
    config_json['sharinghost'] = rstrip(str(urljoin(settings.SITEURL, reverse("arcportal_home"))), '/')

    context = {'config_json': json.dumps(config_json)}
    return render(request, VIEW_TPL, context)


def save(request, map_form):
    if map_form.is_valid():
        basicviewer_obj = map_form.save(commit=False)
        basicviewer_obj.app = App.objects.get(name=APP_NAME)
        basicviewer_obj.owner = request.user
        basicviewer_obj.save()
        # redirect to app instance details after saving instance.
        return HttpResponseRedirect(reverse('appinstance_detail', kwargs={'appinstanceid': basicviewer_obj.pk}))
    else:
        context = {'map_form': map_form}
        return render(request, NEW_EDIT_TPL, context)


#
def new(request):
    if request.method == 'POST':
        map_form = NewForm(request.POST, prefix='map_form')
        return save(request, map_form)

    else:
        context = {'map_form': NewForm(prefix='map_form')}
        return render(request, NEW_EDIT_TPL, context)


def edit(request, resource_id):
    app_instance_obj = BasicViewer.objects.get(pk=resource_id)
    if request.method == 'POST':
        map_form = NewForm(request.POST, prefix='map_form', instance=app_instance_obj)
        return save(request, map_form)

    else:
        context = {'map_form': NewForm(prefix='map_form', instance=app_instance_obj)}
        return render(request, NEW_EDIT_TPL, context)
