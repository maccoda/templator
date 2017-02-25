import logging
from statements import Parser


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Template:
    """docstring for Template."""

    def __init__(self, file_name):
        logger.debug("Opening " + file_name + " for template creation")
        # self.content = ""
        # # Mapping between content in template to final content
        # self.map = dict()
        # Open the file and lets start the templating
        with open(file_name, encoding="utf-8") as f:
            self.parser = Parser(f.read())
        #     self.content = f.read()
        #     # Want to capture everything in double braces
        #     # NOTE To escape braces in string need to double up
        #     regex = re.compile("{{[#/]*\w+(?:\s\w+)*}}")
        #     segments = regex.findall(self.content)
        #     for match in segments:
        #         self.map[match] = ""
        #     logger.debug("The built map is: ", self.map)

    # This function will take the data and will open the file here
    def render(self, data):

        return self.parser.render(data)


if __name__ == '__main__':
    import os
    print("Welcome to the templating engine built by you")
    print("We are in " + os.getcwd())
    logging.basicConfig(level=logging.DEBUG)
    template = Template("test_resources/test_variable.tmpl")
    template.render({"name": "Eva", "home_town": "Melbourne"})
