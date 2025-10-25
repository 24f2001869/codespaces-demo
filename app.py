from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitHub Codespaces</title>
    </head>
    <body>
        <h1>GitHub Codespaces Demo</h1>
        <p>Email: 24f2001869@ds.study.iitm.ac.in</p>
    </body>
    </html>
    """

@app.get("/plain")
async def plain_text():
    return "24f2001869@ds.study.iitm.ac.in"

@app.get("/json")
async def json_response():
    return {"email": "24f2001869@ds.study.iitm.ac.in"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
