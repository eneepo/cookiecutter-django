# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}
## Secret Key
Generate Secret Key
``` shell
$ python -c """import random; key=''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789%^&*(-_=+)') for i in range(50)]); print('SECRET_KEY=\'{}\''.format(key))""" >> .env
```
Set environment variables from `.env` file
``` shell
$ set -o allexport; source .env; set +o allexport
```

## Asset Management
Assets directory is located at `{{ cookiecutter.project_name }}/{{ cookiecutter.project_slug }}/assets`
with the following structure:

```
assets
  └ dist
  └ source
    └ css
    └ img
    └ js
    └ css
```
You can use gulp to clean, build, watch and serve the static files

``` shell
# Build static files
$ gulp
# Clean static files
$ gulp clean
# Watch for changes and build static files
$ gulp watch
# Watch for changes, build and serve static files
$ gulp serve
```
## Containers
### Docker
Build a single docker image
``` shell
$ docker build -f containers/docker/django/Dockerfile .
```
### Compose

``` shell
$ docker-compose -f containers/compose/development.yml up
```
To force rebuilding the image
``` shell
$ docker-compose -f containers/compose/development.yml up --build
```
Because `COMPOSE_FILE` has been set in the `.env` file you don't need to use `-f`
switch for the production
``` shell
$ docker-compose up --build
```

## Documentation
Generate documentation
``` shell
$ cd docs
$ make html
```
