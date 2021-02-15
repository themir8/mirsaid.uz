[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/mirsaid-mirzohidov/mirsaid.uz/">
    <img src="./logo.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Mirsaid.uz blog project</h3>

  <p align="center">
    Mirsaid.uz blog project on Django
    <br />
    <a href="https://mirsaiduz.pythonanywhere.com/">View Demo</a>
    ·
    <a href="https://github.com/mirsaid-mirzohidov/mirsaid.uz/issues">Report Bug</a>
    ·
    <a href="https://github.com/mirsaid-mirzohidov/mirsaid.uz/issues">Request Feature</a>
    ·
    <a href="https://github.com/mirsaid-mirzohidov/mirsaid.uz/pulls">Send a Pull Request</a>
  </p>
</p>

### Tech
Requirements:
 * [Python] +3.5 - Python object oriented programming language

We use:

* [Django] - is a high-level Python Web framework


## Installation

### Project

```sh
$ mkdir myproject && cd myproject
$ git clone https://github.com/mirsaid-mirzohidov/mirsaid.uz.git .
$ virtualenv -p /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```


### Run
```sh
$ python manage.py runserver
```
or
```sh
$ make run
```

### View
Api http://localhost:8000/


[Python]: <https://www.python.org/>
[Django]: <https://www.djangoproject.com/>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/mirsaid-mirzohidov/mirsaid.uz?style=for-the-badge
[forks-url]: https://github.com/mirsaid-mirzohidov/mirsaid.uz/network/members
[stars-shield]: https://img.shields.io/github/stars/mirsaid-mirzohidov/mirsaid.uz?style=for-the-badge
[stars-url]: https://github.com/mirsaid-mirzohidov/mirsaid.uz/stargazers
[issues-shield]: https://img.shields.io/github/issues/mirsaid-mirzohidov/mirsaid.uz?style=for-the-badge
[issues-url]: https://github.com/mirsaid-mirzohidov/mirsaid.uz/issues
