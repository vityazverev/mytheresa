from urllib.parse import urljoin


def extract_unique_links(page, base_url):
    # Extract all the links (href attributes) on the page
    links = page.eval_on_selector_all("a", "elements => elements.map(el => el.href)")

    # Convert to a set to remove duplicates, then back to a list
    unique_links = list(set(links))

    # Filter out empty, anchor, or JavaScript links
    filtered_links = [urljoin(base_url, link) for link in unique_links
                      if link and not link.startswith("javascript") and not link.startswith("#")]

    return filtered_links


def perform_login(page, login_page_url, username, password):
    """
    Function to perform login action.
    """
    # Navigate to the login page
    page.goto(login_page_url, timeout=30000)

    # Fill in the login form
    page.fill('input[name="username"]', username)  # Fill in the username
    page.fill('input[name="password"]', password)  # Fill in the password

    # Submit the login form
    page.click('input[type="submit"]')

    # Return the page object for further assertions
    return page
