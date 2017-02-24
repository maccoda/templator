from statements import ConditonalStatement, VariableStatement


class TestStatement:

    def test_variable_statement(self):
        tester = VariableStatement("{{data}}", {"data": "Hello"})
        assert tester.evaluate() == "Hello"

    def test_conditional_statement(self):
        tester = ConditonalStatement(
            "{{#if good}}\nIt is good\n{{#else}}\nIt is not good\n{{/else}}",
            {"good": True, "bad": False})

        assert tester.evaluate() == "It is good"
