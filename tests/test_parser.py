def test_filter_non_academic_authors():
    authors = [
        {"name": "Dr. John Doe", "affiliation": "Pfizer"},
        {"name": "Dr. Jane Smith", "affiliation": "Harvard University"},
    ]
    non_academic_authors, affiliations = filter_non_academic_authors(authors)
    assert non_academic_authors == ["Dr. John Doe"]
    assert affiliations == ["pfizer"]
