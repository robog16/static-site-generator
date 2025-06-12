from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(None, tag=None, value=None, props=None)

    def to_html(self):
        if not self.value:
            raise ValueError('All leaf nodes must have a value.')
        if not self.tag:
            return f'{self.value}'
        else:
            return f'"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"'

    def __eq__(self, value):
        return self.tag == value.tag and self.value == value.value and self.props == value.props
