# 1) Set the DISPLAY endpoint for Docker (assumes VcXsrv/Xming is running)
$Env:DISPLAY = "host.docker.internal:0.0"

# 2) Check if the Docker image exists locally (silence all output)
docker image inspect pscs-app:latest *>$null
# 3) Use the exit code to decide on building
if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker image 'pscs-app:latest' not found locally. Building now..."
    docker build -t pscs-app:latest .
} else {
    Write-Host "Docker image 'pscs-app:latest' found locally."
}

# 4) Run the container with X11 forwarding
docker run -it --rm `
    -e DISPLAY=$Env:DISPLAY `
    pscs-app
