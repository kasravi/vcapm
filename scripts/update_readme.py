import os
import json

root_readme_path = 'readme.md'  # Path to the root README file
meta_data_start_tag = '<!---metadata'
meta_data_end_tag = '/metadata--->'

# Function to parse JSON metadata from a readme.md file
def parse_readme_metadata(readme_path):
    with open(readme_path, 'r') as file:
        content = file.read()
        metadata_start = content.find(meta_data_start_tag)
        metadata_end = content.find(meta_data_end_tag, metadata_start)
        if metadata_start != -1 and metadata_end != -1:
            metadata = content[metadata_start + len(meta_data_start_tag):metadata_end]
            metadata_dict = json.loads(metadata)
            return metadata_dict
    return None

def generate_table_row(metadata, level, path):
    tabs = ('&nbsp;' * (level-1)*2)
    row = f"| { tabs}{metadata['type']} | [{metadata['title']}]({path}) | {metadata['take']} | {metadata['status']} | {metadata['progress']}% | {', '.join(metadata['tags']) if 'tags' in metadata else ''} |\n"
    return row

def generate_table_content():
    table_content = "| Type | Title | Take | Status | Progress | Tags |\n|------|-------|------|--------|----------|------|\n"
    for root, dirs, files in os.walk('.'):
        if 'readme.md' in files:
            readme_path = os.path.join(root, 'readme.md')
            metadata = parse_readme_metadata(readme_path)
            if metadata:
                level = len([a for a in root.split(os.sep) if a == "e"])
                table_content += generate_table_row(metadata, level, readme_path)
    return table_content
# Generate HTML tree content
html_tree_content = generate_table_content()

with open('readme.md', 'w') as root_readme:  # Open in 'w' mode to truncate and write
    root_readme.write(html_tree_content)

print("Root README updated successfully with HTML tree!")