import requests

CROSSREF_URL = "https://api.crossref.org/works"

def search_crossref_papers(query, max_results=5):
    """
    CrossRef API를 사용하여 논문 검색
    """
    params = {
        "query": query,
        "rows": max_results,
        "select": "title,abstract,URL"
    }

    response = requests.get(CROSSREF_URL, params=params)

    if response.status_code == 200:
        papers = response.json().get("message", {}).get("items", [])
        results = []
        for paper in papers:
            results.append({
                "title": paper.get("title", ["No title"])[0],
                "summary": paper.get("abstract", "No abstract available."),
                "pdf_link": paper.get("URL", "No URL available")
            })
        return results
    else:
        print(f"CrossRef API 요청 실패: {response.status_code}")
        return []
