# src/scaffold/generator.py
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

def create_project(project_name: str, target_dir: str = "."):
    """
    Generates a new Python project from templates.
    """
    # 1. Set up Jinja2 environment
    # This tells Jinja2 where to find our template files
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True
    )
    # A custom filter to make names Python-friendly (e.g., "my-app" -> "my_app")
    env.filters['slugify'] = lambda value: value.lower().replace(" ", "_").replace("-", "_")

    # 2. Create the main project directory
    project_path = os.path.join(target_dir, project_name)
    os.makedirs(project_path, exist_ok=True)
    print(f"✅ Created project directory: {project_path}")

    # 3. Create the src sub-directory
    src_path = os.path.join(project_path, "src", project_name.replace("-", "_"))
    os.makedirs(src_path, exist_ok=True)
    print(f"✅ Created source directory: {src_path}")

    # 4. Render and write the files
    # Top-level files
    render_and_write(env, "pyproject.toml.j2", project_path, "pyproject.toml", project_name=project_name)
    render_and_write(env, "README.md.j2", project_path, "README.md", project_name=project_name)
    render_and_write(env, ".gitignore.j2", project_path, ".gitignore", project_name=project_name)

    # Files inside src directory
    render_and_write(env, "main.py.j2", src_path, "main.py", project_name=project_name)

    # Create __init__.py file (it's empty, so no template needed)
    with open(os.path.join(src_path, "__init__.py"), "w") as f:
        f.write("")
    print(f"✅ Created file: {os.path.join(src_path, '__init__.py')}")


def render_and_write(env: Environment, template_name: str, output_path: str, output_filename: str, **context):
    """
    Helper function to render a template and write it to a file.
    """
    template = env.get_template(template_name)
    rendered_content = template.render(**context)
    filepath = os.path.join(output_path, output_filename)
    with open(filepath, "w") as f:
        f.write(rendered_content)
    print(f"✅ Created file: {filepath}")
