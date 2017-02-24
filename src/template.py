import re


class Template:
    """docstring for Template."""

    def __init__(self, file_name):
        self.content = ""
        # Mapping between content in template to final content
        self.map = dict()
        # Open the file and lets start the templating
        with open(file_name, encoding="utf-8") as f:
            self.content = f.read()
            # Want to capture everything in double braces
            # NOTE To escape braces in string need to double up
            regex = re.compile("{{[#/]*\w+(?:\s\w+)*}}")
            segments = regex.findall(self.content)
            for match in segments:
                self.map[match] = ""
            print("The built map is: ", self.map)

    # This function will take the data and will open the file here
    def render(self, data):

        def extract_segment(segment):
            print(segment)
            return segment[1:len(segment)]

        def wrap_for_comparison(segment):
            return "{{" + segment + "}}"

        def replace_with_evaluated_content(key, eval_content):
            print("replacing", key, "with", eval_content)
            self.content = self.content.replace(key, eval_content)

        # Data should be a dictionary
        for key in data.keys():
            print("Current key", wrap_for_comparison(key))
            wrapped_key = wrap_for_comparison(key)
            # Check if the template contains the value
            if wrapped_key in self.map:
                self.map[wrapped_key] = data[key]
                replace_with_evaluated_content(wrapped_key, data[key])
            else:
                print(key, "is not present!!!")

        return self.content


if __name__ == '__main__':
    print("Welcome to the templating engine built by you")
    template = Template("test.tmpl")
    template.render({"name": "Eva", "home_town": "Melbourne"})
