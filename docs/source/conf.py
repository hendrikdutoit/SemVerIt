import sys

sys.path.insert(0, "d:\\dropbox\\projects\\SemVerIt\\src")
project = "SemVerIt"
copyright = "2021, Hendrik du Toit"
author = "Hendrik du Toit"
version = "0"
release = "0.0.1"
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "hendrikdutoit",  # Username
    "github_repo": "SemVerIt",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/source/",  # Path in the checkout to the docs root
}
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.autosummary"]
templates_path = ["_templates"]
language = "en"
exclude_patterns = []
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
autosummary_generate = True
autosummary_imported_members = True
