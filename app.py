from re import template
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import uvicorn
from views import views

static = StaticFiles(directory='statics')
routes = [
    Route("/", views.homepage, name="home"),
    Route("/resume.html", views.resume, name="resume"),
    Route("/discord.html", views.discord_bot, name="discord"),
    Mount("/static", static, name="static"),
]
app = Starlette(debug=True, routes=routes,
                exception_handlers=views.exception_handlers)
