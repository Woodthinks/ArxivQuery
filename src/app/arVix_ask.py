import arxiv
from typing import List, Tuple, Dict, Union


def search_arxiv(
    prefix_query_pairs: List[Tuple[str, str]],
    relations: List[str],
    max_results: int = 10,
    sort_by=arxiv.SortCriterion.Relevance,
    download: bool = False,
    download_path: str = ".",
):
    # 检查 relations 列表的长度是否符合要求
    if len(relations) != len(prefix_query_pairs) - 1:
        raise ValueError(
            "The length of 'relations' must be one less than the length of 'prefix_query_pairs'."
        )

    query_parts = []
    for prefix, query in prefix_query_pairs:
        if prefix == "all":
            query_parts.append(query)
        else:
            query_parts.append(f"{prefix}:{query}")

    # 根据 relations 列表构建查询字符串
    search_query = ""
    for i in range(len(query_parts) - 1):
        search_query += f"{query_parts[i]} {relations[i]} "
    search_query += query_parts[-1]

    search = arxiv.Search(query=search_query, max_results=max_results, sort_by=sort_by)
    client = arxiv.Client()
    results = []

    """
    - entry_id	            A url 
    - updated	            When the result was last updated.
    - published	            When the result was originally published.
    - title	The             title of the result.
    - authors	            The result’s authors, as arxiv.Authors.
    - summary	            The result abstract.
    - comment	            The authors’ comment if present.
    - journal_ref	        A journal reference if present.
    - doi	                A URL for the resolved DOI to an external resource if present.
    - primary_category	    The result’s primary arXiv category. See arXiv: Category Taxonomy[4].
    - categories	        All of the result’s categories. See arXiv: Category Taxonomy.
    - links	                Up to three URLs associated with this result, as arxiv.Links.
    - pdf_url	            A URL for the result’s PDF if present. Note: this URL also appears among result.links.
    """

    for result in client.results(search):
        result_dict = {
            "entry_id": result.entry_id,
            "updated": str(result.updated),
            "published": str(result.published),
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "summary": result.summary,
            "comment": result.comment if result.comment else "",
            "journal_ref": result.journal_ref if result.journal_ref else "",
            "doi": result.doi if result.doi else "",
            "primary_category": result.primary_category,
            "categories": result.categories,
            "links": [str(link.href) for link in result.links],
            "pdf_url": result.pdf_url if result.pdf_url else "",
        }
        results.append(result_dict)

        if download:
            try:
                result.download_pdf(dirpath=download_path)
                print(
                    f"Successfully downloaded paper: {result.title} to {download_path}"
                )
            except Exception as e:
                print(f"Error occurred while downloading paper {result.title}: {e}")
    print(type({"results": results}))
    print(result)
    return {"results": results}


if __name__ == "__main__":
    prefix_query_pairs = [
        ("all", "machine learning"),
        ("au", "John Doe"),
        ("ti", "deep learning"),
    ]
    relations = ["AND", "OR"]
    max_results = 5
    sort_by = arxiv.SortCriterion.Relevance
    download = False
    download_path = "./papers"

    results = search_arxiv(
        prefix_query_pairs=prefix_query_pairs,
        relations=relations,
        max_results=max_results,
        sort_by=sort_by,
        download=download,
        download_path=download_path,
    )

    print("Search Results:")
    for result in results["results"]:
        print(result["title"])
