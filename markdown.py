import mammoth
import pandoc
import os

# Path to the input DOCX file
docx_file_path = "D:/Office/Marker/Test_marker.docx"

# Path to the output directory
output_dir = "D:/Office/Marker"

# Function to convert HTML to Markdown using Pandoc
def convert_html_to_markdown(input_html_file, output_md_file):
    command = f"pandoc -i {input_html_file} -o {output_md_file}"
    os.system(command)

# Convert DOCX to HTML using Mammoth
with open(docx_file_path, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html_output = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion

# Save HTML output to output_dir as result.html
html_file_path = os.path.join(output_dir, "result.html")
with open(html_file_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_output)

# Convert HTML to Markdown using Pandoc
output_file_path = os.path.join(output_dir, "result.md")

convert_html_to_markdown(html_file_path, output_file_path)


