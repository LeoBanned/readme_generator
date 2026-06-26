# readme-gen 📝

> Generate a **beautiful GitHub profile README** from your public data — in one command.

`readme-gen` fetches your public GitHub profile (followers, total stars, top languages, featured repositories) and renders a polished `README.md` with badges, a language bar, and your best projects. Perfect for your profile repo (`yourname/yourname`).

## ✨ Features

- 📊 Auto-built **stat badges** (followers, total stars, public repos)
- 🌈 **Top languages** bar chart from your repositories
- ⭐ **Featured projects** ranked by stars
- 🌐 Website / location / company line
- 🚀 Single command, zero config — works without a token

## 📦 Installation

```bash
pip install -r requirements.txt
# or install as a CLI tool
pip install .
```

## 🔧 Usage

```bash
# Preview in the terminal
readme-gen torvalds --preview

# Write to README.md
readme-gen torvalds -o README.md

# Customize number of featured repos
readme-gen torvalds --top 8

# Use a token to raise API rate limits
export GITHUB_TOKEN=ghp_xxx
readme-gen LeoBanned
```

If you don't install the package, run it as a module:

```bash
python -m readme_gen.cli torvalds --preview
```

## 🧩 Options

| Option | Description |
|---|---|
| `--output, -o` | Output file path (default `README.md`) |
| `--top, -t` | Number of featured repositories (default `5`) |
| `--token` | GitHub token, or set `GITHUB_TOKEN` env var |
| `--preview` | Print to the console instead of writing a file |

## 📁 Project structure

```
readme_gen/
  __init__.py        # package metadata
  github_client.py   # GitHub REST API client + data models
  generator.py       # Markdown rendering
  cli.py             # Typer-based CLI
```

## 🤝 Contributing

PRs welcome! Good first issues are tagged `good first issue`. Ideas: theme support, SVG charts, GitHub Action to auto-update your profile daily.

## 📄 License

MIT — see [LICENSE](LICENSE).
