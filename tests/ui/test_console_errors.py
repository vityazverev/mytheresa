class TestConsoleErrors:

    def test_no_console_errors_for_all_pages(self, context, links, browser_type):
        errors_for_links = []

        # Visit each unique link and check for console errors
        for link in links:
            new_page = context.new_page()  # Create a new page from context
            console_messages = []

            new_page.on("console", lambda msg: console_messages.append(msg))

            try:
                new_page.goto(link, timeout=30000)  # Set timeout to 30 seconds
                error_messages = [msg for msg in console_messages if msg.type == "error"]

                if error_messages:
                    errors_for_links.append((link, [msg.text for msg in error_messages]))
            except Exception as e:
                errors_for_links.append((link, f"Navigation error: {str(e)}"))
            finally:
                new_page.close()

        assert len(errors_for_links) == 0, f"Console errors found on the following pages: {errors_for_links}"
