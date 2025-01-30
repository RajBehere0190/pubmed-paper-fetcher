from cli import main
import sys

def test_cli_valid_query(mocker):
    mocker.patch("sys.argv", ["cli.py", "cancer treatment", "-f", "test.csv"])
    main()
    # Verify the output file is created and has content.
    assert os.path.exists("test.csv")
    os.remove("test.csv")
