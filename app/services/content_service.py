from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

import markdown


BASE_DIR = Path(__file__).resolve().parents[2]
CONTENT_DIR = BASE_DIR / "content"


class ContentError(Exception):
    """Raised when content files are missing or malformed."""


class ContentLibrary:
    def __init__(self, content_dir: Path | None = None) -> None:
        self.content_dir = content_dir or CONTENT_DIR

    @lru_cache(maxsize=1)
    def get_tree(self) -> list[dict[str, Any]]:
        if not self.content_dir.exists():
            raise ContentError(f"Content directory not found: {self.content_dir}")

        nodes: list[dict[str, Any]] = []
        for item_dir in sorted(path for path in self.content_dir.iterdir() if path.is_dir()):
            meta_path = item_dir / "meta.json"
            if not meta_path.exists():
                continue
            nodes.append(self._load_node(item_dir, ancestors=[]))

        nodes.sort(key=lambda item: item["order"])
        return nodes

    def get_first_leaf(self, nodes: list[dict[str, Any]] | None = None) -> dict[str, Any] | None:
        nodes = nodes or self.get_tree()
        for node in nodes:
            leaf = self._find_first_leaf(node)
            if leaf:
                return leaf
        return None

    def get_node(self, path_slugs: list[str]) -> dict[str, Any]:
        if not path_slugs:
            raise ContentError("Invalid item path.")

        current_level = self.get_tree()
        node: dict[str, Any] | None = None

        for slug in path_slugs:
            node = next((item for item in current_level if item["slug"] == slug), None)
            if not node:
                raise ContentError("The requested item was not found.")
            current_level = node["children"]

        return node

    def get_node_tab_content(
        self, node: dict[str, Any], requested_tab: str | None
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        tabs = node["tabs"]
        if not tabs:
            raise ContentError("This item does not define any tabs.")

        active_tab = next((tab for tab in tabs if tab["code"] == requested_tab), tabs[0])
        tab_path = Path(node["path"]) / active_tab["file"]

        if active_tab["type"] == "markdown":
            return active_tab, {"type": "markdown", "html": self._render_markdown(tab_path)}
        if active_tab["type"] == "quiz":
            return active_tab, {"type": "quiz", "items": self._read_json(tab_path)}
        raise ContentError(f"Unsupported tab type: {active_tab['type']}")

    def _load_node(self, node_dir: Path, ancestors: list[dict[str, str]]) -> dict[str, Any]:
        meta = self._read_json(node_dir / "meta.json")
        declared_children = {child["slug"]: child for child in meta.get("children", [])}

        children: list[dict[str, Any]] = []
        for child_dir in sorted(path for path in node_dir.iterdir() if path.is_dir()):
            child_meta_path = child_dir / "meta.json"
            if not child_meta_path.exists():
                continue

            child_node = self._load_node(
                child_dir,
                ancestors=ancestors
                + [
                    {
                        "code": meta.get("code", ""),
                        "title": meta["title"],
                        "slug": meta["slug"],
                    }
                ],
            )
            declared_meta = declared_children.get(child_node["slug"], {})
            child_node["order"] = declared_meta.get("order", child_node["order"])
            child_node["code"] = declared_meta.get("code", child_node["code"])
            child_node["title"] = declared_meta.get("title", child_node["title"])
            children.append(child_node)

        children.sort(key=lambda item: item["order"])

        path_slugs = [ancestor["slug"] for ancestor in ancestors] + [meta["slug"]]
        breadcrumbs = ancestors + [{"code": meta.get("code", ""), "title": meta["title"], "slug": meta["slug"]}]

        return {
            "code": meta.get("code", ""),
            "title": meta["title"],
            "slug": meta["slug"],
            "order": meta.get("order", 999),
            "description": meta.get("description", ""),
            "path": str(node_dir),
            "tabs": list(meta.get("tabs", [])),
            "children": children,
            "is_leaf": bool(meta.get("tabs")),
            "path_slugs": path_slugs,
            "url_path": "/".join(path_slugs),
            "breadcrumbs": breadcrumbs,
            "search_blob": " ".join(
                [
                    meta.get("code", ""),
                    meta["title"],
                    meta.get("description", ""),
                    " ".join(child["title"] for child in children),
                    " ".join(child["code"] for child in children),
                ]
            ).lower(),
        }

    def _find_first_leaf(self, node: dict[str, Any]) -> dict[str, Any] | None:
        if node["is_leaf"]:
            return node
        for child in node["children"]:
            leaf = self._find_first_leaf(child)
            if leaf:
                return leaf
        return None

    def _read_json(self, file_path: Path) -> Any:
        try:
            with file_path.open("r", encoding="utf-8-sig") as file_obj:
                return json.load(file_obj)
        except FileNotFoundError as exc:
            raise ContentError(f"Missing file: {file_path}") from exc
        except json.JSONDecodeError as exc:
            raise ContentError(f"Invalid JSON in {file_path}") from exc

    def _render_markdown(self, file_path: Path) -> str:
        try:
            raw_text = file_path.read_text(encoding="utf-8-sig")
        except FileNotFoundError as exc:
            raise ContentError(f"Missing file: {file_path}") from exc

        return markdown.markdown(raw_text, extensions=["extra", "tables", "sane_lists", "toc"])
