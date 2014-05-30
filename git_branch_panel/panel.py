import sys

import django
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from debug_toolbar.panels import DebugPanel

try:
    from git import Repo
except ImportError:
    raise ImportError("Ensure GitPython is installed")

class GitBranchPanel(DebugPanel):
    """
    Panel that displays basic information about the current git branch
    """
    name = 'GitBranch'
    has_content = True
    repo = None

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        try:
            self.repo = Repo(settings.SITE_ROOT)
        except:
            self.repo = None


    def nav_title(self):
        return _('Current Git Branch')

    def nav_subtitle(self):
        if self.repo:
            return '%s' % self.repo.active_branch
        else:
            return 'Not a valid git repository.'

    def url(self):
        return ''
    
    def title(self):
        return _('Current Git Branch')

    def content(self):
        return self.nav_subtitle()
