import os

TOTAL = 100

def create_structure():
    for i in range(1, TOTAL + 1):
        folder = f"folder_{i}"
        file = f"file_{i}.py"

        os.makedirs(folder, exist_ok=True)

        path = os.path.join(folder, file)
        with open(path, "w") as f:
            f.write(f'''"""
{file}
Auto-generated boilerplate
"""

def main():
    print("Hello from {file}")

if __name__ == "__main__":
    main()
''')

    print(f"✅ Created {TOTAL} folders with Python boilerplate files.")


if __name__ == "__main__":
    create_structure()
