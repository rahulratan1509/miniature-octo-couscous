import subprocess

def git_push():
    commit_msg = input("Enter commit message: ").strip()

    if not commit_msg:
        print("❌ Commit message cannot be empty.")
        return

    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

    print("🚀 Changes committed and pushed successfully.")


if __name__ == "__main__":
    git_push()
