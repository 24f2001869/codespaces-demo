from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Codespaces Demo")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitHub Codespaces Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 40px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: white;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.95);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                color: #333;
                text-align: center;
            }}
            h1 {{
                color: #2c3e50;
                margin-bottom: 20px;
            }}
            .email {{
                background: #3498db;
                color: white;
                padding: 15px 25px;
                border-radius: 25px;
                font-size: 1.2em;
                font-weight: bold;
                display: inline-block;
                margin: 20px 0;
            }}
            .info {{
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                border-left: 4px solid #3498db;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 GitHub Codespaces Demo</h1>
            <div class="info">
                <h2>CloudFirst Development</h2>
                <p>This application is running in a GitHub Codespace</p>
            </div>
            <div class="email">
                📧 24f2001869@ds.study.iitm.ac.in
            </div>
            <div class="info">
                <p><strong>Port Forwarding:</strong> Active</p>
                <p><strong>Environment:</strong> GitHub Codespaces</p>
                <p><strong>Framework:</strong> FastAPI (Python)</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Codespaces Demo"}

@app.get("/api/info")
async def get_info():
    return {
        "email": "24f2001869@ds.study.iitm.ac.in",
        "message": "Hello from GitHub Codespaces!",
        "framework": "FastAPI",
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)