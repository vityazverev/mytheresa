class TestStatusCodes:

    def test_status_codes_for_all_pages(self, context, links, browser_type):
        errors_for_links = []

        # Visit each unique link and check the status code
        for link in links:
            new_page = context.new_page()  # Create a new page from context

            try:
                response = new_page.goto(link, timeout=30000)
                status_code = response.status

                if status_code >= 400:
                    errors_for_links.append((link, f"Unexpected status code: {status_code}"))
            except Exception as e:
                errors_for_links.append((link, f"Navigation error: {str(e)}"))
            finally:
                new_page.close()

        assert len(errors_for_links) == 0, f"Errors found on the following pages: {errors_for_links}"
