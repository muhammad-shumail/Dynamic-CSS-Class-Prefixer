from bs4 import BeautifulSoup

def add_prefix_to_classes(input_file, output_file_prefix="modified_"):
    """
    Add a prefix to class attributes in an HTML file and save the modified content.

    Args:
        input_file (str): Path to the input HTML file.
        output_file_prefix (str, optional): Prefix to be added to the output file name.
                                           Defaults to "modified_".
    """
    try:
        # Read the HTML file
        with open(input_file, "r") as file:
            html_content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Print original and modified classes
        print("Original Classes => Modified Classes")

        # Add prefix to class attributes
        for tag in soup.find_all(class_=True):
            original_classes = tag["class"]
            modified_classes = [f"mod-{cls}" for cls in original_classes]
            tag["class"] = modified_classes

            # Print classes and their modified versions
            print(f"{original_classes} => {modified_classes}")

        # Save the modified HTML content
        output_file = f"{output_file_prefix}{input_file}"
        with open(output_file, "w") as file:
            file.write(str(soup))

        print(f"\nModification complete. Modified HTML saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_file_path = "index.html"
add_prefix_to_classes(input_file_path)
