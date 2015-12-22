from django import forms
from codemirror import *

from cartoview.app_manager.forms import AppInstanceForm
from models import BasicViewer
from config import config_template


class NewForm(AppInstanceForm):
    class Meta(AppInstanceForm.Meta):
        model = BasicViewer
        fields = AppInstanceForm.Meta.fields + ['config', 'web_map_id']

    web_map_id = forms.CharField(widget=forms.HiddenInput)
    config = CodeMirrorFormField(initial=config_template)
