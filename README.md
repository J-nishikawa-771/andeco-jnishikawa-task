# andeco-tasks-nishikawa

---

## リポジトリの目的

日々のタスクをMarkdownで管理し、GitHub Issue・GitHub Projectと連携して運用する。

## 基本運用フロー

1. VS Code で `tasks/FY26/Q4/` 配下のMarkdownファイルを編集する
2. Issue番号を含めてコミット・プッシュする（例：`#1 Add sales tasks`）
3. GitHub ActionsがMarkdownの変更を検知する
4. `sync_md_to_github.py` が自動でGitHub Issueを作成・更新する（実装予定）
5. GitHub ProjectにステータスやDue Dateが反映される

## MarkdownとGitHubの関係

| レイヤー | 役割 |
| --- | --- |
| Markdown | タスク定義・メモの原本 |
| GitHub Issue | 実行単位（タスク1件 = Issue1件） |
| GitHub Project | カンバン表示・ステータス管理 |

- `task_id` でMarkdownタスクとGitHub Issueを紐づける
- 同期後、yamlブロックの `github_issue` フィールドにIssue番号が書き込まれる
- Markdown内の `status` は初期値。ステータスの正はGitHub Project

## ディレクトリ構成

```
tasks/FY26/Q4/
├── 01_management/   management.md
├── 02_sales/        sales.md, hubspot.md
├── 03_projects/     projects.md, asana.md
├── 04_backoffice/   finance_billing.md, people_org.md, information_systems.md
└── 05_others/       others.md
```

## VS Codeでの編集方針

- `tasks/FY26/Q4/` 配下のファイルを編集する
- タスクテンプレートの書式を統一する（下記参照）
- 案件・プロジェクトごとにファイルを分けず、カテゴリファイル内のセクションで管理する
- コミットメッセージには必ずIssue番号を含める（例：`#1 Initialize structure`）

## Claudeを使う範囲

- VS Code上でのMarkdown編集・差分確認
- コミット・プッシュの補助
- HubSpotからの担当案件抽出（owner_id: 162042066）
- Asanaからの担当タスク抽出（ワークスペース：株式会社Andeco、user GID: 1210852746876577）
- GitHub Issue作成・Projectへの追加

## ステータス定義

| ステータス | 意味 |
| --- | --- |
| Backlog | まだ着手しない |
| Todo | やることが確定している |
| In Progress | 作業中 |
| Paused | 一時停止 |
| Waiting | 先方確認待ち・社内確認待ち |
| Done | 完了 |

ステータスの正は **GitHub Project** で管理する。Markdown内の `status` は初期値または参考値。

## task_idのルール

フォーマット：`FY26-Q4-{カテゴリコード}-{番号}`

| カテゴリコード | 対象 |
| --- | --- |
| MG | 経営 |
| SA | 営業 |
| PJ | プロジェクト |
| FB | 財務会計・請求 |
| HR | 人事・組織開発 |
| IS | 情シス |
| OT | その他 |

- 番号は3桁ゼロ埋め（001, 002, ...）
- IDはファイル横断で重複禁止
- 一度付与したtask_idは変更しない

## タスクテンプレート

```md
#### FY26-Q4-XX-001: タスク名

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
