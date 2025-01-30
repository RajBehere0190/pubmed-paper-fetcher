import argparse
import sys
from pubmed_fetcher import fetch_papers, filter_non_academic_authors, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug information")
    args = parser.parse_args()
    
    if args.debug:
        print(f"Debug Mode: ON")
        print(f"Search Query: {args.query}")
        if args.file:
            print(f"Output File: {args.file}")

    try:
        print(f"Fetching papers from PubMed for query: '{args.query}'...")
        papers = fetch_papers(args.query)
        print(f"Fetched {len(papers)} papers from PubMed.")
        
        results = []
        for paper in papers:
            if args.debug:
                print(f"Processing paper: {paper['PubmedID']} - {paper['Title']}")
            
            non_academic_authors, company_affiliations = filter_non_academic_authors(paper["Authors"])
            if non_academic_authors:
                results.append({
                    "PubmedID": paper["PubmedID"],
                    "Title": paper["Title"],
                    "Publication Date": paper["Publication Date"],
                    "Non-academic Author(s)": ", ".join(non_academic_authors),
                    "Company Affiliation(s)": ", ".join(company_affiliations),
                })
        
        if args.file:
            if results:
                save_to_csv(results, args.file)
                print(f"Results saved to {args.file}")
            else:
                print(f"No results to save. The file '{args.file}' was not created.")
        else:
            if results:
                for result in results:
                    print(result)
            else:
                print("No results to display.")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
