from setuptools import setup, find_packages

from django_python3_ldap import __version__


version_str = ".".join(str(n) for n in __version__)
        

setup(
    name = "django-python3-ldap",
    version = version_str,
    license = "BSD",
    description = "Django LDAP user authentication backend for Python 3.",
    author = "Dave Hall",
    author_email = "dave@etianen.com",
    url = "https://github.com/etianen/django-python3-ldap",
    packages = find_packages(),
    install_requires = [
        "django>=1.7",
        "python3-ldap==0.9.5.3",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Django",
    ],
)