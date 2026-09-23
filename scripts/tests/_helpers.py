"""Shared helpers for the scripts unit-test suite.

The script files under scripts/ are hyphenated and not importable as normal
modules, so they are loaded by path via load_module(). The git-backed
diff tests share a small repo setup so every test exercises the same
bootstrap.
"""

import importlib.util
import subprocess


def load_module(path, name):
    """Import a Python file by filesystem path and return its module object."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def init_git_repo(repo):
    """Initialize a disposable git repo with a committer identity set."""
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "tester"], cwd=repo, check=True)


def commit_all(repo, message="wip"):
    """Stage and commit everything in repo, so diff-based tests have history."""
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", message], cwd=repo, check=True)
