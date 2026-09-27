"""Lightweight arXiv-Sanity-style similarity features for paper intake.

This intentionally uses only the Python standard library. It learns from the
curation decision database, but never makes an acceptance decision by itself.
"""
from __future__ import annotations

import math
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / ".curation" / "review.sqlite3"

_STOPWORDS = {
    "about", "after", "again", "also", "among", "because", "been", "being",
    "between", "could", "does", "each", "from", "have", "into", "more",
    "most", "other", "over", "same", "should", "such", "than", "that",
    "their", "them", "these", "they", "this", "through", "using", "were",
    "which", "while", "with", "would", "paper", "papers", "model", "models",
    "research", "study", "method", "methods", "approach", "based", "show",
    "shows", "result", "results", "provide", "provides", "new", "can", "may",
}


def _tokens(text: str) -> list[str]:
    words = re.findall(r"[a-z][a-z0-9+.-]{2,}", text.lower())
    return [
        word.strip(".-+")
        for word in words
        if word not in _STOPWORDS and len(word) <= 32
    ]


def _text_from_path(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _decision_documents() -> tuple[list[str], list[str]]:
    """Return text documents from exact kept/rejected decision paths."""
    if not DB_PATH.is_file():
        return [], []
    kept: list[str] = []
    rejected: list[str] = []
    try:
        db = sqlite3.connect(DB_PATH)
        rows = db.execute("SELECT path, decision, title, source, preview FROM decisions WHERE decision IN ('keep', 'reject')")
        for relative, decision, stored_title, stored_source, stored_preview in rows:
            text = ""
            if stored_title or stored_source or stored_preview:
                text = " ".join((stored_title or "", stored_source or "", stored_preview or ""))
            path = (ROOT / str(relative)).resolve()
            if path.is_file():
                text = _text_from_path(path)
            if not text:
                continue
            if decision == "keep":
                kept.append(text)
            else:
                rejected.append(text)
        db.close()
    except sqlite3.Error:
        return [], []
    return kept, rejected


def _idf(documents: list[list[str]]) -> dict[str, float]:
    count = len(documents)
    document_frequency: Counter[str] = Counter()
    for document in documents:
        document_frequency.update(set(document))
    return {
        token: math.log((1 + count) / (1 + frequency)) + 1.0
        for token, frequency in document_frequency.items()
    }


def _vector(tokens: list[str], idf: dict[str, float]) -> dict[str, float]:
    frequencies = Counter(tokens)
    norm = math.sqrt(sum((frequency * idf.get(token, 1.0)) ** 2 for token, frequency in frequencies.items()))
    if not norm:
        return {}
    return {
        token: (frequency * idf.get(token, 1.0)) / norm
        for token, frequency in frequencies.items()
    }


def _cosine(left: dict[str, float], right: dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    if len(left) > len(right):
        left, right = right, left
    return sum(value * right.get(token, 0.0) for token, value in left.items())


def _centroid(vectors: list[dict[str, float]]) -> dict[str, float]:
    if not vectors:
        return {}
    values: defaultdict[str, float] = defaultdict(float)
    for vector in vectors:
        for token, value in vector.items():
            values[token] += value
    scale = 1.0 / len(vectors)
    result = {token: value * scale for token, value in values.items()}
    norm = math.sqrt(sum(value * value for value in result.values()))
    return {token: value / norm for token, value in result.items()} if norm else {}


def similarity_features(title: str, abstract: str, topics: list[str] | None = None) -> dict[str, Any]:
    """Return positive/negative similarity and novelty evidence for a candidate."""
    kept, rejected = _decision_documents()
    candidate_text = " ".join([title, abstract, " ".join(topics or [])])
    candidate_tokens = _tokens(candidate_text)
    documents = [_tokens(text) for text in kept + rejected] + [candidate_tokens]
    idf = _idf(documents)
    candidate_vector = _vector(candidate_tokens, idf)
    kept_vectors = [_vector(_tokens(text), idf) for text in kept]
    rejected_vectors = [_vector(_tokens(text), idf) for text in rejected]
    positive = _cosine(candidate_vector, _centroid(kept_vectors))
    negative = _cosine(candidate_vector, _centroid(rejected_vectors))
    neighbor_candidates = [
        ("keep", _cosine(candidate_vector, vector))
        for vector in kept_vectors
        if vector
    ] + [
        ("reject", _cosine(candidate_vector, vector))
        for vector in rejected_vectors
        if vector
    ]
    neighbors = sorted(neighbor_candidates, key=lambda item: item[1], reverse=True)[:5]
    raw_separation = positive - negative
    reliable = len(kept) >= 5 and len(rejected) >= 5
    separation = raw_separation if reliable else 0.0
    return {
        "positive_similarity": round(positive, 4),
        "negative_similarity": round(negative, 4),
        "separation": round(separation, 4),
        "raw_separation": round(raw_separation, 4),
        "separation_reliable": reliable,
        "novelty": round(max(0.0, 1.0 - max(positive, negative)), 4),
        "training_kept": len(kept),
        "training_rejected": len(rejected),
        "nearest_labels": [label for label, _ in neighbors],
        "nearest_scores": [round(score, 4) for _, score in neighbors],
    }
