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

    # some common settings keys to find a path somewhere in the project
    settings_keys = (
        'PROJECT_ROOT',
        'PROJECT_DIR',
        'SITE_ROOT',
        'SITE_DIR',
        'SETTINGS_ROOT',
        'SETTINGS_DIR',
        'ROOT_PATH',
        'GIT_REPO_DIR', # fallback
    )

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        # attempt to find a valid directory in the project
        git_path = None
        for key in self.settings_keys:
            if hasattr(settings, key):
                git_path = getattr(settings, key, None)

        if git_path is None:
            raise Exception("Couldn't find git directory.  Try setting GIT_REPO_DIR.")

        try:
            self.repo = Repo(git_path)
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
