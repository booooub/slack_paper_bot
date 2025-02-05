import requests

SEMANTIC_SCHOLAR_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_semantic_scholar_papers(query, max_results=5):
    """
    Semantic Scholar API를 사용하여 논문 검색
    """
    params = {
        "query": query,
        "fields": "title,abstract,url",
        "limit": max_results
    }
    
    response = requests.get(SEMANTIC_SCHOLAR_URL, params=params)
    
    if response.status_code == 200:
        papers = response.json().get("data", [])
        results = []
        for paper in papers:
            results.append({
                "title": paper["title"],
                "summary": paper.get("abstract", "No abstract available."),
                "pdf_link": paper["url"]
            })
        return results
    else:
        print(f"Semantic Scholar API 요청 실패: {response.status_code}")
        return []
