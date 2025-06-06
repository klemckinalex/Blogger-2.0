from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Папка со статикой (CSS, JS, картинки)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Папка с шаблонами
templates = Jinja2Templates(directory="templates")

# Корневой маршрут: отображает index.html
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
