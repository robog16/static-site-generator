class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise Exception('NotImplementedError')

    def props_to_html(self):
        html_string = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
        return html_string
    
    def __eq__(self, value):
        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
        