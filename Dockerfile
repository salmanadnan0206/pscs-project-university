FROM python:3.10-slim

# Install all required Qt and X11 dependencies at once
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Core graphics libraries
    libgl1-mesa-glx \
    libegl1 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libfontconfig1 \
    # X11 core libraries
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxi6 \
    # XCB libraries needed by Qt
    libxcb1 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    libxcb-xkb1 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxcb-sync1 \
    libxcb-render0 \
    libxcb-shm0 \
    libxcb-glx0 \
    libxcb-cursor0 \
    # Additional dependencies for Qt functionality
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    # GLib dependency
    libglib2.0-0 \
    # Database support
    sqlite3 \
    # For font rendering
    libfreetype6 \
    # Cleanup apt cache
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy & install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire project code
COPY pscs-project-university/ ./pscs-project-university/

# Tell Qt to use the host X server
ENV QT_QPA_PLATFORM=xcb
# Ensure Qt can find fonts
ENV QT_QPA_FONTDIR=/usr/share/fonts

# Default working dir & entrypoint
WORKDIR /app/pscs-project-university
ENTRYPOINT ["python", "login_page.py"]
