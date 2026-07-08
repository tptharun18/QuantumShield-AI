from fastapi import FastAPI

app = FastAPI(
    title="QuantumShield AI",
    description="Enterprise Identity, Cloud & Post-Quantum Security Intelligence Platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to QuantumShield AI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }