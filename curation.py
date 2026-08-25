"""Local preference learning and review queue for the AI research wiki."""
from __future__ import annotations

import json
import re
import shutil
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
MIRROR_ROOT = Path("/home/rich/logseq-brain/pages/ai-research")
STATE_DIR = ROOT / ".curation"
DB_PATH = STATE_DIR / "review.sqlite3"
MIN_REVIEW_SCORE = 0.60


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
        "finding", "findings", "authors", "across", "while", "introduces",
        "without", "both", "when", "work", "study", "rather", "three", "they",
        "over", "single", "high", "show", "shows", "results", "using", "use",
        "used", "new", "can", "may", "does", "one", "two", "via", "well",
        "toward", "towards", "propose", "proposed", "demonstrates", "demonstrate",
        "achieves", "enables", "provides", "framework", "approach", "method",
        "methods", "performance", "level", "time", "state", "indicating",
    }
    cleaned = {word.strip(".-+") for word in words}
    return sorted(set(word for word in cleaned if word and word not in stop))


_DISPLAY_TOPIC_WORDS = {
    "agent", "agents", "alignment", "benchmark", "benchmarks", "coding",
    "compression", "deception", "diffusion", "embedding", "evaluation",
    "fine-tuning", "governance", "harness", "inference", "interpretability",
    "knowledge", "language", "llm", "memory", "model", "models", "multimodal",
    "moe", "open-source", "planning", "privacy", "quantization", "rag",
    "reasoning", "retrieval", "robotics", "safety", "security", "self-improvement",
    "sycophancy", "tool", "tool-use", "training", "transformer", "vision",
    "world-model",
}


def _candidate_paths(status: str = "pending") -> list[Path]:
    paths: set[Path] = set()
    directories = ("pending/papers",) if status == "pending" else (
        "pending/papers", "entities/paper", "concepts/papers", "papers"
    )
    for directory in directories:
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
    source_reference = re.search(r"^Source:\s*(.+)$", body, re.MULTILINE)
    if not source and source_reference:
        source = source_reference.group(1).strip()
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
        "identity": _identity(source or title),
    }


