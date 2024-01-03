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
    row = f"<td> {metadata['type']} </td><td> { tabs}<a href='{path}'>{metadata['title']}</a> </td><td> {metadata['take']} </td><td> {metadata['status']} </td><td> {metadata['progress']}% </td><td> {', '.join(metadata['tags']) if 'tags' in metadata else ''} </td>"
    return row

def generate_html_table_content():
    html_table_content = "<table><thead><tr><th>Type</th><th>Title</th><th>Take</th><th>Status</th><th>Progress</th><th>Tags</th></tr></thead><tbody>"
    for root, dirs, files in os.walk('.'):
        if 'readme.md' in files:
            readme_path = os.path.join(root, 'readme.md')
            metadata = parse_readme_metadata(readme_path)
            if metadata:
                level = len([a for a in root.split(os.sep) if a == "e"])
                row = generate_table_row(metadata, level, readme_path)
                # Apply conditional styling based on metadata (for example, if status is 'complete')
                if metadata.get('type') == 'epic':
                    html_table_content += f'<tr style="color: green;">{row}</tr>'
                else:
                    html_table_content += f'<tr>{row}</tr>'
    html_table_content += "</tbody></table>"
    return html_table_content

html_table_content = generate_html_table_content()

with open('readme.md', 'r+') as root_readme:
    content = root_readme.read()
    tree_start = content.find('<!--- Table Start -->')
    tree_end = content.find('<!--- Table End -->', tree_start + 1)
    updated_content = content[:tree_start + len('<!--- Table Start -->')] + "\n" + html_table_content + "\n" + content[tree_end:]
    root_readme.seek(0)
    root_readme.write(updated_content)
    root_readme.truncate()

print("Root README updated successfully with HTML tree!")