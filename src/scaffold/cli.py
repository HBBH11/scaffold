# src/scaffold/cli.py
import click
import os
from .generator import create_project # <-- Import our new function

@click.group()
def cli():
    """A simple CLI tool to scaffold new Python projects."""
    pass

@cli.command()
@click.argument('project_name')
def create(project_name):
    """Creates a new Python project."""
    click.echo(f"🚀 Creating project: {project_name}")
    
    # Get the current directory (where the user is running the command)
    output_dir = os.getcwd()
    
    # Call our generator function
    create_project(project_name, target_dir=output_dir)
    
    click.echo(f"\n✨ Project '{project_name}' created successfully!")
    click.echo(f"Next steps:")
    click.echo(f"  1. cd {project_name}")
    click.echo(f"  2. python -m venv .venv")
    click.echo(f"  3. .venv\\Scripts\\Activate")
    click.echo(f"  4. pip install -e .")
    click.echo(f"  5. python -m {project_name.replace('-', '_')}.main")

if __name__ == '__main__':
    cli()