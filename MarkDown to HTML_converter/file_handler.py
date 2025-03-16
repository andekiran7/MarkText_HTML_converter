from tkinter import filedialog
def open_file():

    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read(), file_path
    return None, None

def save_file(html_content):

    output_file = filedialog.asksaveasfilename(defaultextension=".html",
                                               filetypes=[("HTML files", "*.html")])
    if output_file:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_content)
        return output_file
    return None
