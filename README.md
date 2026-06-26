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

## 📄 License

MIT — see [LICENSE](LICENSE).


<p align="center">
  <a href="https://github.com/LeoBanned"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=800&center=true&vCenter=true&width=600&lines=Hi%2C%20I%27m%20LeoBanned%3BWelcome%20to%20my%20GitHub" alt="header"/></a>
</p>

<p align="center">
  <a href="https://github.com/LeoBanned"><img src="https://img.shields.io/badge/Followers-1-1f6feb?style=for-the-badge&logo=github&logoColor=white" alt="Followers"/></a> <a href="https://github.com/LeoBanned"><img src="https://komarev.com/ghpvc/?username=LeoBanned&style=for-the-badge&color=blueviolet&label=PROFILE+VIEWS" alt="Profile Views"/></a>
</p>

<p align="center">
  <a href="https://github.com/LeoBanned"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
</p>

<h3 align="center">📈 GitHub Stats</h3>
<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=LeoBanned&show_icons=true&count_private=true&hide_border=true&theme=tokyonight" alt="stats"/>
  <img height="165" src="https://streak-stats.demolab.com?user=LeoBanned&hide_border=true&theme=tokyonight" alt="streak"/>
</p>
<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=LeoBanned&layout=compact&hide_border=true&langs_count=8&theme=tokyonight" alt="top languages"/>
</p>

<h3 align="center">📅 Contribution Graph</h3>
<p align="center">
  <a href="https://github.com/LeoBanned"><img src="https://github-readme-activity-graph.vercel.app/graph?username=LeoBanned&theme=tokyo-night&hide_border=true&area=true&radius=8" alt="activity graph" width="95%"/></a>
</p>

<h3 align="center">⭐ Featured Projects</h3>
<p align="center">
  <a href="https://github.com/LeoBanned/readme_gen"><img src="https://github-readme-stats.vercel.app/api/pin/?username=LeoBanned&repo=readme_gen&hide_border=true&theme=tokyonight" alt="readme_gen"/></a>
  <a href="https://github.com/LeoBanned/pirate-station-bots"><img src="https://github-readme-stats.vercel.app/api/pin/?username=LeoBanned&repo=pirate-station-bots&hide_border=true&theme=tokyonight" alt="pirate-station-bots"/></a>
  <a href="https://github.com/LeoBanned/pirate-station-hv"><img src="https://github-readme-stats.vercel.app/api/pin/?username=LeoBanned&repo=pirate-station-hv&hide_border=true&theme=tokyonight" alt="pirate-station-hv"/></a>
  <a href="https://github.com/LeoBanned/pirate-station-cracks"><img src="https://github-readme-stats.vercel.app/api/pin/?username=LeoBanned&repo=pirate-station-cracks&hide_border=true&theme=tokyonight" alt="pirate-station-cracks"/></a>
</p>

<p align="center"><sub>✨ Generated with <a href="https://github.com/topics/readme-generator">readme-gen</a></sub></p>

