import tabula

# Extract table from pdf
df = tabula.read_pdf(
    "/Users/hanseungryun/Library/CloudStorage/OneDrive-개인/문서/python_study/python_automate/input/table.pdf",
    pages="1",
)

print(df)
