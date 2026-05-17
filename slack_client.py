"""
Slack channel CRUD examples using the official slack-sdk.

Requires SLACK_BOT_TOKEN env var (xoxb-...).
"""
import os
import re
import urllib.request
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

_SLACK_URL_RE = re.compile(
    r"https?://[^/]+/archives/(?P<channel>[A-Z0-9]+)/p(?P<ts>\d+)"
    r"(?:\?thread_ts=(?P<thread_ts>[\d.]+))?",
    re.IGNORECASE,
)

def parse_slack_url(url):
    """Extract (channel_id, message_ts, thread_ts) from a /archives/ URL."""
    m = _SLACK_URL_RE.search(url)
    if not m:
        raise ValueError(f"Cannot parse Slack URL: {url}")
    raw = m.group("ts")
    return m.group("channel"), raw[:10] + "." + raw[10:], m.group("thread_ts")

def download_file(token, url_private, dest_path):
    """Download a Slack-hosted file using the bot token for auth."""
    req = urllib.request.Request(url_private, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        Path(dest_path).write_bytes(resp.read())
    return dest_path

if __name__ == "__main__":
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

    # --- Parse a Slack message URL ------------------------------------------
    url = "https://feland.slack.com/archives/C0B440YR8KV/p1778982625353279"
    channel, ts, thread_ts = parse_slack_url(url)
    print(f"Parsed: channel={channel}  ts={ts}")

    # --- READ a message -----------------------------------------------------
    resp = client.conversations_history(channel=channel, latest=ts, inclusive=True, limit=1)
    msg = next((m for m in resp["messages"] if m["ts"] == ts), None)
    if msg:
        print(f"\nMessage: {msg['text'][:200]}")
        for f in msg.get("files", []):
            print(f"  File: {f['name']}  ({f.get('filetype')}, {f.get('size')} bytes)")
            # download_file(client.token, f["url_private_download"], f["name"])

    # --- READ thread replies ------------------------------------------------
    # resp = client.conversations_replies(channel=channel, ts=thread_ts or ts)
    # for m in resp["messages"]:
    #     print(f"  [{m['ts']}] {m['text'][:80]}")

    # --- CREATE a message ---------------------------------------------------
    # resp = client.chat_postMessage(channel=channel, text="Hello from slack_client!")
    # new_ts = resp["ts"]

    # --- UPDATE a message ---------------------------------------------------
    # client.chat_update(channel=channel, ts=new_ts, text="Updated text")

    # --- DELETE a message ---------------------------------------------------
    # client.chat_delete(channel=channel, ts=new_ts)

    # --- UPLOAD a file ------------------------------------------------------
    # client.files_upload_v2(file="report.pdf", channel=channel, title="Report")

    # --- Reactions ----------------------------------------------------------
    # client.reactions_add(channel=channel, name="thumbsup", timestamp=ts)
    # client.reactions_remove(channel=channel, name="thumbsup", timestamp=ts)

    # --- Channel CRUD -------------------------------------------------------
    # client.conversations_create(name="new-channel")
    # client.conversations_info(channel=channel)
    # client.conversations_list(types="public_channel,private_channel")
    # client.conversations_archive(channel=channel)
    # client.conversations_setTopic(channel=channel, topic="New topic")
    # client.conversations_rename(channel=channel, name="renamed")
    # client.conversations_members(channel=channel)
    # client.conversations_join(channel=channel)
    # client.conversations_leave(channel=channel)
    # client.conversations_invite(channel=channel, users="U12345")
