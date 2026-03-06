FROM ghcr.io/astral-sh/uv:debian

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app

RUN uv sync --frozen --no-cache
RUN apt-get install libkrb5-dev -y

# Pip install
ADD src ./src
ADD pyproject.toml .
ADD setup.py .

# RUN pip install . --no-cache-dir
RUN uv sync

CMD ["uv", "run", "fastapi", "run", "src/aind_active_directory_service_server/main.py", "--port", "80"]
