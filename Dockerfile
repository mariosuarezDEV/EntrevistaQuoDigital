FROM python:3.13-slim
WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl
# Install UV curl -LsSf https://astral.sh/uv/install.sh | sh
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# Configure environment for UV
ENV PATH="/root/.uv/bin:${PATH}"
ENV UV_LINK_MODE=copy

# Run project
EXPOSE 5000

CMD ["uv", "run", "flask", "--app", "main", "run", "--host", "0.0.0.0", "--port", "5000"]