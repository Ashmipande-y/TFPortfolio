from fastapi import FastAPI


app = FastAPI(
    title="TrackForge API",
    description="Backend API for the TrackForge construction site asset intelligence platform.",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "trackforge-api",
    }