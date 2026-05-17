---
name: slack-client
description: Used when interacting with Slack. 
---

# Slack Client

Interact with Slack (read/send/update/delete messages, threads, files, reactions, channels) using the `slack_client` module in this skill folder.

## To unblock yourself
- Make sure the .env file has the SLACK_BOT_TOKEN set. Prompt the user to provide the token if it's not set.
- If the provided SLACK_BOT_TOKEN doesn't have the required scopes, prompt the user to provide the required scopes.

## Official documentation

For advanced use cases (Block Kit, modals, streaming messages, Socket Mode, OAuth, SCIM), consult:

- **Python SDK docs**: https://slack.dev/python-slack-sdk/
- **Python SDK Web client**: https://slack.dev/python-slack-sdk/web/index.html
- **API method reference**: https://api.slack.com/methods (append method name, e.g. `/chat.postMessage`)
- **Block Kit Builder**: https://app.slack.com/block-kit-builder/
- **Rate limits**: https://api.slack.com/apis/web-api/rate-limits
- **Scopes reference**: https://api.slack.com/scopes
- **SDK source / issues**: https://github.com/slackapi/python-slack-sdk
