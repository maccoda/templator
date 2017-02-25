from statements import Parser


class TestParser:
    def test_variable_parse(self):
        """Test a single variable parse"""
        tester = Parser("Hello there {{name}}!")
        assert tester.render({"name": "Geoff"}) == "Hello there Geoff!"

    def test_multi_parse(self):
        """Test multi level parsing and rendering"""

        test_str = ("Hello there everyone from {{city}}\n"
                    "{{#each events}}\n"
                    "  {{#if my_condition}}\n"
                    "  The condition was true {{name}}!\n"
                    "  {{#else}}\n"
                    "  The condition was false...\n"
                    "  {{/if}}\n"
                    "{{/each}}\n"
                    "And that is all they wrote.\n"
                    "{{#if my_other_condition}}\n"
                    "  {{#each events}}\n"
                    "  The condition was true again {{name}}!\n"
                    "  {{/each}}\n"
                    "{{#else}}\n"
                    "   The condition was false again\n"
                    "{{/if}}")
        tester = Parser(test_str)
        actual = tester.render({"my_condition": True, "events": [{"name": "Bob"}, {"name": "Frank"}],
                                "city": "New York", "my_other_condition": False})
        # FIXME Need to make a decision on how to handle the whitespace. Which will be removed and which will stay
        expected = ("Hello there everyone from New York\n"
                    "The condition was true Bob!\n  \n"
                    "The condition was true Frank!\n  \n\n"
                    "And that is all they wrote.\n"
                    "The condition was false again\n")

        assert actual == expected
