from fastapi import FastAPI
from routes import ops_user, client_user

app = FastAPI()

app.include_router(ops_user.router, prefix="/ops")
app.include_router(client_user.router, prefix="/client")
