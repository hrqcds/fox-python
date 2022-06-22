from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import user
import uvicorn

app = FastAPI(
    title="Api Foxconn - Protótipo",
    description="A api tem como objetivo criar uma rota para armazenar dados das máquinas,"
                "para uma predição de comportamento. "
                "Feita por: Henrique Costa dos Santos",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:4000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user.route)


if __name__ == "__main__":
    uvicorn.run(app, port=4000)
