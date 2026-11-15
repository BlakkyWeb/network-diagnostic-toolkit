import json
from datetime import datetime


def save_report(results, filename = "network_report.json"):

    report = {
        "Report Generated": datetime.now().isoformat(
            timespec="seconds"
        ),
        "Diagnostic Results": results
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=4
        )

    return filename