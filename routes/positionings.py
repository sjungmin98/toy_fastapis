from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

templates = Jinja2Templates(directory="templates")
 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],
)

positionings_router = APIRouter()

@positionings_router.get("/containers", response_class=HTMLResponse)
async def read_containers(request: Request):
    return templates.TemplateResponse("positionings/containers.html", {"request": request})

@positionings_router.get("/forms", response_class=HTMLResponse)
async def read_forms(request: Request):
    return templates.TemplateResponse("positionings/forms.html", {"request": request})

@positionings_router.get("/grids", response_class=HTMLResponse)
async def read_grids(request: Request):
    return templates.TemplateResponse("positionings/grids.html", {"request": request})

@positionings_router.get("/standards", response_class=HTMLResponse)
async def read_standards(request: Request):
    return templates.TemplateResponse("positionings/standards.html", {"request": request})

app.include_router(positionings_router, prefix="/positionings")