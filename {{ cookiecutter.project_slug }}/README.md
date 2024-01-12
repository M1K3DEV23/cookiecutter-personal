# {{cookiecutter.project_title}}

- **By:** {{cookiecutter.project_author_name}}

- **Contact:** {{cookiecutter.project_author_email}}

## Licence

{% if cookiecutter.open_source_license == 'MIT' %} This project has The MIT License (MIT) Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.project_author_name }}

{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %} Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.project_author_name }} All rights reserved.

{% elif cookiecutter.open_source_license == 'No license file' %} This project has not a license file {% endif %}

## Directories Distribution
