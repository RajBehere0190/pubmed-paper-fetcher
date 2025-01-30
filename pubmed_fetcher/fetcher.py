import requests
from typing import List, Dict

PUBMED_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_papers(query: str, max_results: int = 10) -> List[Dict]:
    """Fetch paper details from PubMed API."""
    params = {"db": "pubmed", "term": query, "retmax": max_results, "retmode": "json"}
    response = requests.get(PUBMED_API, params=params)
    response.raise_for_status()
    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
    return [fetch_paper_details(paper_id) for paper_id in paper_ids]

def fetch_paper_details(paper_id: str) -> Dict:
    """Fetch detailed metadata for a given paper."""
    params = {"db": "pubmed", "id": paper_id, "retmode": "json"}
    response = requests.get(DETAILS_API, params=params)
    response.raise_for_status()
    data = response.json().get("result", {}).get(paper_id, {})
    return {
        "PubmedID": paper_id,
        "Title": data.get("title", "Unknown"),
        "Publication Date": data.get("pubdate", "Unknown"),
        "Authors": data.get("authors", [])
    }
