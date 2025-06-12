from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError('All leaf nodes must have a tag.')
        if not self.children:
            raise ValueError('All leaf nodes must have a children.')
        else:
            child = ''
            html_string = f'<{self.tag}>{child}</{self.tag}>'
            for i in self.children:

            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'






    def __eq__(self, value):
        return self.tag == value.tag and self.value == value.value and self.props == value.props