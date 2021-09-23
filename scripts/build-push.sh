#!/usr/bin/env bash

set -e

DOCKERFILE="$NAME"

if [ "$NAME" == "latest" ] ; then
    DOCKERFILE="python3.9"
fi

# Slim images are missing the build tools for uvloop
if [[ "$NAME" =~ "slim" ]] ; then
    PLATFORMS="linux/amd64"
else
    PLATFORMS="linux/amd64,linux/arm64,linux/arm/v7"
fi

use_tag="tiangolo/uvicorn-gunicorn-fastapi:$NAME"
use_dated_tag="${use_tag}-$(date -I)"

bash scripts/docker-login.sh

docker buildx create --use

docker buildx build \
  --platform $PLATFORMS \
  --file "./docker-images/${DOCKERFILE}.dockerfile" \
  -t "$use_tag"  \
  -t "$use_dated_tag"  \
  --push \
  "./docker-images/"
