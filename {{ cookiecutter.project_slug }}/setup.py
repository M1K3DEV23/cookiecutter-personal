import os

from setuptools import find_packages, setup


def readme() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return open(os.path.join(os.path.dirname(__file__), "README.md")).read()


setup(
    name="{{ cookiecutter.project_slug }}_packages",
    version="1.0",
    author='{{ cookiecutter.project_author_name.replace("\'", "\\\'") }}',
    author_email="{{ cookiecutter.project_author_email }}",
    description="{{ cookiecutter.project_description }}",
    python_requires=">=3",
    license='{% if cookiecutter.open_source_license == "MIT" %}MIT{% elif cookiecutter.open_source_license == "BSD-3-Clause" %}BSD-3{% endif %}',
    url="",
    packages=find_packages(),
    long_description=readme(),
)
