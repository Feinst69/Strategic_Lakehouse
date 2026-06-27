import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


PROJECT_ROOT = Path(__file__).resolve().parents[2]
GOLD_DIR = PROJECT_ROOT / "data" / "gold"
WEB_DIR = PROJECT_ROOT / "src" / "web"

app = FastAPI(
    title="Strategic Lakehouse API",
    description="API BI exposant les KPI Gold du POC Lakehouse.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")


@app.get("/")
def home() -> FileResponse:
    return FileResponse(WEB_DIR / "index.html")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/kpis")
def get_kpis() -> dict[str, float | int | str]:
    kpi_file = GOLD_DIR / "kpis.json"
    if not kpi_file.exists():
        raise HTTPException(
            status_code=404,
            detail="KPI Gold introuvables. Lancez d'abord: python -m src.pipeline",
        )

    with kpi_file.open(encoding="utf-8") as file:
        return json.load(file)


@app.get("/api/data-quality")
def get_data_quality() -> dict:
    quality_file = GOLD_DIR / "data_quality_report.json"
    if not quality_file.exists():
        raise HTTPException(
            status_code=404,
            detail="Rapport qualite introuvable. Lancez d'abord: python -m src.pipeline",
        )

    with quality_file.open(encoding="utf-8") as file:
        return json.load(file)


@app.get("/api/lineage")
def get_lineage() -> dict:
    lineage_file = GOLD_DIR / "lineage.json"
    if not lineage_file.exists():
        raise HTTPException(
            status_code=404,
            detail="Lineage introuvable. Lancez d'abord: python -m src.pipeline",
        )

    with lineage_file.open(encoding="utf-8") as file:
        return json.load(file)
