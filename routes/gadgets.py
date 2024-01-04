from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

templates = Jinja2Templates(directory="templates")
 

gadgets_router = APIRouter()

@gadgets_router.get("/buttons", response_class=HTMLResponse)
async def read_buttons(request: Request):
    return templates.TemplateResponse("/gadgets/buttons.html", {"request": request})


@gadgets_router.get("/cards", response_class=HTMLResponse)
async def read_cards(request: Request):
    return templates.TemplateResponse("gadgets/cards.html", {"request": request})

@gadgets_router.get("/colors", response_class=HTMLResponse)
async def read_colors(request: Request):
    return templates.TemplateResponse("gadgets/colors.html", {"request": request})

@gadgets_router.get("/colors_second", response_class=HTMLResponse)
async def read_colors2(request: Request):
    return templates.TemplateResponse("gadgets/colors_second.html", {"request": request})




