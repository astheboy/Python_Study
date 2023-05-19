import tabula
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_filename = "table.pdf"
relative_path = os.path.join(script_dir, pdf_filename)
absolute_path = os.path.abspath(relative_path)

print(relative_path)
print(absolute_path)

# Extract table from pdf
df = tabula.read_pdf(relative_path, pages="1", multiple_tables=True)
print(df)
