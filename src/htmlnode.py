from enum import Enum

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        children = ",".join(self.children) if self.children != None else ""
        props = ",".join("=".join((key, val)) for (key, val) in self.props.items())
        return f"HTMLNode({self.tag}, {self.value}, [{children}],{self.props_to_html()})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props = ""

        if self.props:
            for prop in self.props:
                value = self.props[prop]
                props += f' {prop}="{value}"'

        return props
