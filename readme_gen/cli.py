"""Command-line interface for readme-gen."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel

from .github_client import GitHubClient
from .generator import render_readme

app = typer.Typer(
    add_completion=False,
    help="Generate a beautiful GitHub profile README from your public data.",
)
console = Console()


@app.command()
def generate(
    username: str = typer.Argument(..., help="GitHub username to generate for."),
    output: Path = typer.Option(
        Path("README.md"), "--output", "-o", help="Output file path."
    ),
    top_n: int = typer.Option(
        5, "--top", "-t", help="Number of featured repositories to include."
    ),
    token: str = typer.Option(
        None,
        "--token",
        help="GitHub token (or set GITHUB_TOKEN env var) to raise rate limits.",
    ),
    preview: bool = typer.Option(
        False, "--preview", help="Print the result to the console instead of writing."
    ),
) -> None:
    """Fetch USERNAME's public data and render a README.md."""
    client = GitHubClient(token=token)
    with console.status(f"Fetching data for [bold cyan]{username}[/]..."):
        try:
            profile = client.build_profile(username, top_n=top_n)
        except Exception as exc:  # noqa: BLE001
            console.print(f"[bold red]Error:[/] {exc}")
            raise typer.Exit(code=1)

    markdown = render_readme(profile)

    if preview:
        console.print(
            Panel(escape(markdown), title="README.md preview", expand=False)
        )
        return

    output.write_text(markdown, encoding="utf-8")
    console.print(
        f"[bold green]\u2713[/] Wrote {len(markdown)} chars to "
        f"[bold]{output}[/] for [cyan]{profile.login}[/]."
    )


def main() -> None:
    app()


if __name__ == "__main__":
    main()
