[![Build Status](https://travis-ci.org/tiangolo/uvicorn-gunicorn-fastapi-docker.svg?branch=master)](https://travis-ci.org/tiangolo/uvicorn-gunicorn-fastapi-docker)


## Supported tags and respective `Dockerfile` links

* [`python3.7`, `latest` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/blob/master/python3.7/Dockerfile)
* [`python3.6` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/blob/master/python3.6/Dockerfile)
* [`python3.6-alpine3.8` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/blob/master/python3.6-alpine3.8/Dockerfile)
* [`python3.7-alpine3.8` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/blob/master/python3.7-alpine3.8/Dockerfile)


# uvicorn-gunicorn-fastapi

[**Docker**](https://www.docker.com/) image with [**Uvicorn**](https://www.uvicorn.org/) managed by [**Gunicorn**](https://gunicorn.org/) for high-performance [**FastAPI**](https://fastapi.tiangolo.com/) web applications in **[Python](https://www.python.org/) 3.7** and **3.6** with performance auto-tuning. Optionally with Alpine Linux.

**GitHub repo**: <https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker>

**Docker Hub image**: <https://hub.docker.com/r/tiangolo/uvicorn-fastapi-gunicorn/>


## Description

**FastAPI** has shown to be a Python web framework with [one of the best performances, as measured by third-party benchmarks](https://www.techempower.com/benchmarks/#section=test&runid=a979de55-980d-4721-a46f-77298b3f3923&hw=ph&test=fortune&l=zijzen-7), thanks to being based on and powered by [**Starlette**](https://www.starlette.io/).

The achievable performance is on par with (and in many cases superior to) **Go** and **Node.js** frameworks.

This image has an "auto-tuning" mechanism included, so that you can just add your code and get that same **high performance** automatically. And without making sacrifices.


## Technical Details


### Uvicorn

**Uvicorn** is a lightning-fast "ASGI" server.

It runs asynchronous Python web code in a single process.


### Gunicorn

You can use **Gunicorn** to manage Uvicorn and run multiple of these concurrent processes.

That way, you get the best of concurrency and parallelism.


### FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+.

The key features are:

* **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic).
* **Fast to code**: Increase the speed to develop features by about 300% to 500% *.
* **Less bugs**: Reduce about 40% of human (developer) induced errors. *
* **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
* **Easy**: Designed to be easy to use and learn. Less time reading docs.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Less bugs.
* **Robust**: Get production-ready code. With automatic interactive documentation.
* **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" target="_blank">OpenAPI</a> (previously known as Swagger) and <a href="http://json-schema.org/" target="_blank">JSON Schema</a>.

<small>* estimation based on tests on an internal development team, building production applications.</small>


### `tiangolo/uvicorn-gunicorn-fastapi`

This image will set a sensible configuration based on the server it is running on (the amount of CPU cores available) without making sacrifices.

It has sensible defaults, but you can configure it with environment variables or override the configuration files.

There is also an Alpine version. If you want it, use one of the Alpine tags from above.


### `tiangolo/uvicorn-gunicorn`

This image (`tiangolo/uvicorn-gunicorn-fastapi`) is based on [**tiangolo/uvicorn-gunicorn**](https://github.com/tiangolo/uvicorn-gunicorn-docker).

That image is what actually does all the work.

This image just installs FastAPI and has the documentation specifically targeted at FastAPI.

If you feel confident about your knowledge of Uvicorn, Gunicorn and ASGI, you can use that image directly.


### `tiangolo/uvicorn-gunicorn-starlette`

There is a sibling Docker image: [**tiangolo/uvicorn-gunicorn-starlette**](https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker)

If you are creating a new [**Starlette**](https://www.starlette.io/) web application and you want to discard all the additional features from FastAPI you should use [**tiangolo/uvicorn-gunicorn-starlette**](https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker) instead.

**Note**: FastAPI is based on Starlette and adds several features on top of it. Useful for APIs and other cases: data validation, data conversion, documentation with OpenAPI, dependency injection, security/authentication and others.


## How to use

* You don't need to clone the GitHub repo. You can use this image as a base image for other images, using this in your `Dockerfile`:

```Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
```

It will expect a file at `/app/app/main.py`.

Or otherwise a file at `/app/main.py`.

And will expect it to contain a variable `app` with your FastAPI application.

Then you can build your image from the directory that has your `Dockerfile`, e.g:

```bash
docker build -t myimage ./
```

## Quick Start

### Build your Image

* Go to your project directory.
* Create a `Dockerfile` with:

```Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
```

* Create an `app` directory and enter in it.
* Create a `main.py` file with:

```Python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

* You should now have a directory structure like:

```
.
├── app
│   └── main.py
└── Dockerfile
```

* Go to the project directory (in where your `Dockerfile` is, containing your `app` directory).
* Build your FastAPI image:

```bash
docker build -t myimage .
```

* Run a container based on your image:

```bash
docker run -d --name mycontainer -p 80:80 myimage
```

Now you have an optimized FastAPI server in a Docker container. Auto-tuned for your current server (and number of CPU cores).

### Check it

You should be able to check it in your Docker container's URL, for example: http://192.168.99.100/items/5?q=somequery or http://127.0.0.1/items/5?q=somequery (or equivalent, using your Docker host).

You will see something like:

```JSON
{"item_id": 5, "q": "somequery"}
```

### Interactive API docs

Now you can go to <a href="http://192.168.99.100/docs" target="_blank">http://192.168.99.100/docs</a> or <a href="http://127.0.0.1/docs" target="_blank">http://127.0.0.1/docs</a> (or equivalent, using your Docker host).

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)


### Alternative API docs

And you can also go to <a href="http://192.168.99.100/redoc" target="_blank">http://192.168.99.100/redoc</a> or <a href="http://127.0.0.1/redoc" target="_blank">http://127.0.0.1/redoc</a>(or equivalent, using your Docker host).

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)


## Advanced usage

### Environment variables

These are the environment variables that you can set in the container to configure it and their default values:


#### `MODULE_NAME`

The Python "module" (file) to be imported by Gunicorn, this module would contain the actual application in a variable.

By default:

* `app.main` if there's a file `/app/app/main.py` or
* `main` if there's a file `/app/main.py`

For example, if your main file was at `/app/custom_app/custom_main.py`, you could set it like:

```bash
docker run -d -p 80:80 -e MODULE_NAME="custom_app.custom_main" myimage
```


#### `VARIABLE_NAME`

The variable inside of the Python module that contains the FastAPI application.

By default:

* `app`

For example, if your main Python file has something like:

```Python
from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def read_root():
    return {"Hello": "World"}
```

In this case `api` would be the variable with the FastAPI application. You could set it like:

```bash
docker run -d -p 80:80 -e VARIABLE_NAME="api" myimage
```


#### `APP_MODULE`

The string with the Python module and the variable name passed to Gunicorn.

By default, set based on the variables `MODULE_NAME` and `VARIABLE_NAME`:

* `app.main:app` or
* `main:app`

You can set it like:

```bash
docker run -d -p 80:80 -e APP_MODULE="custom_app.custom_main:api" myimage
```


#### `GUNICORN_CONF`

The path to a Gunicorn Python configuration file.

By default:

* `/app/gunicorn_conf.py` if it exists
* `/app/app/gunicorn_conf.py` if it exists
* `/gunicorn_conf.py` (the included default)

You can set it like:

```bash
docker run -d -p 80:80 -e GUNICORN_CONF="/app/custom_gunicorn_conf.py" myimage
```


#### `WORKERS_PER_CORE`

This image will check how many CPU cores are available in the current server running your container.

It will set the number of workers to the number of CPU cores multiplied by this value.

By default:

* `2`

You can set it like:

```bash
docker run -d -p 80:80 -e WORKERS_PER_CORE="3" myimage
```

If you used the value `3` in a server with 2 CPU cores, it would run 6 worker processes.

You can use floating point values too.

So, for example, if you have a big server (let's say, with 8 CPU cores) running several applications, and you have a FastAPI application that you know won't need high performance. And you don't want to waste server resources. You could make it use `0.5` workers per CPU core. For example:

```bash
docker run -d -p 80:80 -e WORKERS_PER_CORE="0.5" myimage
```

In a server with 8 CPU cores, this would make it start only 4 worker processes.


#### `WEB_CONCURRENCY`

Override the automatic definition of number of workers.

By default:

* Set to the number of CPU cores in the current server multiplied by the environment variable `WORKERS_PER_CORE`. So, in a server with 2 cores, by default it will be set to `4`.

You can set it like:

```bash
docker run -d -p 80:80 -e WEB_CONCURRENCY="2" myimage
```

This would make the image start 2 worker processes, independent of how many CPU cores are available in the server.


#### `HOST`

The "host" used by Gunicorn, the IP where Gunicorn will listen for requests.

It is the host inside of the container.

So, for example, if you set this variable to `127.0.0.1`, it will only be available inside the container, not in the host running it.

It's is provided for completeness, but you probably shouldn't change it.

By default:

* `0.0.0.0`

#### `PORT`

The port the container should listen on.

If you are running your container in a restrictive environment that forces you to use some specific port (like `8080`) you can set it with this variable.

By default:

* `80`

You can set it like:

```bash
docker run -d -p 80:8080 -e PORT="8080" myimage
```


#### `BIND`

The actual host and port passed to Gunicorn.

By default, set based on the variables `HOST` and `PORT`.

So, if you didn't change anything, it will be set by default to:
    
* `0.0.0.0:80`

You can set it like:

```bash
docker run -d -p 80:8080 -e BIND="0.0.0.0:8080" myimage
```


#### `LOG_LEVEL`

The log level for Gunicorn.

One of:

* `debug`
* `info`
* `warning`
* `error`
* `critical`

By default, set to `info`.

If you need to squeeze more performance sacrificing logging, set it to `warning`, for example:

You can set it like:

```bash
docker run -d -p 80:8080 -e LOG_LEVEL="warning" myimage
```

### Custom Gunicorn configuration file

The image includes a default Gunicorn Python config file at `/gunicorn_conf.py`.

It uses the environment variables declared above to set all the configurations.

You can override it by including a file in:

* `/app/gunicorn_conf.py`,
* `/app/app/gunicorn_conf.py` or replacing the one in
* `/gunicorn_conf.py` or replacing the one in


## License

This project is licensed under the terms of the MIT license.
