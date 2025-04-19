#!/usr/bin/env bash
# run-macos.sh

# 1) Find your host IP (on en0; change interface if needed)
IP=$(ifconfig en0 | awk '/inet /{print $2}')

# 2) Allow XQuartz to accept connections from that IP
xhost + $IP

# 3) Run the container, pointing DISPLAY at your XQuartz server
docker run -it --rm \
  -e DISPLAY=${IP}:0 \
  pscs-app
