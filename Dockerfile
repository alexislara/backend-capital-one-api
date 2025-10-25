# --------------------------
# Base image
# --------------------------
FROM python:3.11-alpine AS base

ARG SRC_DIR=/usr/src/app
ARG APP_USER=django

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8
ENV LANG C.UTF-8
ENV HOME=${SRC_DIR}
ENV PATH="/opt/venv/bin:$PATH"

RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    gettext \
    postgresql-dev \
    bash

RUN addgroup -S ${APP_USER} && adduser -S ${APP_USER} -G ${APP_USER}

# Crear entorno virtual global
RUN python -m venv /opt/venv

WORKDIR ${SRC_DIR}
EXPOSE 8000

# --------------------------
# Builder
# --------------------------
FROM base AS builder

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# --------------------------
# Development
# --------------------------
FROM base AS development

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER django

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM base AS production
WORKDIR /home/django/app
COPY --from=builder /opt/venv /opt/venv
COPY . .
USER django

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health-check/ || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
