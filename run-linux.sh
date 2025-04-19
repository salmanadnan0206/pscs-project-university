#!/usr/bin/env bash
# run-linux.sh — automatically builds & then runs your container on Linux/X11

# 1) If the image doesn't exist, build it
if [[ -z "$(docker images -q pscs-app 2> /dev/null)" ]]; then
  echo "🔨 Building pscs-app image…"
  docker build --no-cache -t pscs-app . || { echo "Build failed!"; exit 1; }
fi

# 2) Allow GUI forwarding
xhost +local:docker

# 3) Run the container
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  pscs-app

