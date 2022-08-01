
import os
import git


# It's a test related to the blow command.
# git diff $(cat .git/refs/heads/master)..12f86a244ca63e5d47c1a4add5f1408b7da9927e -- content/en/term-a.m

root = os.getcwd()
print("Root dir: ", root)

# Get latest main's hash
repo = git.Repo(search_parent_directories=True)
repo.git.checkout('master')
sha_main = repo.head.object.hexsha
print(sha_main)

# Execute from the repository root directory
repo = git.Repo('.')

# Get all branches 
remote_refs = repo.remote('origin').refs
print(remote_refs)

# Filter 'dev-*'
dev_branches = [b.name for b in remote_refs if 'dev-' in b.name]
dev_branches = [s.replace("origin/", "") for s in dev_branches]
print(dev_branches)

# Get all dev-lang directories
path_content = os.path.join(root, "content")
print("Content dir: ", path_content)

dev_directories = []
for path_content, dirs, files in os.walk(path_content):
    for subdir in dirs:
        if subdir != "en":
            print(os.path.join(path_content, subdir))
            dev_directories.append(os.path.join(path_content, subdir))

print(dev_directories)

# Get localized files
localized_files = []
dev_lang_root = dev_directories[0]
for dev_directories[0], directories, files in os.walk(dev_directories[0], topdown=False):
    for file in files:
        abs_path = os.path.join(dev_directories[0], file)
        print("abs_path: ", abs_path)
        rel_path = os.path.relpath(abs_path, dev_lang_root)
        print("rel_path: ", rel_path)
        localized_files.append(rel_path)

    for dir in directories:
        print(os.path.join(dev_directories[0], dir))

print(localized_files)

# Diff


# Get SHA from the localized file
