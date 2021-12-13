import shutil
import os.path as osp
from typing import List
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/")
async def root():
    """
    main page
    :return:
    """
    return {"message": "Hellow World"}


@app.post("/upload_image")
async def upload_image(files: List[UploadFile] = File(...)):
    """
    save images to disk
    :param files:
    :return: str
    """
    for image in files:
        save_to = osp.join("database", "images", image.filename)
        with open(save_to, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

    return {"message": "All files are uploaded"}


@app.post("/upload_video")
async def upload_video(file: UploadFile = File(...)):
    """
    save video to disk
    :param file:
    :return: str
    """
    save_to = osp.join("database", "videos", file.filename)
    with open(save_to, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}

