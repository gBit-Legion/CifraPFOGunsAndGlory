from fastapi import FastAPI, Body, UploadFile, File, Form, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from typing import Annotated

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return FileResponse("frontend/public/index.html")


@app.post("/documents")
async def drag_and_drop(files: list[UploadFile]):
    for file in files:
        contents = await file.read()
        file.close()
        buffer = BytesIO(contents)
        with open(file.filename, "wb") as f:
            f.write(buffer.getbuffer())
        print(file.file)
