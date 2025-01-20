# Stage 1: Builder
FROM python:3.10-alpine as base
LABEL maintainer="steffythankamwilson7@gmail.com"

FROM base as builder

# Install system dependencies
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev

# Upgrade pip
RUN pip install --upgrade pip

WORKDIR /install
COPY ./requirements.txt ./

RUN pip3 install --no-cache-dir \
        --prefix="/install" -r requirements.txt

# Stage 2: Final lightweight image
FROM base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevent creation of .pyc files
ENV PYTHONUNBUFFERED 1         # Ensure real-time output logging

RUN apk update && rm -rf /var/cache/apk/*

COPY --from=builder /install /usr/local
# Set working directory
WORKDIR /usr/src/app
COPY . .

# Expose the application port
EXPOSE 8090

# Set the default command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8090"]
