🚀 Scaffold
A powerful, simple, and fast command-line tool to scaffold new Python projects in seconds. Stop wasting time on boilerplate and start building.

License: MITPython 3.8+

Why Scaffold?
Starting a new Python project often means repeating the same tedious steps: creating directories, writing a pyproject.toml, setting up a src layout, and creating a .gitignore. Scaffold automates all of that for you with a single command, giving you a clean, modern, and production-ready project structure every time.

✨ Installation
Install Scaffold with a single command using pip:

pip install scaffold-cli
🚀 Quick Start
Creating a new project is as simple as running one command.

bash

Line Wrapping

Collapse
Copy
1
scaffold create my-awesome-app
Watch it happen!
The tool will instantly create a new directory with a complete project structure, giving you clear feedback along the way.


Line Wrapping

Collapse
Copy
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
🚀 Creating project: my-awesome-app
✅ Created project directory: ./my-awesome-app
✅ Created source directory: ./my-awesome-app/src/my_awesome_app
✅ Created file: ./my-awesome-app/pyproject.toml
✅ Created file: ./my-awesome-app/README.md
✅ Created file: ./my-awesome-app/.gitignore
✅ Created file: ./my-awesome-app/src/my_awesome_app/main.py
✅ Created file: ./my-awesome-app/src/my_awesome_app/__init__.py

✨ Project 'my-awesome-app' created successfully!
Next steps:
  1. cd my-awesome-app
  2. python -m venv .venv
  3. .venv\Scripts\Activate
  4. pip install -e .
  5. python -m my_awesome_app.main
📁 What's Generated?
Scaffold creates a modern Python project layout that follows best practices.


Line Wrapping

Collapse
Copy
1
2
3
4
5
6
7
8
my-awesome-app/
├── .gitignore
├── README.md
├── pyproject.toml
└── src/
    └── my_awesome_app/
        ├── __init__.py
        └── main.py
src layout: Prevents many common packaging issues.
pyproject.toml: The modern standard for defining Python projects.
.gitignore: Pre-configured to ignore common Python junk.
main.py: A ready-to-run entry point for your application.
🗺️ Roadmap
Scaffold is just getting started. Here's what we're planning next:

 Interactive Templates: Choose from different project templates (e.g., basic, fastapi, cli-tool).
 Automatic Git Initialization: Automatically run git init and make an initial commit.
 Advanced Customization: Add options for license choice, dependency management (Poetry/Pip-tools), and more.
 Plugin System: Allow users to create and share their own custom templates.
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

📜 License
Distributed under the MIT License. See LICENSE for more information.

Made with ❤️ by HBBH11


