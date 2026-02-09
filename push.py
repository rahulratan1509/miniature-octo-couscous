import subprocess
from datetime import datetime

def git_push():
    msg = f"Auto commit {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", msg], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

    print("🚀 Pushed to GitHub successfully.")


if __name__ == "__main__":
    git_push()
