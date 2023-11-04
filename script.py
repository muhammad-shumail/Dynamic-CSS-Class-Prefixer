from bs4 import BeautifulSoup
import re

html_file = "index.html"
css_file = "index.css"
prefixer = "mod-"

# Read the HTML file
with open(html_file, "r") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Add prefix to class attributes
for tag in soup.find_all(class_=True):
    tag["class"] = [prefixer + css_class for css_class in tag["class"]]
    print(tag["class"])

# Save the modified HTML content
output_file = f"modified_{html_file}"
with open(output_file, "w") as file:
    file.write(str(soup))
    

# Read the CSS file
with open(css_file, "r") as file:
    css_content = file.read()

# Print original and modified CSS class names
print("Original CSS Classes => Modified CSS Classes")

# Add prefix to class names using regular expressions
modified_css = re.sub(r'\.([a-zA-Z_-]+)', r'.mod-\1', css_content)

# Print CSS classes and their modified versions
original_classes = re.findall(r'\.([a-zA-Z_-]+)', css_content)
modified_classes = re.findall(r'\.([a-zA-Z_-]+)', modified_css)
for original, modified in zip(original_classes, modified_classes):
    print(f"{original} => {modified}")

# Save the modified CSS content
output_file = f"modified_{css_file}"
with open(output_file, "w") as file:
    file.write(modified_css)
