# Use the official Ubuntu 24.04 base image provided by the benchmark framework.
FROM ghcr.io/laude-institute/t-bench/ubuntu-24-04:20250624

# Update package lists and install python3-pytest directly using the system's
# package manager (apt-get). This is the correct way for modern Ubuntu.
RUN apt-get update && apt-get install -y python3-pytest

# Copy all task files from your local directory into the container.
COPY . /app

# Create the directory where the output report is expected to be saved.
RUN mkdir -p /app/reports

# Set the working directory to /app.
WORKDIR /app
