from fastapi import Request
from fastapi import FastAPI
from routes.gadgets import gadgets_router as gadgets_router
from routes.positionings import positionings_router as positionings_router
from routes.users import users_router as users_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.include_router(gadgets_router, prefix="/gadgets")
app.include_router(positionings_router, prefix="/positionings")
app.include_router(users_router, prefix="/users")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse("main.html", {'request':request})



