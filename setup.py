import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='git_branch_panel',
    version='0.1',
    packages=['git_branch_panel'],
    include_package_data=True,
    license='BSD License',
    description='A Django Debug Toolbar panel to display the current git branch',
    long_description=README,
    url='http://github.com/rantecki/git-branch-debug-panel',
    author='Richard Antecki',
    author_email='richard@antecki.id.au',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
