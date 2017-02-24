from template import Template


class TestTemplate():

    def test_render_variables(self):
        resource = "test_resources/test_variable"
        template = Template(resource + ".tmpl")
        result = template.render({"name": "Eva", "home_town": "Melbourne"})

        with open(resource + "_sol.tmpl", encoding="utf-8") as f:
            solution = f.read()
            assert result == solution

    def test_render_conditional_true(self):
        resource = "test_resources/test_conditional"
        template = Template(resource + ".tmpl")
        result = template.render({"my_condition": True})

        with open(resource + "_true.tmpl", encoding="utf-8") as f:
            solution = f.read()
            assert result == solution
