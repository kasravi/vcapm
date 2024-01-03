import os
import json

root_readme_path = 'readme.md' 
meta_data_start_tag = '<!---metadata'
meta_data_end_tag = '/metadata--->'

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
    row = f"| {metadata['type']} | { tabs}[{metadata['title']}]({path}) | {metadata['take']} | {metadata['status']} | {metadata['progress']}% | {', '.join(metadata['tags']) if 'tags' in metadata else ''} |\n"
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

html_table_content = generate_table_content()

with open('readme.md', 'r+') as root_readme:
    content = root_readme.read()
    tree_start = content.find('<!--- Table Start -->')
    tree_end = content.find('<!--- Table End -->', tree_start + 1)
    updated_content = content[:tree_start + len('<!--- Table Start -->')] + "\n" + html_table_content + "\n" + content[tree_end:]
    root_readme.seek(0)
    root_readme.write(updated_content)
    root_readme.truncate()

print("Root README updated successfully with the table!")