from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"email": "24f2001869@ds.study.iitm.ac.in", "message": "Hello from Codespaces!"}
