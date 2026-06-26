"""Render a Profile into a beautiful Markdown README."""

from __future__ import annotations

from .github_client import Profile


def _header(p: Profile) -> str:
    title = p.name or p.login
    lines = ['<h1 align="center">Hi, I\u2019m ' + title + ' \U0001F44B</h1>']
    if p.bio:
        lines.append('<p align="center"><em>' + p.bio + '</em></p>')
    if p.avatar_url:
        lines.append(
            '<p align="center">'
            '<img src="' + p.avatar_url + '" width="120" '
            'style="border-radius:50%" alt="avatar"/>'
            '</p>'
        )
    return "\n".join(lines)


def _stat_badges(p: Profile) -> str:
    base = "https://img.shields.io/badge"
    parts = [
        f"![Followers]({base}/Followers-{p.followers}-1f6feb?style=for-the-badge&logo=github&logoColor=white)",
        f"![Stars]({base}/Total%20Stars-{p.total_stars}-f1c40f?style=for-the-badge&logo=github&logoColor=white)",
        f"![Repos]({base}/Public%20Repos-{p.public_repos}-2ecc71?style=for-the-badge&logo=github&logoColor=white)",
        f"![Following]({base}/Following-{p.following}-9b59b6?style=for-the-badge&logo=github&logoColor=white)",
    ]
    views = (
        "![Profile Views](https://komarev.com/ghpvc/?username="
        + p.login
        + "&style=for-the-badge&color=blueviolet)"
    )
    return '<p align="center">\n' + "\n".join(parts) + "\n" + views + "\n</p>"


def _lang_bar(p: Profile, top: int = 6) -> str:
    if not p.languages:
        return ""
    items = list(p.languages.items())[:top]
    total = sum(c for _, c in items) or 1
    lines = ['<h3 align="center">\U0001F4CA Top Languages</h3>', "", "```text"]
    for lang, count in items:
        pct = round(count / total * 100)
        filled = "\u2588" * (pct // 5)
        empty = "\u2591" * (20 - pct // 5)
        lines.append(f"{lang:<14}{filled}{empty} {pct}%")
    lines.append("```")
    return "\n".join(lines)


def _top_repos(p: Profile) -> str:
    if not p.top_repos:
        return ""
    lines = ['<h3 align="center">\u2B50 Featured Projects</h3>', ""]
    for r in p.top_repos:
        lang = f" \u00B7 `{r.language}`" if r.language else ""
        desc = f"<br/>{r.description}" if r.description else ""
        lines.append(
            f"- **[{r.name}]({r.url})** \u2605 {r.stars} \u00B7 \u2442 {r.forks}{lang}{desc}"
        )
    lines.append("")
    return "\n".join(lines)


def _socials(p: Profile) -> str:
    parts = []
    if p.blog:
        url = p.blog if p.blog.startswith("http") else f"https://{p.blog}"
        parts.append(f"\U0001F310 [Website]({url})")
    if p.location:
        parts.append(f"\U0001F4CD {p.location}")
    if p.company:
        parts.append(f"\U0001F3E2 {p.company}")
    if not parts:
        return ""
    return '<p align="center">' + "  \u2022  ".join(parts) + "</p>"


def render_readme(p: Profile) -> str:
    """Return a full README.md string for the given profile."""
    blocks: list[str] = [_header(p), ""]

    socials = _socials(p)
    if socials:
        blocks.append(socials)
        blocks.append("")

    blocks.append(_stat_badges(p))
    blocks.append("")

    lang_bar = _lang_bar(p)
    if lang_bar:
        blocks.append(lang_bar)
        blocks.append("")

    repos = _top_repos(p)
    if repos:
        blocks.append(repos)

    blocks.append("---")
    blocks.append(
        '<p align="center"><sub>Generated with \u2764\uFE0F by '
        "[readme-gen](https://github.com/topics/readme-generator)</sub></p>"
    )
    blocks.append("")

    return "\n".join(blocks)
