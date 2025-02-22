from arVix_ask import search_arxiv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Tuple, Any
import uvicorn

app = FastAPI()
app.mount("/src/web", StaticFiles(directory="src/web"), name="static")

context = []


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


@app.post("/search")
def GetSearch(infor: Infor):
    result = search_arxiv(
        prefix_query_pairs=infor.prefix_query_pairs,
        relations=infor.relations,
        max_results=infor.max_results,
        download=infor.download,
        download_path=infor.download_path,
    )
    context.clear()
    context.append(result)
    return True


@app.get("/answer")
async def answer():
    return {"results": context}


if __name__ == "__main__":
    uvicorn.run("mainGUI:app", host="127.0.0.1", port=8000, reload=True)
