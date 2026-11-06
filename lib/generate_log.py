from datetime import datetime
import requests


def generate_log(data):
    # Validate that the provided log data is a list.
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Create a filename using today's date.
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each log entry on its own line.
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    # Use the external requests package without making a network request.
    request = requests.Request(
        "GET",
        "https://example.com"
    ).prepare()

    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Prepared request: {request.method} {request.url}",
    ]

    generate_log(log_data)