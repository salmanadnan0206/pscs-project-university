# 1) Ensure VcXsrv/Xming is running (Disable access control)
# 2) Set the display endpoint for Docker
$Env:DISPLAY = "host.docker.internal:0.0"

# 3) Check if the Docker image exists locally
$imageExists = docker image inspect pscs-app:latest -f '{{.Id}}' -ErrorAction SilentlyContinue

if (-not $imageExists) {
    Write-Host "Docker image 'pscs-app:latest' not found locally. Building the image..."
    docker build -t pscs-app:latest .
} else {
    Write-Host "Docker image 'pscs-app:latest' found locally."
}

# 4) Run the container
docker run -it --rm `
  -e DISPLAY=$Env:DISPLAY `
  pscs-app
