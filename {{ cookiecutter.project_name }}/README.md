# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

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

## Documentation
Generate documentation
``` shell
$ cd docs
$ make html
```
