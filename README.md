# andeco-tasks-nishikawa

---

## Repository Purpose

日々のタスクを管理・メモする

## Basic Operation Flow

1. Edit Markdown files in VS Code under `tasks/FY26/Q4/`
2. Commit and push to GitHub (reference issue number in commit message)
3. GitHub Actions detects changes to `tasks/**/*.md`
4. `sync_md_to_github.py` creates / updates GitHub Issues automatically
5. GitHub Project reflects status, priority, and due dates

## Markdown and GitHub Integration

| Layer | Role |
| --- | --- |
| Markdown | Source of truth for task definitions and notes |
| GitHub Issue | Execution unit — one issue per task |
| GitHub Project | Kanban view and status management |

- `task_id` links a Markdown task to its GitHub Issue
- `github_issue` field in the yaml block stores the issue number after sync
- `status` in Markdown is the initial value; authoritative status lives in GitHub Project

## Directory Structure

```
tasks/FY26/Q4/
├── 01_management/   management.md
├── 02_sales/        sales.md, hubspot.md
├── 03_projects/     projects.md, asana.md
├── 04_backoffice/   finance_billing.md, people_org.md, information_systems.md
└── 05_others/       others.md
```

## VS Code Editing Policy

- Edit task files under `tasks/FY26/Q4/`
- Use the task template format consistently (see below)
- Do not create per-project or per-deal files; use sections within category files
- Commit with issue reference (e.g., `#1 Initialize structure`)

## Claude Usage Scope

- Markdown editing and diff review in VS Code
- Commit / push assistance
- HubSpot deal extraction (owner_id: 162042066)
- Asana task extraction (workspace: 株式会社Andeco, user GID: 1210852746876577)
- GitHub Issue creation and Project management

## Status Definitions

| Status | Meaning |
| --- | --- |
| Backlog | Not started yet |
| Todo | Confirmed to do |
| In Progress | Currently working |
| Paused | Temporarily stopped |
| Waiting | Waiting for client or team response |
| Done | Completed |

Authoritative status is managed in **GitHub Project**. The `status` field in Markdown is the initial value.

## task_id Rules

Format: `FY26-Q4-{CATEGORY}-{NUMBER}`

| Category code | Scope |
| --- | --- |
| MG | Management |
| SA | Sales |
| PJ | Projects |
| FB | Finance and Billing |
| HR | People and Organization |
| IS | Information Systems |
| OT | Others |

- Numbers are zero-padded to 3 digits (001, 002, ...)
- IDs must be unique across all files
- Once assigned, a task_id must not be changed

## Task Template

```md
#### FY26-Q4-XX-001: Task name

\`\`\`yaml
task_id: FY26-Q4-XX-001
category: ...
subcategory: ...
source: manual
source_id: ""
github_issue: ""
project_item_id: ""
status: Todo
due: ""
priority: P2
estimate: ""
\`\`\`

##### Background

背景を記載。

##### Acceptance Criteria

* 完了条件1

##### Notes

* YYYY-MM-DD: メモ
```
