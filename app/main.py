from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from api.text import process_text
from api.image import process_image
from api.audio import process_audio
from api.video import process_video
from api.math import solve_math_problem
from api.logic import logical_reasoning

app = FastAPI()

# Serve static files (e.g., HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Text Processing
@app.post("/api/text")
async def text_processing(text: str):
    response = process_text(text)
    return JSONResponse(content={"response": response})

# Image Processing
@app.post("/api/image")
async def image_processing(file: UploadFile = File(...)):
    response = process_image(file)
    return JSONResponse(content={"response": response})

# Audio Processing
@app.post("/api/audio")
async def audio_processing(file: UploadFile = File(...)):
    response = process_audio(file)
    return JSONResponse(content={"response": response})

# Video Processing
@app.post("/api/video")
async def video_processing(file: UploadFile = File(...)):
    response = process_video(file)
    return JSONResponse(content={"response": response})

# Math Problem Solving
@app.post("/api/math")
async def math_processing(problem: str):
    response = solve_math_problem(problem)
    return JSONResponse(content={"response": response})

# Logical Reasoning
@app.post("/api/logic")
async def logic_processing(premises: list, conclusion: str):
    response = logical_reasoning(premises, conclusion)
    return JSONResponse(content={"response": response})
