from typing import List, Tuple

COMPANY_TERMS = ["Pfizer", "Moderna", "Roche", "AstraZeneca"]

def filter_non_academic_authors(authors: List[dict]) -> Tuple[List[str], List[str]]:
    """Extract non-academic authors and their company affiliations."""
    non_academic_authors = []
    company_affiliations = []
    for author in authors:
        name = author.get("name", "Unknown")
        affiliation = author.get("affiliation", "").lower()
        if any(term in affiliation for term in COMPANY_TERMS):
            non_academic_authors.append(name)
            company_affiliations.append(affiliation)
    return non_academic_authors, company_affiliations
