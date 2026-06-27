#!/usr/bin/env bash
set -euo pipefail

python3 -m src.pipeline

echo
echo "Pipeline termine."
echo "Lancez ensuite l'API avec :"
echo "uvicorn src.api.main:app --reload"
echo
echo "Endpoints utiles :"
echo "- Dashboard: http://127.0.0.1:8000"
echo "- KPI:       http://127.0.0.1:8000/api/kpis"
echo "- Qualite:   http://127.0.0.1:8000/api/data-quality"
echo "- Lineage:   http://127.0.0.1:8000/api/lineage"
