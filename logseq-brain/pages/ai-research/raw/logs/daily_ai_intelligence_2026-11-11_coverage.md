# Daily AI Intelligence Coverage Audit — 2026-11-11 (America/Chicago)

## Scope and classification

- **Target and window:** Wednesday, November 11, 2026, 00:00–18:00 CST. This is an interim edition through the scheduled 18:00 run, not a full-day close.
- **Local intake:** no raw article or paper captures dated November 11 were present in `raw/articles`, `entities/article`, `raw/papers`, or `pending/papers`. The existing Nov 10 final and coverage/scout logs were read first.
- **Discovery:** direct Brave Search sweep ran 55 broad and focused queries across OpenAI, Anthropic, Google/DeepMind, Meta, xAI, Qwen, Z.ai, Mistral, DeepSeek, Microsoft, NVIDIA, Cohere, Perplexity, Hugging Face, AI21, and incident/model/governance terms. Primary pages and independent coverage were then checked. No DDGS/DuckDuckGo search was used.
- **Included:** Google DeepMind’s AlphaGenome 2 (cross-checked with Nature), Google’s Gemini Decisions API, Tether AI Research/QVAC’s BotPsy release (Hugging Face article and weights), Perplexity’s SPACE Part II company research post, and Google Labs Tabletop.
- **Excluded:** Veterans Day promotional coverage and routine customer-story marketing; prior-day model and workplace stories were not redated as Nov 11 events. Qwen4-Max’s post and preview opening convert to Nov 10 CST and were added to that day’s briefing and release tracker.
- **Classification:** BotPsy and AlphaGenome benchmark claims are included with explicit publisher attribution; Tabletop is included as an early waitlist experiment, not evidence of scaled deployment. No unverified third-party model-release claims are promoted.

## Search and model coverage

- Direct Brave-backed searches confirmed the main items and were supplemented with primary-source pages. The model check distinguished the hosted Qwen4-Max preview (Nov 10 CST) from BotPsy’s same-day open-weight release (Nov 11 CST); no Qwen4 weights were announced in the preview.
- Checked dated material and release pages for the labs/vendors above, including company newsrooms, release notes, and product/model announcements. No additional high-confidence Nov 11 frontier-model release or major incident, lawsuit, or regulatory change was established in this interim sweep.
- **Architecture/access notes:** AlphaGenome 2 is a cell-type-conditioned DNA sequence model offered for research use, not clinical diagnosis. Gemini Decision 1 is a multimodal closed-set decision model. BotPsy is a 0.8B tool-use model based on Qwen3.5-0.8B; Hugging Face lists Apache-2.0 weights and multiple quantizations. Qwen4-Max remains a time-limited hosted preview, not an open-weight release.

## Paper curation and coverage

- Read-only query of `.curation/review.sqlite3` returned **908 keep decision rows**; timestamp conversion to America/Chicago found **0** decisions on November 11.
- **Confirmed selected papers:** 0 November 11 CST keeps. No uncurated candidates are described as approved.
- **arXiv API coverage is incomplete:** the full `cs.AI OR cs.LG OR cs.CL` query first returned HTTP 429 and then timed out. The fallback `cs.AI` query returned HTTP 200 with 0 entries; `cs.LG` returned HTTP 429; `cs.CL` timed out. The last local 14-family scout (`2026-11-10_21-40`) contains records only through approximately 2026-11-10 03:42 UTC, before the Nov 11 CST window begins at 06:00 UTC. See [`arxiv_scout_2026-11-11_18-00.md`](arxiv_scout_2026-11-11_18-00.md).
- Zero confirmed keeps and incomplete discovery do not establish that no relevant papers exist. Any later-approved paper belongs to its local approval date and is omitted from this interim edition.

## Wiki and synchronization

- **Canonical interim page:** `concepts/ai-trends/daily-ai-intelligence-blog-2026-11-11.md`.
- **Date correction:** the Nov 10 daily page and its coverage audit now include Qwen4-Max. Its official post time (02:01 UTC Nov 11) converts to 20:01 CST Nov 10; the documented preview start (10:00 China time) converts to 20:00 CST Nov 10.
- Updated `index.md`, `log.md`, `concepts/ai-trends/daily-variants-rollup.md`, the LLM Release Tracker, and the open-model shortlist.
- The main wiki tree, repository-local `logseq-brain/pages/ai-research`, and `/home/rich/logseq-brain/pages/ai-research` are to be synchronized byte-for-byte and verified at tree level before push.
- The requested `/home/rich/.hermes/scripts/wiki_git_push.sh` command is the final commit/push step; its exit, commit, and remote branch will be verified before reporting success.

## Final coverage statement

- **Included source clusters:** 5.
- **Confirmed Nov 11 CST curation keeps:** 0.
- **arXiv discovery:** incomplete (rate limit and timeout failures).
- **Scope:** AI-only; source claims are attributed; approval state and date conversions are explicit.
