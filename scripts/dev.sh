#!/usr/bin/env bash

set -e
set -x

uv run alembic upgrade head
uv run fastapi dev
