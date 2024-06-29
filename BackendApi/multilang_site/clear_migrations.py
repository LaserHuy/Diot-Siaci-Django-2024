import os

for root, dirs, files in os.walk('.'):
    if 'migrations' in dirs:
        migration_dir = os.path.join(root, 'migrations')
        for file in os.listdir(migration_dir):
            if file != '__init__.py' and file.endswith('.py'):
                os.remove(os.path.join(migration_dir, file))
