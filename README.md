# 🚀 Scaffold

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

> **Stop wasting time on boilerplate. Start building.**

Scaffold is a powerful, elegant command-line tool that generates production-ready Python project structures in seconds. With beautiful terminal output and intelligent defaults, it takes the pain out of project setup so you can focus on what matters—writing great code.

---

## ✨ Why Scaffold?

Starting a new Python project shouldn't feel like a chore. Yet, we've all been there: manually creating directories, copying boilerplate files, setting up configuration, and wrestling with project structure. Scaffold eliminates all of that with a single command.

### Key Features

- **⚡ Lightning Fast** - Generate complete project structures in seconds
- **🎨 Beautiful CLI** - Rich, colorful terminal output with real-time progress feedback
- **📦 Modern Standards** - Follows Python packaging best practices (PEP 517/518)
- **🎯 Multiple Templates** - Choose from pre-built templates or customize your own
- **🔧 Production Ready** - Includes all the essentials: tests, CI/CD, documentation structure
- **📁 Smart Layouts** - Uses the modern `src/` layout to prevent common packaging issues

---

## 📦 Installation

Install Scaffold using pip:

```bash
pip install scaffold-cli
```

**Requirements:** Python 3.8 or higher

---

## 🚀 Quick Start

### Create Your First Project

Generate a new Python project with the default template:

```bash
scaffold create my-awesome-app
```

Watch as Scaffold works its magic:

```
🚀 Creating project 'my-awesome-app' with template 'basic'...
✓ Creating project directory
✓ Creating source directory
✓ Generating pyproject.toml
✓ Setting up test structure
✓ Creating .gitignore
✓ Adding LICENSE file

✨ Project created successfully! ✨
```

### Navigate and Start Coding

```bash
cd my-awesome-app
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

---

## 📖 Usage

### Basic Command

```bash
scaffold create <project-name> [options]
```

### Available Options

| Option | Description | Default |
|--------|-------------|---------|
| `--template, -t` | Choose a project template | `basic` |
| `--author, -a` | Set the project author | Current user |
| `--description, -d` | Add a project description | None |
| `--license, -l` | Choose a license | `MIT` |
| `--python-version` | Set minimum Python version | `3.8` |

### Examples

**Create a web application:**
```bash
scaffold create my-web-app --template fastapi --author "Your Name"
```

**Create a CLI tool:**
```bash
scaffold create my-cli-tool --template cli --description "An awesome CLI tool"
```

**Create with specific Python version:**
```bash
scaffold create my-project --python-version 3.10 --license Apache-2.0
```

---

## 📁 Project Structure

Scaffold generates a clean, modern project layout following best practices:

```
my-awesome-app/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Automated testing
│       └── publish.yml         # Package publishing
├── src/
│   └── my_awesome_app/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml              # Modern Python packaging
└── pytest.ini                   # Test configuration
```

### Why `src/` Layout?

The `src/` layout is considered a best practice because it:
- Prevents common import issues during development
- Ensures tests run against the installed package, not source files
- Clearly separates package code from project metadata
- Is recommended by the Python Packaging Authority (PyPA)

---

## 🎨 Available Templates

Scaffold comes with several built-in templates to suit different project types:

### 📦 Basic (`basic`)
Perfect for libraries and simple applications
- Clean project structure
- Testing setup with pytest
- Basic documentation

### 🌐 FastAPI (`fastapi`)
For building modern web APIs
- FastAPI application structure
- Async/await support
- API documentation with OpenAPI
- Testing with pytest and httpx

### 🖥️ CLI (`cli`)
For command-line applications
- Click framework setup
- Argument parsing
- Help documentation
- Easy distribution as a console script

---

## 🛠️ Development

### Setting Up for Development

Clone the repository and set up your development environment:

```bash
git clone https://github.com/HBBH11/scaffold.git
cd scaffold
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Running with Coverage

```bash
pytest --cov=src --cov-report=html
```

### Code Quality

The project uses several tools to maintain code quality:

```bash
# Format code
black src tests

# Lint code
ruff check src tests

# Type checking
mypy src
```

---

## 🗺️ Roadmap

We're actively working on making Scaffold even better. Here's what's coming:

- [ ] **More Templates** - Django, Flask, Data Science, and more
- [ ] **Custom Templates** - Create and share your own project templates
- [ ] **Interactive Mode** - Step-by-step project configuration wizard
- [ ] **Git Integration** - Automatic initialization and initial commit
- [ ] **Dependency Managers** - Support for Poetry, PDM, and Pipenv
- [ ] **Docker Support** - Optional Dockerfile and docker-compose.yml
- [ ] **Pre-commit Hooks** - Automatic setup of code quality checks
- [ ] **Plugin System** - Extend Scaffold with community plugins

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. **Any contributions you make are greatly appreciated!**

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Write clear, descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Follow the existing code style
- Check that all tests pass before submitting

---

## 🐛 Bug Reports & Feature Requests

Found a bug? Have an idea for a new feature? We'd love to hear from you!

- **Bug Reports**: [Open an issue](https://github.com/HBBH11/scaffold/issues/new?labels=bug)
- **Feature Requests**: [Open an issue](https://github.com/HBBH11/scaffold/issues/new?labels=enhancement)
- **Questions**: [Start a discussion](https://github.com/HBBH11/scaffold/discussions)

---

## 📝 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

This means you can:
- ✅ Use it commercially
- ✅ Modify it
- ✅ Distribute it
- ✅ Use it privately

Just include the original copyright and license notice in any copy of the software.

---

## 🙏 Acknowledgments

Scaffold stands on the shoulders of giants. Special thanks to:

- [Rich](https://github.com/Textualize/rich) - For the beautiful terminal output
- [Click](https://click.palletsprojects.com/) - For the excellent CLI framework
- The Python packaging community for their tireless work on modern standards

---

## 💬 Support

If you find Scaffold helpful, consider:

- ⭐ **Starring the repository** to show your support
- 🐦 **Sharing it** with others who might find it useful
- 💬 **Contributing** to make it even better

---

## 📬 Contact

**Project Maintainer:** [HBBH11](https://github.com/HBBH11)

**Project Link:** [https://github.com/HBBH11/scaffold](https://github.com/HBBH11/scaffold)

---

<div align="center">

**Built with ❤️ using [Rich](https://github.com/Textualize/rich)**

*Scaffold - Because life's too short for boilerplate*

</div>
