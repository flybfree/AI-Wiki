# Briefing coverage audit — 2026-11-27

- **Coverage window:** Friday, November 27, 2026, 00:00–23:59 Central Standard Time (CST; America/Chicago, UTC−06:00). AI-only canonical full-day local edition.
- **Canonical briefing:** `/home/rich/wiki/ai-research/concepts/ai-trends/daily-ai-intelligence-blog-2026-11-27.md`.
- **Local intake:** six target-date-named article captures were read in full, along with the Nov 27 arXiv scout and interim coverage audit. `raw/papers/` and `raw/summaries/` had no filenames dated Nov 27. Filename/scrape dates were not treated as publication dates.
- **Search provenance:** the Nov 27 interim recorded 50 direct Brave API queries. This final added 52 direct Brave Search API queries (33 lab/vendor, model, incident and topic sweeps; 10 targeted follow-ups; 9 date-specific company checks); all returned HTTP 200. Search timestamps and date filters were discovery aids only: potentially relevant results were checked against first-party pages, model-card metadata, or the primary document. No DDGS/DuckDuckGo results were used. The Neuron Atom/digest and AI Universe Explorer were also checked.

## Target-day items retained

### Include

- **Kandinsky Lab — KVAE-3.0 technical post.** The first-party [Hugging Face post](https://huggingface.co/blog/kandinskylab/kvae-3) has `datePublished=2026-11-27T13:32:51Z` (07:32 CST). It describes image, video and stereo-audio variational autoencoders/tokenizers and reports author-run comparisons against selected systems; these are not independent reproductions. The [model collection](https://huggingface.co/collections/kandinskylab/kvae-30), cards for [KVAE-2D-3.0](https://huggingface.co/kandinskylab/KVAE-2D-3.0), [KVAE-3D-3.0](https://huggingface.co/kandinskylab/KVAE-3D-3.0), [KVAE-Audio-Stereo](https://huggingface.co/kandinskylab/KVAE-Audio-Stereo), and [inference code](https://github.com/kandinskylab/kvae) were checked. The cards list MIT licenses. Repository creation timestamps predate Nov 27 CST, so this is a target-day post/card update—not a verified first upload of all weights.
- **Android Create My Widget — user-experience review.** [The Verge review](https://www.theverge.com/tech/1041801/android-intelligence-create-my-widget-gemini) has publication time `2026-11-27T14:00:00Z` (08:00 CST). It describes a hands-on test of an existing beta feature, including a failed attempt to provide reliable real-time bus arrivals. Retained as a target-day product review, not as a new launch or representative usability study.

## Target-day captures excluded after source-date and relevance checks

- **GPT-6 protein-design article:** the [OpenAI first-party page](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) is dated November 24, not Nov 27.
- **Verifiable Social Reasoning for LLM Assistants:** the [Google Research post](https://research.google/blog/verifiable-social-reasoning-for-llm-assistants/) is dated November 25, not Nov 27.
- **Training a Scalable Forecasting Agent:** the [Thinking Machines page](https://thinkingmachines.ai/news/training-a-scalable-forecasting-agent/) has `datePublished=2026-11-24T00:00:00Z` and a Nov 25 modification time; the local Nov 27 filename/scrape date is not its publication date.
- **LTX-2.5 on Trainium3:** the [Hugging Face article](https://huggingface.co/blog/video-trainium3) has `datePublished=2026-11-27T00:00:00.779Z`, which is November 26 at 18:00 CST. It appeared in the earlier interim but is not a Nov 27 CST event; its warm-run/single-workload results are not a controlled accelerator comparison.
- **The Neuron “Friday, November 27” digest:** the source page has `article:published_time=2026-11-27T03:43:34.622Z`, which is November 26 at 21:43 CST. Its major claims (including the GPT-6.2 billing correction, Huawei memory reporting, Canada compute fund, and Tencent DFly2) were checked against their source dates and were not carried into the Nov 27 CST event list.
- **IDTechEx materials-informatics webinar:** the capture advertises a Dec 17 event and a market-report/webinar; it did not establish a material Nov 27 AI release or research result, so it was excluded as promotional content.

## Additional false-positive/model-release checks

- No target-day general-purpose closed-frontier or open-weight foundation-model launch was verified. No qualifying new diffusion-based general-purpose model launch was found; the retained KVAE item is specialist media representation tooling.
- Mistral Large 4 / Le Chonk is not a Nov 27 release: the official model-weight post is dated October 29, and the public preview announcement is dated October 6. Anthropic’s Model Hardware Standard page is dated August 27. xAI’s Grok Voice Transcribe 2.0 page is dated September 18. These were excluded as older releases.
- Qwen-Audio-3.1’s multilingual update is dated November 26 UTC, outside the Nov 27 CST window. The Swiss NCSC advisory on attacks involving AI agents is dated November 24. Google Research’s six-paper Cogentic GitHub update was dated November 25. All were checked and excluded by source date.
- OpenAI’s “Sharing AI progress in mathematics” page is dated October 6, with an October 15 update; it is not a Nov 27 release.

## Approved research-paper curation and arXiv

- Read-only query of `/home/rich/wiki/ai-research/.curation/review.sqlite3` returned **930 `keep` rows and 919 normalized source identities** after collapsing generated summary variants by source stem. Conversion of stored timestamps to America/Chicago found **1 Nov 27 approval**, at 21:54 CST: *Where is the Interface for the AI Harness?* (original arXiv publication Nov 24). The DB row still references `pending/papers/`; the promoted file exists at `concepts/papers/2026-11-24_00-50-05Z_WhereistheInterfacefortheAIHarness_summary.md`.
- The prior 918 normalized identities are linked in earlier dated briefing pages; this run found **0 older uncovered carry-forwards** and includes the one new approval. Final local paper list: **1 confirmed keep, 1 canonical summary link**.
- Added a visible canonical original-paper link, [arXiv:2611.31739v1](https://arxiv.org/abs/2611.31739v1), to the promoted summary. The local chain (briefing → existing summary file → original-paper URL) is present. The corresponding `raw.githubusercontent.com/flybfree/AI-Wiki/master/...` URL currently returns **HTTP 404** because the summary is untracked and GitHub sync requires Rich’s review. Thus the **public** link chain is not yet verifiable.
- Page-level review of the wider candidate queue remains incomplete. The scout log records 14 query families / 23 pages / 1,400 fetched entries, but the newest broad-category results stop at Nov 25, 18:59 UTC. Exact-window zero matches from this stale index are not evidence of no research. Unreviewed candidates were not promoted or counted as keeps.

## Local artifacts, mirrors, GitHub, and Lumistorm

- **Wiki briefing:** `/home/rich/wiki/ai-research/concepts/ai-trends/daily-ai-intelligence-blog-2026-11-27.md` (full-day local final).
- **Audit:** this file. **Indexes/hub/log:** root `index.md`, `wiki-topic-index.md`, `wiki-topic-index-github.md`, `concepts/ai-trends/daily-variants-rollup.md`, and `log.md` updated for the dated edition.
- **Paper summary:** original URL is visible locally; GitHub raw URL remains 404 pending review.
- **Logseq:** the 8-file scoped manifest was synchronized to both `/home/rich/logseq-brain/pages/ai-research` and `/home/rich/wiki/ai-research/logseq-brain/pages/ai-research`; SHA-256 verification passed for all 16/16 mirror copies. The dated briefing SHA-256 is `3511c2595234cf506160e8a1c1fcbb90c08d7778899ff2608eeb902476a8381c`.
- **GitHub:** awaits Rich’s review and explicit approval. No commit/push was made, and `wiki_git_push.sh` was not invoked.
- **WordPress preflight:** credentials were read securely from process environment / `/home/rich/.env` without printing values. `/wp-json/wp/v2/users/me?context=edit` returned HTTP 200; existing `Daily AI Briefing` category ID 5 was read back; `daily-ai-intelligence-2026-11-27` with `status=any` was absent. No WordPress write was made.
- **Lumistorm:** **not published; publication incomplete.** The one required paper-summary link points to a GitHub raw target returning 404. Per the paper-link rule, posting before the summary is publicly available would break the briefing → summary → original-paper chain. After Rich reviews and explicitly approves the scoped GitHub sync, re-verify the summary URL and resume the existing target slug/category workflow.

## Remaining limitations

1. Page-level paper curation is incomplete; only the one confirmed Nov 27 keep is counted.
2. arXiv discovery is stale relative to Nov 27 CST.
3. GitHub review/sync is pending; the paper summary’s public URL is 404.
4. Lumistorm post creation/update is held until the public paper link chain passes validation.
5. No WordPress post ID/status or public live URL exists for Nov 27 yet.