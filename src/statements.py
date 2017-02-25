"""
Module containing all data related to the parsing and evaluating of
statements within a template.
"""

import logging
import re

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Parser:
    """
    The parser to parse the template string and determine which areas are required to be substituted.
    """
    variable_parser = r"{{(\w+)}}"
    # FIXME May still have problems if there is an if within an if
    conditional_parser = r"{{#if (\w+)}}((?:\s|.)+?){{/if}}"
    loop_parser = r"{{#each (\w+)}}((?:\s|.)+?){{/each}}"
    largest_element_parser = r"{{#(\w+)\s\w+}}(?:\s|.)+?\s*{{/\1}}"

    def __init__(self, content):
        self.content = content

    def render(self, data):
        matches = re.finditer(self.largest_element_parser, self.content)

        if not matches:
            return self.content

        for match in matches:
            if match.group(1) == "if":
                conditional_content = re.match(self.conditional_parser, match.group())
                eval_cond = self.__evaluate_conditional(conditional_content, data)
                result = Parser(eval_cond).render(data)
                if result:
                    self.content = self.content.replace(match.group(), result)

            elif match.group(1) == "each":
                loop_content = re.match(self.loop_parser, match.group())
                eval_loop = self.__evaluate_loop(loop_content, data)
                result = Parser(eval_loop).render(data)
                if result:
                    self.content = self.content.replace(match.group(), result)

            else:
                raise Exception
        result = self.__evaluate_variables(self.content, data)
        return result

    def __evaluate_conditional(self, re_capture, data):
        condition = re_capture.group(1)
        alternatives = re_capture.group(2).split("{{#else}}")
        # FIXME Does not check if is in the table, should fail anyway
        if data[condition]:
            return alternatives[0]
        else:
            return alternatives[1]

    def __evaluate_loop(self, re_capture, data):
        iteration = re_capture.group(1)
        internals = re_capture.group(2)

        result = ""
        # FIXME Again no check
        for element in data[iteration]:
            result += self.__evaluate_variables(internals, element)

        return result

    def __evaluate_variables(self, template_string, data):
        matches = re.finditer(self.variable_parser, template_string)
        result = template_string.lstrip()
        for match in matches:
            key = match.group(1)
            result = result.replace(match.group(), data[key])

        return result


