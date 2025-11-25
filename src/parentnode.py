from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Error: No tag!")
        
        if not self.children:
            raise ValueError("Error: No children!")
        
        children = "".join([child.to_html() for child in self.children])

        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
        