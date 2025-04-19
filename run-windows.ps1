# run-windows.ps1

# 1) Ensure VcXsrv/Xming is running (Disable access control)
# 2) Tell Docker the display endpoint
$Env:DISPLAY = "host.docker.internal:0.0"

# 3) Run the container
docker run -it --rm `
  -e DISPLAY=$Env:DISPLAY `
  pscs-app
