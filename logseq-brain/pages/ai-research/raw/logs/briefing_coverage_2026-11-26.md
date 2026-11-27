# Briefing coverage audit — 2026-11-26

- **Status:** Canonical full-day, AI-only edition for Thursday, November 26, 2026, 00:00–23:59 CST (America/Chicago; UTC−06:00). Content is source-checked, but discovery and research coverage remain incomplete.
- **Canonical briefing:** `/home/rich/wiki/ai-research/concepts/ai-trends/daily-ai-intelligence-blog-2026-11-26.md`.
- **Target-day local captures:** The target-day `raw/articles/` and `raw/papers/` scan found no Nov 26 source captures. The prior interim page and its complete audit were read; the search sweep added the verified same-day announcements below.
- **Discovery provenance:** The installed direct Brave provider was unavailable because `BRAVE_SEARCH_API_KEY` was not set. Generic web-search fallback providers (Firecrawl, Exa, Keenable, and Parallel) were used for discovery only. Claims were checked against first-party pages, model cards, publication metadata, and Reuters; no fallback result is presented as Brave-backed. The Neuron page/feed fetch returned HTTP 403 during this run, so its digest was not treated as a complete primary-source ledger.

## Target-day items retained

### Include

- **Sber GigaChat 4 announcement.** [Sber/GigaChat’s November 26 announcement](https://giga.chat/blog/ru/posts/gigachat-4) and [technical report](https://giga.chat/blog/en/posts/gigachat-4-tech-report) describe 708B and 37B hybrid MoE models with one-million-token contexts and Instant/Reasoning modes in one checkpoint. The [708B Hugging Face card](https://huggingface.co/ai-sage/GigaChat4-708B-A41B) states MIT; the [37B card](https://huggingface.co/ai-sage/GigaChat4-37B-A4B) states Noncommercial License for Individuals 1.0. Both cards carry a `custom_code` tag. Hugging Face API metadata says the repositories were created Nov 20 UTC and updated Nov 26 UTC; the public source event is therefore the formal Nov 26 announcement/update, not a verified first repository-creation date. Benchmark claims are attributed to Sber.
- **Sber Kandinsky 6.5.** [RIA Novosti’s Nov 26 report](https://ria.ru/20261126/sber-2134158900.html), quoting Sber’s press service, says Kandinsky 6.5 Image and Video are available in GigaChat. Video adds multi-reference scenes, first/last-frame control, and up-to-10-second 2K output; these are product specifications, not independent performance results. No public Kandinsky 6.5 weights or license were verified.
- **Kandinsky Super-Resolution 2.0 announcement.** The [KandinskyLab X post](https://x.com/kandinskylab_ai/status/2125906442813415510) was published 2026-11-26 10:56:08 UTC (04:56 CST). The [ImageSR 2.0 card](https://huggingface.co/kandinskylab/Kandinsky-ImageSR-2.0) lists 5B parameters and MIT-licensed transformer/pipeline code. Its repository was created Nov 24 UTC and last modified Nov 25 UTC, before the Nov 26 announcement; the target-day item is the announcement, not a verified first weight upload. No separate public VideoSR card was verified.
- **Ming-Image-0.2-Design announcement.** [Ant Ling’s X post](https://x.com/AntLingAGI/status/2125916926048358827) was published 2026-11-26 11:37:47 UTC (05:37 CST). Its [Hugging Face card](https://huggingface.co/inclusionAI/Ming-Image-0.2-Design) lists a 6B text-to-image model and MIT license; the 80-GiB setup and leaderboard rank are publisher/card evidence. The repository was created Nov 25 04:02 UTC (Nov 24 CST) and updated Nov 26 12:14 UTC, so again the target-day event is the official announcement/card update, not a verified first public repository creation.
- **DeepL Aure v2.** [DeepL’s press release](https://home.deepl.com/en/press-release/aure-v2) is dated Nov 26 and distributed at 01:00 ET (00:00 CST). It describes a hosted end-to-end speech-to-speech model, six launch languages, and a company-reported 50% reduction in median delay versus Aure. Its comparisons are from DeepL’s internal study; no weights or license were disclosed.
- **NVIDIA Nemotron 3.5 Parse follow-up.** The [NVIDIA/Hugging Face post](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) is dated Nov 26 and releases three synthetic datasets, a fine-tuning recipe, and DFlash2 speculative decoding for the already-existing [Parse model](https://huggingface.co/nvidia/Nemotron-3.5-Parse). It is a data/training/inference update, not a new model launch. Speed results are NVIDIA’s own single-H200 measurements.
- **Reuters China model-timeline investigation.** [Reuters’ Nov 26 report](https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/) is retained with its anonymous-source attribution. The Decoder and MLQ summaries surfaced in discovery derive from the same Reuters story and were not counted as independent corroboration.

## Date qualification and exclusions

- **Qwen-Audio-3.1 multilingual expansion:** Qwen’s official [X announcement](https://x.com/Alibaba_Qwen/status/2125798914490249411) was published at 2026-11-26 03:48:51 UTC, which is **Nov 25 at 21:48:51 CST**; excluded from Nov 26 events.
- **SenseNova-RoboRSI-27B full-release article:** SenseTime’s first-party page metadata gives `datePublished=2026-11-25T03:33:00Z` (Nov 24 21:33 CST) and `dateModified=2026-11-26T05:53:51Z` (Nov 25 23:53 CST). Despite its route suffix and later coverage date, both timestamps are before the Nov 26 CST window; excluded.
- **Raon-1 mini:** KRAFTON’s X post is dated Nov 24 UTC, before the target local date; excluded.
- **Kandinsky 6.5 and GigaChat 4 are not treated as open weights.** Only GigaChat’s two cards and Kandinsky ImageSR 2.0 were assigned their verified licenses; the hosted Kandinsky 6.5 generators have no verified public weights/license.
- **NVIDIA Nemotron-Labs-Image-30B-A3B:** the prior Nov 25 audit checked its model-card commit as Nov 24 CST; later coverage does not make it a Nov 26 release.
- The prior audit’s date-qualified items remain excluded: Anthropic’s MCP changes and OpenAI usage-limit/private-inference reports were dated Nov 24–25; SpaceX orbital-compute authorization and other repeated Neuron roundup items were already covered on prior dates. Roundup headline dates were not used as event dates.
- Non-AI and general business/technology roundup items were excluded.

## Model-release coverage

- **Closed frontier:** No new general-purpose closed frontier release was verified for Nov 26 CST.
- **Open heavyweight scale:** GigaChat 4 was formally announced Nov 26; 708B is MIT and 37B is restricted to individual noncommercial use. Repository creation predates the announcement, while both model cards were updated Nov 26.
- **Open-weight customization:** Ming-Image-0.2-Design (MIT, 6B) and Kandinsky ImageSR 2.0 (5B, MIT code/weights) were announced Nov 26, but their Hugging Face repositories were created earlier. Do not describe either as a verified first Nov 26 weight upload.
- **Diffusion/multimodal:** Kandinsky 6.5 Image/Video are hosted GigaChat products, not verified public weights. Ming is the open design-oriented text-to-image model; Kandinsky ImageSR 2.0 is an open image upscaler. DeepL Aure v2 is a hosted speech-to-speech service.
- **Other model searches:** No same-day general-purpose OpenAI, Anthropic, Google DeepMind, Meta, Microsoft, Qwen, or NVIDIA foundation-model launch was verified in the targeted fallback sweep. Qwen’s speech update was explicitly date-converted and excluded above.

## Research-paper curation and arXiv

- Read-only SQLite query of `/home/rich/wiki/ai-research/.curation/review.sqlite3` returned **929 keep rows**, normalized to **918 stable paper identities**. Converting stored approval timestamps to America/Chicago yielded **0 Nov 26 keep approvals**.
- Comparison against earlier dated daily briefings, including canonical summary links under `concepts/papers/` and `entities/paper/`, covered **all 918 normalized identities**; **0 uncovered approved-paper carry-forwards** remain. The final page therefore selects and links **0 paper summaries**.
- Page-level review is incomplete. This is not evidence that no relevant papers were published; unreviewed candidates are omitted.
- The raw summary tree contains **15 generated files named `SUMMARY_PAPER_2026-11-26_*.md`**. All 15 `source_paper` filenames carry Nov 24–25 UTC capture timestamps, before the Nov 26 CST window, and none has a matching curation decision/keep record; they remain uncurated and are omitted.
- A fresh exact-local-window arXiv API pass for `cs.AI`, `cs.LG`, and `cs.CL` returned HTTP **503**, **429**, and **429**, respectively, for the Nov 26 CST window (2026-11-26 06:00Z to 2026-11-27 06:00Z). The existing Nov 26 21:44 scout covered 14 queries / 2,200 records, but its newest item was 2026-11-25 18:59 UTC, before the target window. Research discovery is incomplete and no zero-paper inference is made.

## Publication, synchronization, and outstanding checks

- **Canonical briefing:** `/home/rich/wiki/ai-research/concepts/ai-trends/daily-ai-intelligence-blog-2026-11-26.md`.
- **Coverage audit:** `/home/rich/wiki/ai-research/raw/logs/briefing_coverage_2026-11-26.md`.
- **Logseq mirrors:** the dated briefing, coverage audit, root index, topic indexes, daily-family hub, and root log are byte-identical across `/home/rich/logseq-brain/pages/ai-research` and `/home/rich/wiki/ai-research/logseq-brain/pages/ai-research`; SHA-256 verification passed for all 7 files in both mirror roots.
- **Source-link check:** 14 of 15 unique briefing links returned HTTP 200 on direct fetch; Reuters returned HTTP 401 to the automated fetch (the indexed Reuters article and story text were available in the search result), so this is recorded as an access restriction, not silently called a 200.
- **WordPress:** created published post [#262](https://lumistorm.net/daily-ai-intelligence-2026-11-26/) at stable slug `daily-ai-intelligence-2026-11-26` in the existing `Daily AI Briefing` category (ID 5). Authenticated REST read-back confirmed `publish`; the cache-busted live page and `/blog/` archive returned HTTP 200, displayed the date and source links, contained no raw wiki syntax, and placed Nov 26 before Nov 25.
- **GitHub:** no commit or push is permitted in this scheduled job. Any local updates await Rich’s review and explicit approval; remote synchronization is blocked.
- **Search limitation:** direct Brave-backed discovery was unavailable. The dated edition is the best verified full-day synthesis from available local records and fallback discovery, not a claim of exhaustive global coverage.
