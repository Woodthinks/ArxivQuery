from arVix_ask import search_arxiv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Tuple, Any
import json
import uvicorn
import arVix_ask

app = FastAPI()
app.mount("/src/web", StaticFiles(directory="src/web"), name="static")


class Infor(BaseModel):
    prefix_query_pairs: List[Tuple[str, str]]
    relations: List[str]
    max_results: int
    download: bool
    download_path: str


@app.get("/", response_class=HTMLResponse)
def root():
    try:
        with open("src/web/homepage.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return html_content
    except FileNotFoundError:
        return "<h1>File not found</h1>"


@app.post("/search", response_class=HTMLResponse)
def GetSearch(infor: Infor):
    result = search_arxiv(
        prefix_query_pairs=infor.prefix_query_pairs,
        relations=infor.relations,
        max_results=infor.max_results,
        download=infor.download,
        download_path=infor.download_path,
    )
    try:
        with open("database.json", "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving data to database.json: {e}")
    try:
        with open("src/web/answer.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return html_content
    except FileNotFoundError:
        return "<h1>File not found</h1>"


@app.get("/answer")
async def answer():
    try:
        with open("database.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except Exception as e:
        return {"error": f"Error reading database.json: {e}"}
    return data


if __name__ == "__main__":
    uvicorn.run("mainGUI:app", host="127.0.0.1", port=8000, reload=True)
