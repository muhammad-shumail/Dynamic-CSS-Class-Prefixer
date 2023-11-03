import re

def add_prefix_to_css_classes(input_file, output_file_prefix="modified_"):
    """
    Add a prefix to CSS class names in a CSS file and save the modified content.

    Args:
        input_file (str): Path to the input CSS file.
        output_file_prefix (str, optional): Prefix to be added to the output file name.
                                           Defaults to "modified_".
    """
    try:
        # Read the CSS file
        with open(input_file, "r") as file:
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
        output_file = f"{output_file_prefix}{input_file}"
        with open(output_file, "w") as file:
            file.write(modified_css)

        print(f"\nModification complete. Modified CSS saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_css_file_path = "styles.css"
add_prefix_to_css_classes(input_css_file_path)
