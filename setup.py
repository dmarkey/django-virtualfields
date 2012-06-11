from setuptools import setup

setup(
    name = "django-virtualfields",
    version = "0.0.1",
    author = "David Markey",
    author_email = "david@dmarkey.com",
    description = ("A set of fields for django that can be backed by a single TextField "
                                   " that can be added/removed withoout a DB change"),
    license = "BSD",
    keywords = "django virtualfield",
    url = "http://packages.python.org/django-virtualfields",
    packages=['virtualfields',],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: BSD License",
    ],
)

