"""GitHub API client for fetching public user data."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any

import requests

API_BASE = "https://api.github.com"


@dataclass
class Repo:
    name: str
    description: str
    stars: int
    forks: int
    language: str | None
    url: str


@dataclass
class Profile:
    login: str
    name: str | None
    bio: str | None
    avatar_url: str | None
    followers: int
    following: int
    public_repos: int
    location: str | None
    blog: str | None
    company: str | None
    total_stars: int = 0
    languages: dict[str, int] = field(default_factory=dict)
    top_repos: list[Repo] = field(default_factory=list)


class GitHubClient:
    """Minimal client around the public GitHub REST API."""

    def __init__(self, token: str | None = None) -> None:
        self.session = requests.Session()
        token = token or os.getenv("GITHUB_TOKEN")
        headers = {"Accept": "application/vnd.github+json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self.session.headers.update(headers)

    def _get(self, path: str, **params: Any) -> Any:
        resp = self.session.get(f"{API_BASE}{path}", params=params, timeout=20)
        resp.raise_for_status()
        return resp.json()

    def fetch_user(self, username: str) -> dict[str, Any]:
        return self._get(f"/users/{username}")

    def fetch_repos(self, username: str) -> list[dict[str, Any]]:
        repos: list[dict[str, Any]] = []
        page = 1
        while True:
            batch = self._get(
                f"/users/{username}/repos",
                per_page=100,
                page=page,
                sort="updated",
            )
            if not batch:
                break
            repos.extend(batch)
            if len(batch) < 100:
                break
            page += 1
        return repos

    def build_profile(self, username: str, top_n: int = 5) -> Profile:
        user = self.fetch_user(username)
        repos_raw = [r for r in self.fetch_repos(username) if not r.get("fork")]

        total_stars = sum(r.get("stargazers_count", 0) for r in repos_raw)
        languages: dict[str, int] = {}
        for r in repos_raw:
            lang = r.get("language")
            if lang:
                languages[lang] = languages.get(lang, 0) + 1

        repos_sorted = sorted(
            repos_raw, key=lambda r: r.get("stargazers_count", 0), reverse=True
        )
        top_repos = [
            Repo(
                name=r["name"],
                description=r.get("description") or "",
                stars=r.get("stargazers_count", 0),
                forks=r.get("forks_count", 0),
                language=r.get("language"),
                url=r.get("html_url", ""),
            )
            for r in repos_sorted[:top_n]
        ]

        return Profile(
            login=user["login"],
            name=user.get("name"),
            bio=user.get("bio"),
            avatar_url=user.get("avatar_url"),
            followers=user.get("followers", 0),
            following=user.get("following", 0),
            public_repos=user.get("public_repos", 0),
            location=user.get("location"),
            blog=user.get("blog"),
            company=user.get("company"),
            total_stars=total_stars,
            languages=dict(
                sorted(languages.items(), key=lambda kv: kv[1], reverse=True)
            ),
            top_repos=top_repos,
        )
