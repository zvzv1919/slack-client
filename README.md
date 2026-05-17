# slack-client

Slack channel CRUD examples using the official [`slack-sdk`](https://github.com/slackapi/python-slack-sdk).

## Setup

```bash
uv sync
cp .env.example .env   # then fill in your token
```

### Required bot token scopes

| Scope | Used for |
|---|---|
| `channels:history` | Reading messages from public channels |
| `channels:read` | Channel info / list |
| `channels:join` | Join public channels |
| `channels:manage` | Create / archive / rename channels |
| `chat:write` | Post / update / delete messages |
| `files:read` | File info / list / download |
| `files:write` | Upload / delete files |
| `groups:history` | Reading messages from private channels |
| `groups:read` | Private channel info |
| `reactions:read` / `reactions:write` | Emoji reactions |
| `users:read` | User lookups |

## Usage

```bash
uv run python slack_client.py
```

The `__main__` block in `slack_client.py` demonstrates every CRUD operation.
Uncomment the ones you need.

### Helpers

```python
from slack_client import parse_slack_url, download_file

# Parse a Slack URL into (channel_id, message_ts, thread_ts)
channel, ts, thread_ts = parse_slack_url("https://workspace.slack.com/archives/C0XXXXX/p1234567890123456")

# Download a Slack-hosted file
download_file(token, url_private, "local_copy.pdf")
```
