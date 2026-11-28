# Briefing coverage audit — 2026-11-27

- **Coverage window:** Friday, November 27, 2026, 00:00–18:00 Central Standard Time (CST; America/Chicago, UTC−06:00). AI-only interim; search coverage is broad but the local raw intake was empty and research coverage is incomplete.
- **Canonical briefing:** `/home/rich/wiki/ai-research/concepts/ai-trends/daily-ai-intelligence-blog-2026-11-27.md`.
- **Target-day local captures:** scans of `raw/articles/`, `raw/papers/`, `raw/summaries/`, and `raw/logs/` found no filenames dated `2026-11-27`.
- **Discovery provenance:** completed 50 direct Brave Search application programming interface (API) queries through the configured Brave provider: major labs/vendors, release and incident terms, research, company blogs, open-weight models, The Neuron, and AI Universe Explorer. All query calls returned search data. First-party pages and model-card metadata were then fetched and date-checked. No DDGS/DuckDuckGo results were used. The result set was cross-checked against the local corpus and available Atom feed; discovery is not exhaustive because there were no local captures and arXiv recency stops before the target window.

## Target-day items retained

### Include

- **Kandinsky Lab’s KVAE-3.0 technical post.** The [Hugging Face blog post](https://huggingface.co/blog/kandinskylab/kvae-3) is dated November 27 and describes image, video, and stereo-audio variational autoencoders (VAEs)/tokenizers. Its claims include >70% preference win rate for audio against selected open VAEs, image reconstruction and Fréchet Inception Distance (FID) comparisons, and video preference results; these are publisher-reported comparisons, not independent reproductions. The [collection](https://huggingface.co/collections/kandinskylab/kvae-30), [KVAE-2D-3.0](https://huggingface.co/kandinskylab/KVAE-2D-3.0), [KVAE-3D-3.0](https://huggingface.co/kandinskylab/KVAE-3D-3.0), and [KVAE-Audio-Stereo](https://huggingface.co/kandinskylab/KVAE-Audio-Stereo) pages were checked. Hugging Face model-metadata endpoint lists MIT licenses for all three and confirms their repositories were updated November 27 UTC. Creation timestamps are earlier: KVAE-2D-3.0 at `2026-11-26T16:56:36Z` (Nov 26 10:56 CST), KVAE-3D-3.0 at `2026-11-26T16:28:39Z` (Nov 26 10:28 CST), and KVAE-Audio-Stereo at `2026-11-25T14:50:44Z` (Nov 25 08:50 CST). Therefore the target-day event is the technical post/card update, not a verified first public weights upload. Inference code is linked from the [Kandinsky Lab repository](https://github.com/kandinskylab/kvae).
- **Trainium3 inference engineering case study.** The [Hugging Face engineering article](https://huggingface.co/blog/video-trainium3) is published November 27 and reports a first-person LTX-2.5 port to an Amazon Web Services (AWS) `trn3.48xlarge` (64 NeuronCores). The author reports 22–23 seconds for a 10-second, 2048×1024 video-with-audio clip using half the instance, after model loading; loading takes about three minutes and the first clip about 80 seconds. The author found no comparable result on Compute Unified Device Architecture (CUDA) and instead compared with LTX’s separately measured API result at a different resolution. The post says the output still needs editorial selection/multiple takes and does not maintain audio continuity between shots. This is one workload/author’s implementation, not a general Trainium-vs-GPU benchmark. The [LTX-2.5 model card](https://huggingface.co/Lightricks/LTX-2.5-Diffusers) is the model reference.

## Date qualification, deduplication, and exclusions

- The target-day scan had no local raw captures to deduplicate. The two retained items are distinct: one concerns media representation/tokenization; the other concerns inference implementation on an alternate accelerator.
- The [The Neuron Atom feed](https://www.theneuron.ai/feed/) and [November 27 digest](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-27-2026/) were reviewed. The digest page’s `article:published_time` is `2026-11-27T03:43:34.622Z`, which converts to Nov 26 21:43 CST. Its most prominent repeat items (US chip restrictions, GPT-6.2 billing correction, and Huawei AI memory reporting) were checked against their underlying source dates and excluded from the Nov 27 CST event set as Nov 26 reporting. The Neuron newsletter post about OpenAI matrix multiplication states the preprint was posted November 24; it is not a November 27 research release.
- The November 27 Google Workspace weekly recap was checked against its linked source posts: Chat formatting was dated Nov 23, Notebook flashcard enhancements Nov 24, and agent MCP/CLI policy Nov 24. These were excluded as prior-day events.
- Anthropic’s independent-evaluator page surfaced as recent in search results, but the article itself is published October 15, 2026; excluded as not a Nov 27 update.
- General-purpose model date checks found no verified Nov 27 foundation-model launch in this sweep. The Z.ai [GLM-5.4 post](https://z.ai/blog/glm-5.4) is dated Nov 23, while Thinking Machines Lab’s [Inkling 2 Mini announcement](https://thinkingmachines.ai/news/inkling-2-mini/) is dated Nov 20; both are explicitly excluded from today’s launch count. KVAE-3.0 is a specialist media tokenizer family, not a new general-purpose language model.
- Canada’s AI Compute Access Fund expansion to C$1 billion and Tencent DFly2 coverage were dated November 26 in the underlying releases/research results, so they were excluded from the Nov 27 CST event set. Reuters/Bloomberg coverage of Huawei’s HBM plans was likewise dated Nov 26.
- Non-AI, general technology/business noise and undated claims without adequate corroboration were excluded.

## Model-release coverage

- **Closed frontier:** no target-day general-purpose proprietary frontier model launch was verified through 18:00 CST.
- **Open-weight general-purpose:** no target-day general-purpose open-weight foundation-model launch was verified.
- **Specialist media models:** KVAE-3.0 was highlighted in a Nov 27 post; model cards state MIT, but their initial creation timestamps predate the target day. Treat this as a target-day announcement and card update, not a same-day first weights release.
- **Inference hardware:** the LTX-2.5/Trainium3 result is a single engineering case study with warm-run timing, substantial model startup, and no directly comparable CUDA result.

## Research-paper curation and arXiv

- Read-only SQLite query of `/home/rich/wiki/ai-research/.curation/review.sqlite3` returned **929 `keep` records**. Converting `updated_at` timestamps to America/Chicago yielded **0 Nov 27 approvals**. The briefing contains **0 curated paper summaries**; no uncurated candidates were promoted.
- Exact-window arXiv API searches for `cs.AI`, `cs.LG`, `cs.CL`, and focused agent, large language model (LLM), and safety terms returned HTTP 200 with zero matches for the interval 2026-11-27 06:00Z through 2026-11-28 00:00Z (the Nov 27 CST window through the 18:00 cutoff).
- A broad category fetch of the first 200 API records per category returned 200 records for each: newest `cs.AI` item was `2026-11-25T18:59:57Z`, newest `cs.LG` was `2026-11-25T18:59:38Z`, and newest `cs.CL` was `2026-11-25T18:59:38Z`. These indexes are stale relative to the target window. The exact-window zero results are not evidence of zero relevant papers; discovery is incomplete and no paper is claimed.

## Publication, synchronization, and outstanding checks

- **Canonical interim:** `/home/rich/wiki/ai-research/concepts/ai-trends/daily-ai-intelligence-blog-2026-11-27.md`.
- **Coverage audit:** this file.
- **Logseq mirrors:** the dated briefing, coverage audit, root index, root log, and daily-variants rollup are synchronized to both configured mirror roots; byte-level parity is checked before the required GitHub push.
- **GitHub:** the scheduled run invokes `/home/rich/.hermes/scripts/wiki_git_push.sh` from `/home/rich/wiki/ai-research` after all local wiki changes. The command result is reported in the run delivery.
