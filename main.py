from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn

async def homepage(request):
    return JSONResponse({"hello":"world"})

async def about(request):
    return JSONResponse({"message": "bye"})

## async means can be accessed at same time.

async def contact(request):
    return JSONResponse({"ok then": "interesting"})


app = Starlette(
    debug=True,
    routes=[
        Route('/', homepage)
        Route('/', about)
        Route('/', contact)
    ]
)
uvicorn.run(app,port=8080)