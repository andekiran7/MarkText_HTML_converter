import tkinter as tk
from tkinter import messagebox
import webview  # WebView for real-time preview
from converter import convert_markdown_to_html
from file_handler import open_file, save_file


def update_preview():
    """
    Updates the live preview when Markdown is changed.
    """
    md_content = text_area.get("1.0", tk.END).strip()
    html_content = convert_markdown_to_html(md_content)
    webview.evaluate_js(f'document.body.innerHTML = `{html_content}`')


def open_markdown():
    """
    Opens a Markdown file and loads its content into the text editor.
    """
    content, file_path = open_file()
    if content:
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", content)
        update_preview()


def convert_and_save():
    """
    Converts Markdown entered by the user and allows saving as an HTML file.
    """
    md_content = text_area.get("1.0", tk.END).strip()

    if not md_content:
        messagebox.showwarning("Warning", "Please enter Markdown content before converting.")
        return

    html_content = convert_markdown_to_html(md_content)

    output_file = save_file(html_content)

    if output_file:
        messagebox.showinfo("Success", f"HTML file saved: {output_file}")


def create_gui():
    """
    Creates an advanced GUI with live preview.
    """
    global text_area

    root = tk.Tk()
    root.title("Advanced Markdown to HTML Converter")
    root.geometry("900x600")

    # Create UI elements
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Markdown Text Editor
    text_area = tk.Text(frame, height=20, width=50, font=("Arial", 12))
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    # Buttons Frame
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X)

    btn_open = tk.Button(button_frame, text="Open Markdown", command=open_markdown)
    btn_open.pack(side=tk.LEFT, padx=5, pady=5)

    btn_convert = tk.Button(button_frame, text="Convert & Save HTML", command=convert_and_save)
    btn_convert.pack(side=tk.LEFT, padx=5, pady=5)

    # Live Preview using WebView
    webview.create_window("HTML Preview", "")
    webview.start(debug=False, gui='tkinter', private_mode=True)

    root.mainloop()
