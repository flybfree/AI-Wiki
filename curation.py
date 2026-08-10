"""Local preference learning and review queue for the AI research wiki."""
from __future__ import annotations

import json
import re
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
MIRROR_ROOT = Path("/home/rich/logseq-brain/pages/ai-research")
STATE_DIR = ROOT / ".curation"
DB_PATH = STATE_DIR / "review.sqlite3"


def _db() -> sqlite3.Connection:
    STATE_DIR.mkdir(exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS decisions (
            path TEXT PRIMARY KEY,
            decision TEXT NOT NULL CHECK(decision IN ('keep', 'reject', 'skip')),
            note TEXT NOT NULL DEFAULT '',
            features TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    db.commit()
    return db


def _frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        import yaml
        value = yaml.safe_load(text[4:end])
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def _body(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    return text


def _tokens(text: str) -> list[str]:
    words = re.findall(r"[a-z][a-z0-9][a-z0-9+.-]{2,}", text.lower())
    stop = {
        "this", "that", "with", "from", "into", "their", "which", "about",
        "these", "those", "using", "have", "more", "than", "will", "model",
        "models", "paper", "summary", "research", "article", "through", "also",
        "such", "based", "often", "first", "only", "each", "other", "where",
    }
    return sorted(set(word for word in words if word not in stop))


def _candidate_paths() -> list[Path]:
    paths: set[Path] = set()
    for directory in ("entities/paper", "concepts/papers", "papers"):
        base = ROOT / directory
        if base.exists():
            paths.update(base.rglob("*_summary.md"))
    return sorted(path for path in paths if path.is_file())


def candidate(path: Path) -> dict[str, Any]:
    text = path.read_text(errors="replace")
    meta = _frontmatter(text)
    body = _body(text)
    title = str(meta.get("title") or "").strip()
    if title.startswith("Summary:"):
        title = title.removeprefix("Summary:").strip()
    reference_title = re.search(r"^-\s*Title:\s*(.+)$", body, re.MULTILINE)
    if reference_title:
        title = reference_title.group(1).strip()
    if not title or title.endswith(".md"):
        linked_title = re.findall(r"^\[\[([^]|]+)(?:\|[^]]+)?\]\]$", body, re.MULTILINE)
        if linked_title:
            title = linked_title[-1].strip()
    if not title or title.endswith(".md"):
        heading = re.search(r"^#\s+Summary:\s*(.+)$", body, re.MULTILINE)
        if not heading:
            heading = re.search(r"^#\s+(?!Summary:)\s*(.+)$", body, re.MULTILINE)
        title = heading.group(1).strip() if heading else path.stem
    source = meta.get("source_url") or meta.get("url") or meta.get("source") or ""
    if not source:
        source_link = re.search(r"\*\*Source\*\*:\s*\[[^]]+\]\(([^)]+)\)", body)
        source = source_link.group(1) if source_link else ""
    tags = meta.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    summary_match = re.search(r"^##\s+Summary\s*$\n(.*?)(?=^##\s+|\Z)", body, re.MULTILINE | re.DOTALL)
    summary = summary_match.group(1) if summary_match else body[:2500]
    takeaways_match = re.search(r"^##\s+(?:Key Takeaways|Key Contributions)\s*$\n(.*?)(?=^##\s+|\Z)", body, re.MULTILINE | re.DOTALL)
    takeaways = takeaways_match.group(1) if takeaways_match else ""
    relative = path.relative_to(ROOT).as_posix()
    return {
        "path": relative,
        "title": title.removeprefix("Summary: ").strip(),
        "source": str(source),
        "tags": [str(tag) for tag in tags] if isinstance(tags, list) else [],
        "preview": re.sub(r"\s+", " ", summary + " " + takeaways).strip()[:900],
        "features": _tokens(title + " " + " ".join(map(str, tags)) + " " + summary + " " + takeaways),
    }


def _decisions(db: sqlite3.Connection) -> dict[str, sqlite3.Row]:
    return {row["path"]: row for row in db.execute("SELECT * FROM decisions")}


def _profile(db: sqlite3.Connection) -> dict[str, Any]:
    rows = list(db.execute("SELECT decision, features FROM decisions WHERE decision != 'skip'"))
    positive = Counter()
    negative = Counter()
    for row in rows:
        bucket = positive if row["decision"] == "keep" else negative
        bucket.update(json.loads(row["features"]))
    return {
        "reviewed": len(rows),
        "kept": sum(row["decision"] == "keep" for row in rows),
        "rejected": sum(row["decision"] == "reject" for row in rows),
        "liked_topics": [word for word, _ in positive.most_common(12)],
        "avoided_topics": [word for word, _ in negative.most_common(12)],
        "positive": positive,
        "negative": negative,
    }


def _score(features: list[str], profile: dict[str, Any]) -> float:
    if not profile["reviewed"]:
        return 0.5
    positive = profile["positive"]
    negative = profile["negative"]
    evidence = 0.0
    for feature in features:
        p = positive[feature]
        n = negative[feature]
        if p or n:
            evidence += (p - n) / (p + n + 2)
    if not features:
        return 0.5
    return round(max(0.02, min(0.98, 0.5 + evidence / min(len(features), 12))), 3)


def score_text(title: str, text: str, tags: list[str] | None = None) -> float:
    """Score a new intake candidate against the learned profile."""
    db = _db()
    learned = _profile(db)
    db.close()
    return _score(_tokens(title + " " + " ".join(tags or []) + " " + text[:5000]), learned)


def learning_status() -> dict[str, Any]:
    """Return the minimum information an intake script needs before filtering."""
    value = profile()
    return {"reviewed": value["reviewed"], "active": value["reviewed"] >= 5}


def list_candidates(status: str = "pending", limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    db = _db()
    decisions = _decisions(db)
    profile = _profile(db)
    result = []
    for path in _candidate_paths():
        item = candidate(path)
        decision = decisions.get(item["path"])
        item["decision"] = decision["decision"] if decision else "pending"
        item["note"] = decision["note"] if decision else ""
        item["updated_at"] = decision["updated_at"] if decision else ""
        item["score"] = _score(item["features"], profile)
        if status == "all" or item["decision"] == status:
            result.append(item)
    db.close()
    result.sort(key=lambda item: (-item["score"], item["title"].lower()))
    return result[max(0, offset) : max(0, offset) + max(1, min(limit, 200))]


def record_decision(path: str, decision: str, note: str = "") -> dict[str, Any]:
    if decision not in {"keep", "reject", "skip"}:
        raise ValueError("decision must be keep, reject, or skip")
    target = (ROOT / path).resolve()
    if not target.is_file() or ROOT not in target.parents or not target.name.endswith("_summary.md"):
        raise ValueError("unknown summary path")
    item = candidate(target)
    now = datetime.now(timezone.utc).isoformat()
    db = _db()
    db.execute(
        """
        INSERT INTO decisions(path, decision, note, features, updated_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(path) DO UPDATE SET
            decision=excluded.decision,
            note=excluded.note,
            features=excluded.features,
            updated_at=excluded.updated_at
        """ ,
        (item["path"], decision, note[:1000], json.dumps(item["features"]), now),
    )
    db.commit()
    db.close()
    return {"path": item["path"], "decision": decision, "updated_at": now}


def delete_rejected(path: str, note: str = "") -> dict[str, Any]:
    """Record rejection, delete the curated wiki page and its Logseq mirror."""
    target = (ROOT / path).resolve()
    if not target.is_file() or ROOT not in target.parents or not target.name.endswith("_summary.md"):
        raise ValueError("unknown summary path")
    if not any(parent.name in {"papers", "entities", "concepts"} for parent in target.parents):
        raise ValueError("only curated paper summaries can be deleted")

    item = candidate(target)
    decision = record_decision(path, "reject", note)
    mirror = MIRROR_ROOT / Path(path)
    removed = []
    for candidate_path in (target, mirror):
        if candidate_path.is_file():
            candidate_path.unlink()
            removed.append(str(candidate_path))

    marker = target.name
    title_marker = f"[[{item['title']}]]"
    for tree in (ROOT, MIRROR_ROOT):
        if not tree.exists():
            continue
        for markdown_file in tree.rglob("*.md"):
            if markdown_file in {target, mirror} or ".git" in markdown_file.parts:
                continue
            original = markdown_file.read_text(errors="replace")
            filtered = "\n".join(
                line for line in original.splitlines()
                if marker not in line and title_marker not in line
            )
            if original.endswith("\n") and filtered:
                filtered += "\n"
            if filtered != original:
                markdown_file.write_text(filtered)

    return {**decision, "removed": removed}


def profile() -> dict[str, Any]:
    db = _db()
    value = _profile(db)
    db.close()
    value.pop("positive", None)
    value.pop("negative", None)
    return value
