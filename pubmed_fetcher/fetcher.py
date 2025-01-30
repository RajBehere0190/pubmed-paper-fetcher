import requests
from typing import List, Dict

# Base URLs for PubMed API endpoints
PUBMED_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"  # For searching papers
DETAILS_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"  # For fetching paper details

def fetch_papers(query: str, max_results: int = 10) -> List[Dict]:
    """
    Fetch paper details from PubMed API based on a search query.

    Args:
        query (str): The search query for PubMed.
        max_results (int): Maximum number of results to fetch (default is 10).

    Returns:
        List[Dict]: A list of dictionaries containing paper details.
    """
    # Define the parameters for the search API request
    params = {
        "db": "pubmed",  # Specify the database (PubMed)
        "term": query,   # Search term (query)
        "retmax": max_results,  # Maximum number of results to return
        "retmode": "json"  # Response format (JSON)
    }

    # Send a GET request to the PubMed search API
    response = requests.get(PUBMED_API, params=params)

    # Raise an exception if the API request fails (e.g., non-200 status code)
    response.raise_for_status()

    # Extract the list of paper IDs from the JSON response
    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])

    # Fetch detailed metadata for each paper ID and return as a list of dictionaries
    return [fetch_paper_details(paper_id) for paper_id in paper_ids]

def fetch_paper_details(paper_id: str) -> Dict:
    """
    Fetch detailed metadata for a specific paper using its PubMed ID.

    Args:
        paper_id (str): The PubMed ID of the paper.

    Returns:
        Dict: A dictionary containing detailed metadata for the paper.
    """
    # Define the parameters for the details API request
    params = {
        "db": "pubmed",  # Specify the database (PubMed)
        "id": paper_id,  # PubMed ID of the paper
        "retmode": "json"  # Response format (JSON)
    }

    # Send a GET request to the PubMed details API
    response = requests.get(DETAILS_API, params=params)

    # Raise an exception if the API request fails
    response.raise_for_status()

    # Extract paper details from the JSON response
    data = response.json().get("result", {}).get(paper_id, {})

    # Return a dictionary containing relevant metadata for the paper
    return {
        "PubmedID": paper_id,  # PubMed ID of the paper
        "Title": data.get("title", "Unknown"),  # Title of the paper
        "Publication Date": data.get("pubdate", "Unknown"),  # Publication date
        "Authors": data.get("authors", [])  # List of authors
    }
