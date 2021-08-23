#Opal Server 
#opal.server.py

import aiohttp_cors

from aiohttp_remotes import AllowedHosts, BasicAuth, Secure, setup
from aiohttp import web
from app.models.Project import setup_project
from app.routers.projectRoutes import project_routes

async def hello(request):
    return web.Response(text="Welcome to Opal Your Friendly Project Manager.")


debug = True  # O
host = '0.0.0.0' # Make app available on the Network
port = 29022
app = web.Application()

app.add_routes([web.get('/', hello)])
app.add_routes(project_routes)


# Configure default CORS settings.
cors = aiohttp_cors.setup(
    app,
    defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    },
)

# Configure CORS on all routes.
for route in list(app.router.routes()):
    cors.add(route)


async def app_factory(app):
    app = app
    await setup_project()
    await setup(
        app, AllowedHosts(allowed_hosts=("*",))
    )  # , BasicAuth("user", "password", "realm"))

    return app

def serve():
    if debug:
        print("Opal Server Reloading....")        
    web.run_app(app_factory(app), host=host, port=port, shutdown_timeout=3600, backlog=256)

if __name__ == "__main__":
    serve()