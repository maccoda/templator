from template import Template


class TestTemplate():

    def test_render(self):
        resource = "test_resources/test_variable"
        template = Template(resource + ".tmpl")
        result = template.render({"name": "Eva", "home_town": "Melbourne"})

        with open(resource + "_sol.tmpl", encoding="utf-8") as f:
            solution = f.read()
            assert result == solution
