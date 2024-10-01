import pytest
from utilities.utils import extract_unique_links
from playwright.sync_api import sync_playwright


# Command-line argument for environment selection
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="production", help="Environment to run tests against: local or production"
    )


# Fixture for the base URL based on environment
@pytest.fixture(scope="session")
def base_url(request):
    env = request.config.getoption("--env")
    if env == "local":
        url = "http://localhost:4000/fashionhub/"
    elif env == "staging":
        url = "https://staging-env/fashionhub/"
    elif env == "production":
        url = "https://pocketaces2.github.io/fashionhub/"
    else:
        raise ValueError(f"Unknown environment: {env}")

    return url


# Parametrize the test with different browsers
@pytest.fixture(params=["chromium", "firefox", "webkit"], scope="session")
def browser_type(request):
    return request.param


# Browser fixture
@pytest.fixture(scope="session")
def browser(browser_type):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # Set to headless=True if needed
    if browser_type == "chromium":
        browser = playwright.chromium.launch(headless=False)  # Launch Chromium
    elif browser_type == "firefox":
        browser = playwright.firefox.launch(headless=False)  # Launch Firefox
    elif browser_type == "webkit":
        browser = playwright.webkit.launch(headless=False)  # Launch WebKit (Safari)

    yield browser
    browser.close()
    playwright.stop()


# Browser context fixture
@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


# Page fixture with `base_url` injected as an argument
@pytest.fixture
def page(context, base_url):  # Inject `base_url` here as an argument
    page = context.new_page()

    # Print base_url to confirm it's being passed correctly
    print(f"Navigating to base_url: {base_url}")

    # Navigate to the base URL
    page.goto(base_url, timeout=30000)

    # Print the actual page URL after navigation
    print(f"Current URL after navigation: {page.url}")

    # Print the full page content to debug if page is loaded correctly
    print(f"Page content:\n{page.content()}")

    yield page
    page.close()


# Links fixture with `base_url` injected as an argument
@pytest.fixture
def links(page, base_url):
    print(f"Extracting links from: {page.url}")

    # Wait for the anchor tags to load
    page.wait_for_selector('a', timeout=10000)  # Ensure links are present

    # Extract unique links
    links = extract_unique_links(page, base_url)

    # Print the extracted links for debugging
    print(f"Extracted links: {links}")

    return links
