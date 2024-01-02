from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

templates = Jinja2Templates(directory="routes/templates")
 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse("main.html"
                                      ,{'request':request})

gadgets_router = APIRouter()

@gadgets_router.get("/buttons", response_class=HTMLResponse)
async def read_buttons(request: Request):
    return templates.TemplateResponse("gadgets/buttons.html", {"request": request})


@gadgets_router.get("/cards", response_class=HTMLResponse)
async def read_cards(request: Request):
    return templates.TemplateResponse("gadgets/cards.html", {"request": request})

@gadgets_router.get("/colors", response_class=HTMLResponse)
async def read_colors(request: Request):
    return templates.TemplateResponse("gadgets/colors.html", {"request": request})

@gadgets_router.get("/colors_second", response_class=HTMLResponse)
async def read_colors2(request: Request):
    return templates.TemplateResponse("gadgets/colors_second.html", {"request": request})

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

app.include_router(gadgets_router, prefix="/gadgets")
app.include_router(positionings_router, prefix="/positionings")


