import json
from report import save_report

def test_save_report(tmp_path):

    # Sample diagnostic results
    results = {
        "DNS": {
            "Domain":"google.com",
            "IP Address": "142.250.129.100",
            "Status": "Success"
        }
    }

    # Create a temporary report path
    filename = tmp_path / "test_report.json"

    # Generate the report
    returned_filename = save_report(
        results,
        str(filename)
    )

    # Check the file existence
    assert filename.exists()

    # Check the returned filename
    assert returned_filename == str(filename)

    # Read the generated JSON file
    with open(filename, "r", encoding="utf-8") as file:
        report = json.load(file)


    # Verify the report contents
    assert report["Diagnostic Results"] == results
    assert "Report Generated" in report