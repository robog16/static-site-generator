from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
<<<<<<< HEAD
        super().__init__(None, tag=None, value=None, props=None)
=======
        super().__init__(tag, value, None, props)
>>>>>>> origin/draft/eloquent-smoke

    def to_html(self):
        if not self.value:
            raise ValueError('All leaf nodes must have a value.')
        if not self.tag:
<<<<<<< HEAD
            return f'{self.value}'
        else:
            return f'"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"'
=======
            return self.value
        else:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
>>>>>>> origin/draft/eloquent-smoke

    def __eq__(self, value):
        return self.tag == value.tag and self.value == value.value and self.props == value.props
