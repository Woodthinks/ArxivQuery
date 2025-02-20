from arVix_ask import search_arxiv
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Tuple, Any

import uvicorn
import arVix_ask

app = FastAPI()


class Infor(BaseModel):
    prefix_query_pairs: List[Tuple[str, str]]
    relations: List[str]
    max_results: int
    sort_by: Any
    download: bool
    download_path: str


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/search")
def GetSearch(infor: Infor):
    result = search_arxiv(
        prefix_query_pairs=infor.prefix_query_pairs,
        relations=infor.relations,
        max_results=infor.max_results,
        download=infor.download,
        sort_by=infor.sort_by,
        download_path=infor.download_path,
    )
    return result


if __name__ == "__main__":
    uvicorn.run("mainGUI:app", host="127.0.0.1", port=8000, reload=True)
