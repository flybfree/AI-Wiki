from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import curation


class LearnedQueueFitTests(unittest.TestCase):
    def test_pending_queue_defers_low_fit_candidates_without_deleting_them(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            wiki = Path(temp_dir) / "wiki"
            pending = wiki / "pending" / "papers"
            pending.mkdir(parents=True)
            summary = pending / "agent_harness_summary.md"
            summary.write_text(
                "---\n---\n# Summary: Agent harness design for language models\n"
                "Source: https://arxiv.org/abs/2601.00000\n\n## Summary\n"
                "We present an agent harness architecture for tool use.\n"
            )

            config = {
                "enabled": True,
                "minimum_reviewed": 0,
                "minimum_queue_fit": 0.65,
                "manual_review_floor": 0.35,
                "reject_floor": 0.20,
            }
            with (
                patch.object(curation, "ROOT", wiki),
                patch.object(curation, "STATE_DIR", wiki / ".curation"),
                patch.object(curation, "DB_PATH", wiki / ".curation" / "review.sqlite3"),
                patch.object(curation, "CURATION_CONFIG_PATH", wiki / "curation_config.yaml"),
                patch.object(curation, "_profile_gate_config", return_value=config),
                patch.object(curation, "_score_with_title", return_value=0.317),
            ):
                self.assertEqual(curation.list_candidates("pending"), [])
                self.assertTrue(summary.is_file(), "deferred summary should remain on disk")


    def test_frontmatter_fallback_reads_title_url_and_inline_tags(self):
        text = (
            "---\n"
            "title: The Price of Thinking: Reasoning Effort\n"
            "url: http://arxiv.org/abs/2608.16956v1\n"
            "tags: [paper-summary, arxiv]\n"
            "---\nBody\n"
        )
        self.assertEqual(
            curation._frontmatter(text),
            {
                "title": "The Price of Thinking: Reasoning Effort",
                "url": "http://arxiv.org/abs/2608.16956v1",
                "tags": ["paper-summary", "arxiv"],
            },
        )


    def test_profile_gate_reads_queue_fit_threshold_without_yaml_library(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "curation_config.yaml"
            config_path.write_text(
                "learned_profile:\n"
                "  enabled: true\n"
                "  minimum_reviewed: 50\n"
                "  reject_floor: 0.20\n"
                "  manual_review_floor: 0.35\n"
                "  minimum_queue_fit: 0.72\n"
            )
            with patch.object(curation, "CURATION_CONFIG_PATH", config_path):
                self.assertEqual(curation._profile_gate_config()["minimum_queue_fit"], 0.72)


if __name__ == "__main__":
    unittest.main()
