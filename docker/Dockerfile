FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml README.md /app/
COPY ./src /app/src
RUN uv pip install --system .

CMD ["greeting-mcp"]