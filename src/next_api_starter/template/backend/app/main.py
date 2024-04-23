from fastapi import FastAPI, Request, middleware
from fastapi.middleware.cors import CORSMiddleware
#from .routers import subrouter
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# app.include_router(
#     sub_routers
# )

#Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers =["*"],
    expose_headers = ["*"]
)


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("------------Request Details------------")
        print(f"Request {request.items}")
        print(f"Method: {request.method}")
        print(f"Path: {request.url.path}")
        print(f"Headers: {request.headers}")
        # You can add more options as you fit fine
        
        response = await call_next(request)
        return response
        
# Only if you want to read all the incoming request uncomment the below code
# app.add_middleware(RequestLoggerMiddleware)


@app.get("/")
def home():
    return f'Hi, this is {service_name}'