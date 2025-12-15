# src/scaffold/cli.py
import click
import os
from .generator import create_project

@click.group()
def cli():
    """A simple CLI tool to scaffold new Python projects."""
    pass

@cli.command()
@click.argument('project_name')
@click.option(
    '--template', 
    default='basic', 
    help='The project template to use (e.g., basic, fastapi).',
    type=click.Choice(['basic', 'fastapi'], case_sensitive=False)
)
def create(project_name, template):
    """Creates a new Python project."""
    click.echo(f"🚀 Creating project '{project_name}' with template '{template}'...")
    
    # Get the current directory
    output_dir = os.getcwd()
    
    try:
        # Call our generator function with the new template argument
        create_project(project_name, template_name=template, target_dir=output_dir)
        
        click.echo(f"\n✨ Project '{project_name}' created successfully!")
        click.echo(f"Next steps:")
        click.echo(f"  1. cd {project_name}")
        click.echo(f"  2. python -m venv .venv")
        click.echo(f"  3. .venv\\Scripts\\Activate")
        click.echo(f"  4. pip install -e .")
        
        # Give a specific next step for FastAPI
        if template == 'fastapi':
            click.echo(f"  5. uvicorn {project_name.replace('-', '_')}.main:app --reload")
        else:
            click.echo(f"  5. python -m {project_name.replace('-', '_')}.main")

    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        click.echo("Try running 'scaffold create --help' to see available templates.", err=True)


if __name__ == '__main__':
    cli()