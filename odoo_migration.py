
import os
import xmlrpc.client
import markdown
import re

# Odoo Connection Details
URL = "https://nexsolinfotech.odoo.com"
DB = "nexsolinfotech"
USERNAME = "ceo@nexsolinfotech.com"
PASSWORD = "Tejraj@1103"

# Path to the knowledge base
BASE_PATH = r"c:\Users\tejas\OneDrive\Desktop\Nexsol Web Dev Docs\Nexsol-Nexus"

def connect_odoo():
    print(f"Connecting to {URL}...")
    common = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common')
    uid = common.authenticate(DB, USERNAME, PASSWORD, {})
    if not uid:
        raise Exception("Authentication failed!")
    print(f"Authenticated successfully. UID: {uid}")
    models = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')
    return uid, models

def convert_md_to_html(filepath):
    print(f"Reading: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    # Convert Mermaid blocks to code blocks so they don't break HTML
    text = re.sub(r'```mermaid', '```', text)
    html = markdown.markdown(text, extensions=['extra', 'codehilite'])
    return html

def create_article(models, uid, name, body="", parent_id=None):
    # Search if article already exists to avoid duplicates
    domain = [('name', '=', name)]
    if parent_id:
        domain.append(('parent_id', '=', parent_id))
    
    try:
        existing = models.execute_kw(DB, uid, PASSWORD, 'knowledge.article', 'search', [domain])
    except Exception as e:
        print(f"Error searching for model 'knowledge.article': {e}. Trying 'document.page'...")
        # Fallback for older Odoo versions or different modules
        existing = models.execute_kw(DB, uid, PASSWORD, 'document.page', 'search', [domain])
        model_name = 'document.page'
    else:
        model_name = 'knowledge.article'
    
    vals = {
        'name': name,
        'body': body,
    }
    # For knowledge.article, internal_permission is often required or useful
    if model_name == 'knowledge.article':
        vals['internal_permission'] = 'write'

    if parent_id:
        vals['parent_id'] = parent_id

    if existing:
        print(f"Updating existing article: {name} (ID: {existing[0]})")
        models.execute_kw(DB, uid, PASSWORD, model_name, 'write', [existing[0], vals])
        return existing[0]
    else:
        print(f"Creating new article: {name}")
        return models.execute_kw(DB, uid, PASSWORD, model_name, 'create', [vals])

def migrate_folder(models, uid, path, parent_id=None):
    folder_name = os.path.basename(path)
    print(f"Processing Folder: {path}")
    # Create an article for the folder itself
    current_parent_id = create_article(models, uid, folder_name, parent_id=parent_id)
    
    if not os.path.exists(path):
        print(f"Warning: Folder {path} does not exist. Skipping.")
        return

    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if item.startswith('.') or item in ['Archive', 'Team-Workspace', 'Current-Projects']:
                continue
            migrate_folder(models, uid, item_path, current_parent_id)
        elif item.endswith('.md'):
            article_name = item.replace('.md', '')
            html_body = convert_md_to_html(item_path)
            create_article(models, uid, article_name, body=html_body, parent_id=current_parent_id)

if __name__ == "__main__":
    try:
        uid, models = connect_odoo()
        
        # Create Root article
        root_id = create_article(models, uid, "Nexsol Nexus")
        
        # Start migration from top-level folders
        for folder in ["00-Core-Strategy", "01-Shared-Operations", "02-Departments", "03-Technical-Deep-Dives"]:
            path = os.path.join(BASE_PATH, folder)
            if os.path.exists(path):
                migrate_folder(models, uid, path, root_id)
        
        print("Migration completed successfully!")
    except Exception as e:
        print(f"Error during migration: {e}")
