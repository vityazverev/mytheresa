import requests
import csv
from datetime import datetime

def fetch_open_pull_requests(repo_url, output_file):
    """
    Fetch open pull requests from the GitHub API for a specific repository and save them to a CSV file.

    :param repo_url: The API URL for fetching pull requests.
    :param output_file: The path where the CSV file will be saved.
    :return: Path to the CSV file.
    """
    response = requests.get(repo_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch pull requests. Status code: {response.status_code}")

    pull_requests = response.json()

    # Prepare data for CSV
    csv_data = []
    for pr in pull_requests:
        pr_name = pr['title']
        pr_created_at = pr['created_at']
        pr_author = pr['user']['login']

        # Convert the created_at to a more readable format
        pr_created_at = datetime.strptime(pr_created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")

        csv_data.append([pr_name, pr_created_at, pr_author])

    # Write to CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['PR Name', 'Created Date', 'Author'])  # Writing headers
        writer.writerows(csv_data)  # Writing PR data

    return output_file
