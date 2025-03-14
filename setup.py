import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='imagestore',
    version='3.2.0',
    packages=find_packages(),
    install_requires=[
        'django',
        'six',
        'pillow',
        'sorl-thumbnail',
        'django-autocomplete-light',
        'django-tagging @ git+https://github.com/webtechnika/django-tagging.git',
        'swapper',
    ],
    author='Pavel Zhukov',
    author_email='gelios@gmail.com',
    description='Gallery solution for django projects',
    long_description=README,
    license='GPL',
    keywords='django gallery',
    url='https://github.com/hovel/imagestore',
    include_package_data=True
)
