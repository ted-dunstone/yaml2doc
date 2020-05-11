# -*- coding: utf-8 -*-

from setuptools import setup

from yaml2rst import __version__

long_description = "\n\n".join([
    open("README.md").read(),
    ])

setup(
    name="yaml2doc",
    version=__version__,
    description="""A Tool for Documenting YAML Files to md and others""",
    long_description=long_description,
    author="Ted Dunstone & Hartmut Goebel",
    author_email='ted@biometix.com',
    license="GPLv3+",
    packages=['yaml2rst'],
    url="https://github.com/ted-dunstone/yaml2doc/yaml2rst",
    # These are for reference only, pip is not able to download packages
    # from github because the archives do not include the project-name.
    download_url="https://github.com/ted-dunstone/yaml2doc/releases",
    bugtrack_url="https://github.com/ted-dunstone/yaml2doc/issues",
    keywords=['YML', 'YAML',
              'rst', 'reStructuresText',
              'literate programming'],
    entry_points={
        'console_scripts': [
            'yaml2doc = yaml2doc.yaml2doc:run',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Documentation',
    ],
)