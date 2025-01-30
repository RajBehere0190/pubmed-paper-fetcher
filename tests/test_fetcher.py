def test_fetch_valid_query():
    papers = fetch_papers("cancer treatment")
    assert len(papers) > 0
    assert "PubmedID" in papers[0]
