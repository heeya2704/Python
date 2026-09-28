import os
import shutil
import subprocess

repo_dir = r"c:\Users\heeya\OneDrive\Documents\TOPS\Python\Topic_Assignment"
backup_dir = os.path.join(repo_dir, "scratch", "backup_sessions")

sessions = [f"Session_{i}" for i in range(22, 29)]

print("1. Copying Session 22 to 28 into Topic_Assignment/...")
target_topic_dir = os.path.join(repo_dir, "Topic_Assignment")
os.makedirs(target_topic_dir, exist_ok=True)

for s in sessions:
    src = os.path.join(backup_dir, s)
    dst = os.path.join(target_topic_dir, s)
    
    if os.path.exists(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"   Copied {s} to Topic_Assignment/{s}")

print("\n2. Staging all restored files and new sessions...")
subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)

print("\n3. Committing new session tasks...")
subprocess.run(["git", "commit", "-m", "Add Session 22 to 28 tasks"], cwd=repo_dir, check=True)

print("\n4. Force pushing restored commit history + new sessions to origin main...")
subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=repo_dir, check=True)

print("\nSUCCESS! Repository restored and updated on GitHub.")
