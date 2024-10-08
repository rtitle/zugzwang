#!/usr/bin/env bash

set -e
set -x

uv run ruff check --select I --fix
uv run ruff format