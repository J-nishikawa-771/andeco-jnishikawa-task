"""
sync_md_to_github.py

Design skeleton for syncing Markdown task files to GitHub Issues and GitHub Projects.
Full implementation is planned for Issue #2.

Requirements:
  pip install PyGithub python-dotenv

Environment variables (set in .env or GitHub Actions secrets):
  PROJECT_PAT   - Personal Access Token with scopes: repo, project
  GITHUB_REPO   - e.g. "J-nishikawa-771/andeco-jnishikawa-task"
  PROJECT_NUMBER - GitHub Project number (integer)
"""

import os
import re
import sys
from pathlib import Path

# TODO: pip install PyGithub python-dotenv
# from github import Github
# from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TASKS_DIR = Path(__file__).parent.parent / "tasks"

# Regex to extract a task block from Markdown
# Matches: task_id, github_issue, status, due, priority
TASK_ID_PATTERN = re.compile(r"task_id:s*(.+)")
GITHUB_ISSUE_PATTERN = re.compile(r'github_issue:s*"?(.*?)"?$', re.MULTILINE)
STATUS_PATTERN = re.compile(r'status:s*(.+)')
DUE_PATTERN = re.compile(r'due:s*"?(.*?)"?$', re.MULTILINE)
PRIORITY_PATTERN = re.compile(r'priority:s*(.+)')
CATEGORY_PATTERN = re.compile(r'category:s*(.+)')
SUBCATEGORY_PATTERN = re.compile(r'subcategory:s*(.+)')

# ---------------------------------------------------------------------------
# Step 1: Read all tasks/**/*.md files
# ---------------------------------------------------------------------------

def collect_md_files(tasks_dir: Path) -> list[Path]:
    """Recursively collect all .md files under tasks/."""
    # TODO: implement glob walk
    return list(tasks_dir.rglob("*.md"))


# ---------------------------------------------------------------------------
# Step 2: Extract task_id blocks from Markdown
# ---------------------------------------------------------------------------

def extract_tasks(md_path: Path) -> list[dict]:
    """
    Parse a Markdown file and return a list of task dicts.

    Each task dict contains:
      task_id, title, github_issue, status, due, priority,
      category, subcategory, body (full markdown block), file_path, line_start
    """
    # TODO: split file by "#### " headings, then parse yaml block per task
    tasks = []
    return tasks


# ---------------------------------------------------------------------------
# Step 3: Detect tasks where github_issue is empty
# ---------------------------------------------------------------------------

def filter_unsynced(tasks: list[dict]) -> list[dict]:
    """Return tasks that have no github_issue assigned yet."""
    return [t for t in tasks if not t.get("github_issue")]


# ---------------------------------------------------------------------------
# Step 4: Create GitHub Issues
# ---------------------------------------------------------------------------

def create_github_issue(repo, task: dict) -> dict:
    """
    Create a GitHub Issue for the given task.

    Returns updated task dict with github_issue set to the new issue number.

    TODO:
      - Build issue title from task["title"]
      - Build issue body from task["body"] (Background, Acceptance Criteria, Notes)
      - Add labels: category, subcategory, priority
      - Set milestone if applicable
      - Return {"number": issue.number, "url": issue.html_url}
    """
    # repo.create_issue(title=..., body=..., labels=[...])
    pass


# ---------------------------------------------------------------------------
# Step 5: Write back Issue number and URL to Markdown
# ---------------------------------------------------------------------------

def write_back_issue(task: dict, issue_number: int, issue_url: str):
    """
    Update the Markdown file to fill in github_issue field.

    TODO:
      - Read file content
      - Locate the yaml block for this task_id
      - Replace: github_issue: "" -> github_issue: "#<number>"
      - Also replace: project_item_id: "" -> project_item_id: "<item_id>" (after step 6)
      - Write file back
    """
    pass


# ---------------------------------------------------------------------------
# Step 6: Add Issue to GitHub Project
# ---------------------------------------------------------------------------

def add_to_project(project_id: str, issue_node_id: str) -> str:
    """
    Add a GitHub Issue to a GitHub Project (v2) via GraphQL API.

    Returns the project item ID.

    TODO:
      - Use GitHub GraphQL API: addProjectV2ItemById mutation
      - Requires PROJECT_PAT with project scope
      - Return item_id for use in step 7
    """
    # GraphQL mutation: addProjectV2ItemById
    pass


# ---------------------------------------------------------------------------
# Step 7: Set Project item fields (Status, Priority, Due Date, Category)
# ---------------------------------------------------------------------------

def set_project_fields(project_id: str, item_id: str, task: dict):
    """
    Set custom field values on a GitHub Project item.

    TODO:
      - Use GitHub GraphQL API: updateProjectV2ItemFieldValue mutation
      - Fields to set: Status, Priority, Due Date, Category
      - Map task["status"] to project Status field option ID
      - Map task["priority"] to project Priority field option ID
      - Set Due Date if task["due"] is not empty
    """
    pass


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """
    Orchestrate the full sync flow.

    TODO:
      1. load_dotenv()
      2. Authenticate: g = Github(os.environ["PROJECT_PAT"])
      3. repo = g.get_repo(os.environ["GITHUB_REPO"])
      4. files = collect_md_files(TASKS_DIR)
      5. all_tasks = [t for f in files for t in extract_tasks(f)]
      6. unsynced = filter_unsynced(all_tasks)
      7. For each task in unsynced:
           issue = create_github_issue(repo, task)
           write_back_issue(task, issue.number, issue.html_url)
           item_id = add_to_project(PROJECT_ID, issue.node_id)
           set_project_fields(PROJECT_ID, item_id, task)
      8. Commit and push the updated Markdown files
    """
    print("sync_md_to_github.py - design skeleton (not yet implemented)")
    print("See Issue #2 for full implementation.")
    sys.exit(0)


if __name__ == "__main__":
    main()
