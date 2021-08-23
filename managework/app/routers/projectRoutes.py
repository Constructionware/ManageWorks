#projectRoutes

from aiohttp import web
from app.models.Project import Project

handler = Project()
project_routes = web.RouteTableDef()

@project_routes.get('/projects')
async def get_projects(request):
    return web.json_response(await handler.loadProjects)

@project_routes.get('/project/{id}')
async def get_project(request):
    id = request.match_info.get('id', "Anonymous")    
    return web.json_response(await handler.get_project(id))

@project_routes.post('/project')
async def create_project(request):
    data = await request.json()
    return web.json_response( await handler.create(data))

@project_routes.post('/project/{password}/')
async def create_private_project(request):
    password = request.match_info.get('password', "Anonymous")  
    data = await request.json()
    return web.json_response( await handler.create_private( data, password))     

@project_routes.put('/project/{id}')
async def update_project(request):
    id = request.match_info.get('id', "Anonymous") 
    data = await request.json()
    return web.json_response( await handler.update(id, data)) 

@project_routes.get('/project/{id}/{clone_id}')
async def clone_project(request):
    id = request.match_info.get('id', "Anonymous") 
    clone_id = request.match_info.get('clone_id', "Anonymous")    
    return web.json_response(await handler.clone( id, clone_id))

#------------------------- DATABASE ---------------------------


