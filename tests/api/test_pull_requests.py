import os
from utilities.api_utils import fetch_open_pull_requests


def test_fetch_pull_requests():
    """
     Test case to fetch open pull requests for a specific repository and save them as a CSV.
    """
    # GitHub API URL for open pull requests
    repo_url = "https://api.github.com/repos/appwrite/appwrite/pulls"

    # Save the file to the current working directory
    output_file = os.path.join(os.getcwd(), 'open_pull_requests.csv')

    # Call the utility function to fetch and save the PRs to CSV
    csv_file = fetch_open_pull_requests(repo_url, output_file)

    # Verify that the CSV file was created
    assert os.path.exists(csv_file), f"CSV file was not created at {csv_file}"

    # Optionally: Verify the CSV contents, e.g., read the file and check the headers
    with open(csv_file, 'r') as file:
        header = file.readline().strip()
        assert header == "PR Name,Created Date,Author", "CSV header mismatch"
