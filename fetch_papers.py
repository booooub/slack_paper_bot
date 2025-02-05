import json
from arxiv_api import search_arxiv_papers
from semantic_scholar_api import search_semantic_scholar_papers
from crossref_api import search_crossref_papers
from database import save_paper, check_duplicate, get_topics
from slack_bot import send_slack_message

with open("config.json") as f:
    config = json.load(f)

def fetch_and_send_papers():
    token = config["slack_token"]
    
    channels = config["channels"].keys()
    
    for channel in channels:
        topics = get_topics(channel)
        
        for topic in topics:
            papers = []
            if config["apis"]["arxiv"]:
                papers.extend(search_arxiv_papers(topic))
            if config["apis"]["semantic_scholar"]:
                papers.extend(search_semantic_scholar_papers(topic))
            if config["apis"]["crossref"]:
                papers.extend(search_crossref_papers(topic))
                
            for paper in papers:
                if not check_duplicate(paper["title"]):
                    save_paper(paper["title"], paper["summary"], paper["pdf_link"])
                    message = f"*{paper['title']}*\n{paper['summary']}\n<{paper['pdf_link']}|[PDF]>"
                    send_slack_message(token, f"#{channel}", message)
