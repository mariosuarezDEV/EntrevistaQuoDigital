FROM python:3.13-slim
WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl
# Install UV curl -LsSf https://astral.sh/uv/install.sh | sh
RUN pip install uv

COPY . .

RUN cd api && uv sync

# Run project
EXPOSE 5000

CMD ["uv", "run", "flask", "--app", "main", "run", "--host", "0.0.0.0", "--port", "5000"]

# command for run this docker image
# docker build -t prueba_tecnica . && docker run -d -p 5000:5000 --name prueba_tecnica --env-file .env prueba_tecnica