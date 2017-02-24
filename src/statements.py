"""Module containing all data related to the parsing and evaluating of
statements within a template.
"""

import re


class Statement():
    """
    A statement contained within the template. This will be the capture in
    the braces.
    """

    def __init__(self):
        self.value = ""

    def evaluate(self):
        return self.value


class VariableStatement(Statement):
    """A statement for a single variable substitution."""

    def __init__(self, template_string, data_map):
        self.template_string = template_string
        self.value = ""

        def extract_segment(segment):
            # Strip the braces
            return segment[2:len(segment) - 2]

        # Data should be a dictionary
        for key in data_map.keys():
            unwrapped_key = extract_segment(template_string)
            # Check if the template contains the value
            if unwrapped_key in data_map:
                self.value = data_map[key]


class ConditonalStatement(Statement):
    """A statement to evaluate a conditional branching."""

    def __init__(self, template_string, data_map):
        self.template_string = template_string
        self.value = ""

        def extract_segment(segment):
            # Strip the braces and if
            return segment[5:len(segment) - 2]
        parts = re.split("({{[#/]*\w+(?:\s\w+)*}})", self.template_string)
        # First is empty for some reason...
        # First will always be of form {{#if boolean}}
        boolean_eval = extract_segment(parts[1])
        if boolean_eval:
            self.value = parts[2].strip()
        else:
            self.value = parts[4].strip()


class LoopStatement(Statement):
    """A statement to evaluate a loop."""

    def __init__(self, template_string, data_map):
        self.template_string = template_string
