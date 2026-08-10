#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
exec uvicorn review_app:app --host "${CURATION_HOST:-0.0.0.0}" --port "${CURATION_PORT:-8765}" "$@"
