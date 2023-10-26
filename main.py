import shutil

from fastapi import FastAPI, Body, UploadFile, File, Form, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


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
        file_location = f"files/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
            print(file_object)
