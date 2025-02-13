# PubMed Paper Fetcher

## Overview

**PubMed Paper Fetcher** is a Python-based tool that retrieves research papers from the **PubMed API** based on a given search query.  
It fetches details such as the **paper title, publication date, and authors**, presenting them in a structured format.

## Project Structure

pubmed-paper-fetcher/

├── pubmed_fetcher/       # Main module containing the fetching logic

│   ├── fetcher.py        # Fetches papers and metadata from PubMed

├── tests/                # Unit tests for the module and CLI

│   ├── test_cli.py       # Tests for the CLI functionality

├── cli.py                # Command-line interface for fetching papers

├── papers.csv            # Sample output file containing fetched papers

├── pyproject.toml        # Configuration file for dependency management (Poetry)

├── poetry.lock           # Lock file for Poetry dependencies

├── .gitignore            # Files and directories to be ignored by Git

└── README.md             # Documentation (this file)





## Installation and Setup

### Prerequisites

- Ensure that you have **Python 3.8+** installed on your system.

### Clone the Repository

git clone https://github.com/RajBehere0190/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher


### Install Dependencies

This project uses **Poetry** for dependency management. If you don’t have it installed, install it first:
pip install poetry

Then, install the required dependencies:
poetry install


## Usage

### Command-line Interface (CLI)

To fetch papers based on a search term, use the following command:

python cli.py --query "machine learning" --max_results 5


## Tools and Technologies Used
Python - Primary programming language.

Requests - For making HTTP requests.

PubMed API - To fetch research papers.

Poetry - Dependency management.


✅ **Now, when you copy this, it will retain all Markdown formatting in your README.md file** without breaking the structure. 🚀

