from pathlib import Path

from setuptools import find_packages, setup

if __name__ == "__main__":
    base_dir = Path(__file__).parent
    src_dir = base_dir / "src"

    about = {}
    with (src_dir / "{{cookiecutter.project_slug}}" / "__about__.py").open() as f:
        exec(f.read(), about)

    install_requirements = [
        "click",
        "jinja2",
        "pandas",
        "loguru",
        "black",
        "isort",
        "mkdocs",
        "mkdocs-material",
        "mkdocs-table-reader-plugin",
        "pyyaml",
    ]

    setup(
        name=about["__title__"],
        version=about["__version__"],
        description=about["__summary__"],
        url=about["__uri__"],
        author=about["__author__"],
        package_dir={"": "src"},
        packages=find_packages(where="src"),
        include_package_data=True,
        install_requires=install_requirements,
        zip_safe=False,
        entry_points="""
            [console_scripts]
            xxx={{cookicutter.project_slug}}.cli:cli            
        """,
    )
