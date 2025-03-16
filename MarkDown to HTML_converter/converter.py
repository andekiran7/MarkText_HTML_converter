import markdown

def convert_markdown_to_html(md_content):

    return markdown.markdown(md_content, extensions=['extra', 'toc', 'codehilite'])
