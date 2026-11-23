# source-to-requirements

A read-only source-to-requirements skill for Codex-compatible agents. No third-party dependencies or executable scripts.

## Install
Copy the `source-to-requirements` directory to `~/.agents/skills/` (user-level) or `<repo>/.agents/skills/` (project-level). Restart your agent session if it does not discover new skills immediately.

## Usage
`$source-to-requirements Analyze the HOME-key interception implementation in this Android 14 checkout. mode: standard. Produce requirements and acceptance scenarios with source evidence.`

Modes: quick, standard (default), deep. Source files must be available in the agent's workspace. This skill does not itself inspect a repository until invoked with access to it.
