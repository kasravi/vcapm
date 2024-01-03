import os
import json

root_readme_path = 'readme.md'  # Path to the root README file
meta_data_start_tag = '<!---metadata'
meta_data_end_tag = '/metadata--->'

# Function to parse JSON metadata from a readme.md file
def parse_readme_metadata(readme_path):
    with open(readme_path, 'r') as file:
        content = file.read()
        print("-----------------")
        print(content)
        print("-----------------")
        metadata_start = content.find(meta_data_start_tag)
        metadata_end = content.find(meta_data_end_tag, metadata_start)
        print(metadata_start, metadata_end)
        if metadata_start != -1 and metadata_end != -1:
            metadata = content[metadata_start + len(meta_data_start_tag):metadata_end]
            metadata_dict = json.loads(metadata)
            return metadata_dict
    return None

# Function to generate a table row from metadata
def generate_table_row(metadata):
    row = f"| {metadata['type']} | {metadata['title']} | {metadata['take']} | {metadata['status']} | {metadata['progress']}% | {', '.join(metadata['tags']) if 'tags' in metadata else ''} |\n"
    return row

# Function to traverse directories, find readme files, and generate table content
def generate_table_content():
    table_content = "| Type | Title | Take | Status | Progress | Tags |\n|------|-------|------|--------|----------|------|\n"
    for root, dirs, files in os.walk('.'):
        if 'readme.md' in files:
            readme_path = os.path.join(root, 'readme.md')
            metadata = parse_readme_metadata(readme_path)
            if metadata:
                table_content += generate_table_row(metadata)
    return table_content

# Function to update the root README file with the generated table content
def update_root_readme(table_content):
    with open(root_readme_path, 'r+') as root_readme:
        content = root_readme.read()
        table_start = content.find('| Type | Title')
        table_end = content.find('|', table_start + 1)
        updated_content = content[:table_start] + table_content + content[table_end:]
        root_readme.seek(0)
        root_readme.write(updated_content)
        root_readme.truncate()

# Generate table content and update the root README
table_content = generate_table_content()
update_root_readme(table_content)
