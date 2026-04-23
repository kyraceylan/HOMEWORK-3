class ScreenElement:
    def __init__(self, element_type, content):
        self.element_type = element_type
        self.content = content

    def render(self):
        if self.element_type == "h1":
            return f"<h1>{self.content}</h1>"
        elif self.element_type == "p":
            return f"<p>{self.content}</p>"
        else:
            return f"<div>{self.content}</div>"
        
# Example usage
if __name__ == "__main__":
    title = ScreenElement("h1", "Welcome to My Screen")
    paragraph = ScreenElement("p", "This is a simple paragraph on my screen.")
    
    print(title.render())
    print(paragraph.render())
    div = ScreenElement("div", "This is a div element.")
    print(div.render())
        