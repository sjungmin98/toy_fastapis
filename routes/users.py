
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
 
users_router = APIRouter()

@users_router.get("/form")
async def read_buttons(request: Request):
    return templates.TemplateResponse("/users/inserts.html", {"request": request})

@users_router.post("/logins")
async def read_buttons(request: Request):
    print(dict(await request.form()))
    return templates.TemplateResponse("/users/logins.html", {"request": request})

@users_router.post("/lists")
async def read_buttons(request: Request):
    print(dict(await request.form()))
    return templates.TemplateResponse("/users/lists.html", {"request": request})
 
@users_router.get("/reads/{object_id}") # /users/reads/John
async def read_buttons(request: Request, object_id):
    dict_details = dict(request.query_params)
    print(dict_details)
    return templates.TemplateResponse("/users/reads.html", {"request": request})

@users_router.get("/lists")
async def read_buttons(request: Request):
    
    return templates.TemplateResponse("/users/lists.html", {"request": request})