def _identity(value: str) -> str:
    """Return a stable identity for generated summaries of one source.

    The summarizer appends ``_YYYYMMDD_HHMM`` when it sees an existing output.
    That timestamp is an output-generation detail, not a new paper identity.
    """
    value = Path(str(value).strip()).name
    value = re.sub(r"_summary\.md$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"\.md$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"_\d{8}_\d{4}$", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return re.sub(r"\s+", " ", value).strip()


def _dedupe_candidates(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep one review card per source, without deleting any files."""
    chosen: dict[str, dict[str, Any]] = {}
    decision_rank = {"keep": 0, "reject": 1, "skip": 2, "pending": 3}
    for item in items:
        key = item["identity"]
        current = chosen.get(key)
        if current is None:
            chosen[key] = item
            continue
        current_rank = (decision_rank.get(current["decision"], 3),
                        len(current["path"]), current["path"])
        item_rank = (decision_rank.get(item["decision"], 3),
                     len(item["path"]), item["path"])
        if item_rank < current_rank:
            chosen[key] = item
    return list(chosen.values())


def _decisions(db: sqlite3.Connection) -> dict[str, sqlite3.Row]:
    return {row["path"]: row for row in db.execute("SELECT * FROM decisions")}


def _profile(db: sqlite3.Connection) -> dict[str, Any]:
    # A single paper can have several generated summary paths.  Collapse those
    # records before learning, otherwise duplicate rejects overwhelm the real
    # keep/reject signal.
    grouped: dict[str, tuple[str, str, str]] = {}
    rank = {"keep": 0, "reject": 1, "skip": 2}
    for row in db.execute("SELECT path, decision, features, updated_at FROM decisions"):
        if row["decision"] == "skip":
            continue
        key = _identity(row["path"])
        current = grouped.get(key)
        candidate = (row["decision"], row["features"], row["updated_at"])
        if current is None or (rank[row["decision"]], row["updated_at"]) < (rank[current[0]], current[2]):
            grouped[key] = candidate
    rows = [{"decision": value[0], "features": value[1]} for value in grouped.values()]
    positive = Counter()
    negative = Counter()
    for row in rows:
        bucket = positive if row["decision"] == "keep" else negative
        bucket.update(_tokens(" ".join(json.loads(row["features"]))))
    kept = sum(row["decision"] == "keep" for row in rows)
    rejected = sum(row["decision"] == "reject" for row in rows)
    topics = set(positive) | set(negative)
    preferences = sorted(
        (word for word in topics if positive[word] + negative[word] >= 8),
        key=lambda word: _feature_signal(word, positive, negative, kept, rejected),
        reverse=True,
    )
    return {
        "reviewed": len(rows),
        "kept": kept,
        "rejected": rejected,
        "liked_topics": [word for word in preferences if word in _DISPLAY_TOPIC_WORDS and _feature_signal(word, positive, negative, kept, rejected) > 0][:12],
        "avoided_topics": [word for word in reversed(preferences) if word in _DISPLAY_TOPIC_WORDS and _feature_signal(word, positive, negative, kept, rejected) < 0][:12],
        "positive": positive,
        "negative": negative,
    }


def _feature_signal(feature: str, positive: Counter, negative: Counter, kept: int, rejected: int) -> float:
    """Compare a feature's prevalence in kept and rejected papers."""
    if positive[feature] + negative[feature] < 5:
        return 0.0
    keep_rate = (positive[feature] + 1) / (kept + 2)
    reject_rate = (negative[feature] + 1) / (rejected + 2)
    total = keep_rate + reject_rate
    return (keep_rate - reject_rate) / total if total else 0.0


def _score(features: list[str], profile: dict[str, Any]) -> float:
    if not profile["reviewed"]:
        return 0.5
    positive = profile["positive"]
    negative = profile["negative"]
    evidence = 0.0
    for feature in features:
        evidence += _feature_signal(feature, positive, negative, profile["kept"], profile["rejected"])
    if not features:
        return 0.5
    return round(max(0.02, min(0.98, 0.5 + evidence / min(len(features), 12))), 3)


def _score_with_title(title: str, text: str, tags: list[str], profile: dict[str, Any]) -> float:
    """Score a candidate with stronger weight on title/topic evidence."""
    title_features = _tokens(title)
    body_features = _tokens(" ".join(tags) + " " + text[:5000])
    features = title_features + body_features
    if not features:
        return 0.5
    positive = profile["positive"]
    negative = profile["negative"]
    evidence = 0.0
    weight_total = 0.0
    for feature in features:
        weight = 3.0 if feature in title_features else 1.0
        evidence += weight * _feature_signal(feature, positive, negative, profile["kept"], profile["rejected"])
        weight_total += weight
    return round(max(0.02, min(0.98, 0.5 + evidence / max(weight_total / 2, 1))), 3)


def score_text(title: str, text: str, tags: list[str] | None = None) -> float:
    """Score a new intake candidate against the learned profile."""
    db = _db()
    learned = _profile(db)
    db.close()
    return _score_with_title(title, text, tags or [], learned)


def learning_status() -> dict[str, Any]:
    """Return the minimum information an intake script needs before filtering."""
    value = profile()
    return {"reviewed": value["reviewed"], "active": value["reviewed"] >= 5}


def list_candidates(status: str = "pending", limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    db = _db()
    decisions = _decisions(db)
    profile = _profile(db)
    result = []
    for path in _candidate_paths(status):
        item = candidate(path)
        decision = decisions.get(item["path"])
        if decision and decision["decision"] == "reject":
            continue
        item["decision"] = decision["decision"] if decision else "pending"
        item["note"] = decision["note"] if decision else ""
        item["updated_at"] = decision["updated_at"] if decision else ""
        item["score"] = _score_with_title(item["title"], item["preview"], item["tags"], profile)
        if status == "pending" and item["score"] < MIN_REVIEW_SCORE:
            continue
        if status == "all" or item["decision"] == status:
            result.append(item)
    db.close()
    result = _dedupe_candidates(result)
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
    promoted_path = _promote_pending(path) if decision == "keep" else path
    return {"path": promoted_path, "decision": decision, "updated_at": now}


def _promote_pending(path: str) -> str:
    prefix = "pending/papers/"
    if not path.startswith(prefix):
        return path
    source = ROOT / path
    destination = ROOT / "concepts/papers" / source.name
    destination.parent.mkdir(parents=True, exist_ok=True)
    source.replace(destination)

    mirror_source = MIRROR_ROOT / path
    mirror_destination = MIRROR_ROOT / "concepts/papers" / source.name
    if mirror_source.is_file():
        mirror_destination.parent.mkdir(parents=True, exist_ok=True)
        mirror_source.replace(mirror_destination)
    elif destination.is_file():
        mirror_destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(destination, mirror_destination)
    return destination.relative_to(ROOT).as_posix()


def _validate_deletion(path: str) -> tuple[Path, dict[str, Any], Path]:
    target = (ROOT / path).resolve()
    if not target.is_file() or ROOT not in target.parents or not target.name.endswith("_summary.md"):
        raise ValueError(f"unknown summary path: {path}")
    if not any(parent.name in {"papers", "entities", "concepts"} for parent in target.parents):
        raise ValueError("only curated paper summaries can be deleted")
    return target, candidate(target), MIRROR_ROOT / Path(path)


def _raw_paths_for_summary(path: str) -> list[Path]:
    stem = Path(path).name.removesuffix("_summary.md")
    return [
        ROOT / "raw/papers" / f"{stem}.md",
        ROOT / "raw/summaries" / f"{stem}.md",
        ROOT / "raw/summaries" / f"SUMMARY_{stem}.md",
        MIRROR_ROOT / "papers" / f"{stem}.md",
        MIRROR_ROOT / "raw/papers" / f"{stem}.md",
    ]


def bulk_delete_rejected(paths: list[str], note: str = "") -> dict[str, Any]:
    """Keep selected paths, reject and delete the remaining paths in one operation."""
    unique_paths = list(dict.fromkeys(paths))
    validated = [_validate_deletion(path) for path in unique_paths]
    now = datetime.now(timezone.utc).isoformat()
    db = _db()
    for path, (_, item, _) in zip(unique_paths, validated):
        db.execute(
            """
            INSERT INTO decisions(path, decision, note, features, updated_at)
            VALUES (?, 'reject', ?, ?, ?)
            ON CONFLICT(path) DO UPDATE SET
                decision='reject', note=excluded.note,
                features=excluded.features, updated_at=excluded.updated_at
            """,
            (path, note[:1000], json.dumps(item["features"]), now),
        )
    db.commit()
    db.close()

    removed = []
    markers = []
    for target, item, mirror in validated:
        markers.append((target.name, f"[[{item['title']}]]"))
        for candidate_path in (target, mirror, *_raw_paths_for_summary(item["path"])):
            if candidate_path.is_file():
                candidate_path.unlink()
                removed.append(str(candidate_path))

    for tree in (ROOT, MIRROR_ROOT):
        if not tree.exists():
            continue
        for markdown_file in tree.rglob("*.md"):
            if ".git" in markdown_file.parts:
                continue
            original = markdown_file.read_text(errors="replace")
            filtered = "\n".join(
                line for line in original.splitlines()
                if not any(marker in line or title_marker in line for marker, title_marker in markers)
            )
            if original.endswith("\n") and filtered:
                filtered += "\n"
            if filtered != original:
                markdown_file.write_text(filtered)

    return {"decision": "reject", "deleted_paths": unique_paths, "removed": removed}


def delete_rejected(path: str, note: str = "") -> dict[str, Any]:
    """Record rejection, delete the curated wiki page and its Logseq mirror."""
    return bulk_delete_rejected([path], note)


def profile() -> dict[str, Any]:
    db = _db()
    value = _profile(db)
    db.close()
    value.pop("positive", None)
    value.pop("negative", None)
    return value
