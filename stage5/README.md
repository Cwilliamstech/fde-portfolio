# Stage 5: MCP Tools for a Construction Scheduler

Two MCP tools that let an AI assistant read job data and draft a crew schedule. Built with FastMCP on synthetic data as part of my 12-stage Forward Deployed Engineering program.

## What it does
- `compile_jobs`: reads `jobs_report.txt` and returns every job's tasks, trades, and due dates, sorted by due date.
- `draft_schedule`: matches each task to the first available crew member (from `crew.txt`) whose trade and availability fit. Each person can be booked only once per date. If nobody fits, the task is marked "no one available."

## How to run
```bash
cd stage5
python3 -m venv .venv && source .venv/bin/activate
pip install "mcp[cli]<2"
mcp dev compiler.py
```
This opens the MCP Inspector, where you can call both tools.

## Design notes
- **Fixed file, least privilege:** each tool reads one hard-coded file, so the AI can't choose to open other files.
- **Draft only:** the scheduler suggests assignments but never finalizes them. A human approves.
- **Single source of truth:** `draft_schedule` calls `compile_jobs()` instead of parsing the jobs file a second time.

## Data
All data is synthetic.