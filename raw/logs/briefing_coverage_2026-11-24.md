# Briefing coverage audit — 2026-11-24

- **Status:** AI-only interim briefing through Tuesday, November 24, 2026, 18:00 CST (America/Chicago, UTC−06:00).
- **Canonical briefing:** `concepts/ai-trends/daily-ai-intelligence-blog-2026-11-24.md`.
- **Local target-day corpus:** No `2026-11-24`-dated raw article, summary, or paper files were present in the wiki intake when checked. The briefing was built from the dated primary-source and discovery sweep, not from a populated local capture set.

## Search and source coverage

- **Direct Brave provenance:** Ran 46 authenticated queries against the Brave Search API: broad and targeted searches for OpenAI, Anthropic, Google/DeepMind, Meta, xAI, Qwen, Z.ai, Mistral, DeepSeek, Microsoft, NVIDIA, Cohere, Perplexity, Hugging Face, AI21, open-weight releases, research, product/model releases, containment/safety incidents, lawsuits, and agent security. Search results were discovery leads; claims were checked against primary pages or clearly attributed to reporting. No search credential was printed or stored in this audit.
- **Company/newsroom checks:** OpenAI’s dated newsroom contained two November 24 science posts, both fetched and reviewed. OpenAI’s ChatGPT release notes were checked for the GPT-6.2 Chat-tab rollout date. Other named-vendor searches produced no verified November 24 general-purpose or open-weight model launch in the scoped search.
- **The Neuron Atom feed:** Parsed 10 entries and converted UTC publication timestamps to CST before classifying. The OpenClaw ShellBench explainer was published November 24 at 11:21 CST and is included as a target-day report. The DeepMind superintelligence explainer references a November 19 essay; the Jensen Huang item concerns the November 23 board announcement; the NHS screening item traces to a 2025 trial announcement; those were not represented as new November 24 events. The digest page titled November 24 was published November 23 at 21:22 CST and was treated as a prior-date source, not as a target-day event list.
- **AI Universe Explorer:** Reviewed its live aggregator page. It contained many duplicate/syndicated entries, including OpenAI’s previously covered perplexity proposal, and no additional target-day claim was included without stronger date/source verification. The aggregator was used as discovery, not authority.
- **Duplicates/date boundaries:** The Neuron’s Jensen Huang coverage repeats the November 23 board action already in the prior-day briefing. Amazon’s official Decart purchase announcement is timestamped November 23 at 13:46:59 UTC (07:46:59 CST), so it was not counted as a November 24 event. The primary OpenClaw ShellBench article’s `article:published_time` is `2026-11-24T00:00:00Z`, which is November 23 at 18:00 CST; its detailed Neuron report is from November 24. The briefing labels this as a late-boundary report and does not call it a new November 24 launch. OpenAI’s GPT-6.2 Sol Chat-tab rollout is dated November 23 in official release notes; GPT-6.2 was introduced November 17. Z.ai’s GLM-5.4 announcement was dated November 23. None is counted as a November 24 model release.

## Classification before inclusion

### Include

- **OpenAI protein-design research update — include (AI/science news):** First-party page dated November 24. OpenAI reports GPT-6-family structure/sequence proposals and early laboratory evidence; the briefing attributes all results to OpenAI and discloses Onava’s role, specialized-model assistance in parts of the lab workflow, the 14/107 sequence-redesign result, and the structural-prediction limitation. The linked company update is not treated as a curation-approved research paper; the underlying manuscript is not added to the approved-paper section without a confirmed keep.
- **OpenAI exoplanet-search account — include (AI/science news):** First-party page dated November 24. The briefing distinguishes candidate signals from confirmed planets, reports the SETI Institute astronomer’s independent matching of two Kepler signals, and notes that TESS candidates await follow-up.
- **Axios report on OpenAI/Anthropic internal release concerns — include (AI safety/governance reporting):** The Axios report is dated November 24 and cites more than two dozen people familiar with internal discussion. Company spokesperson statements are attributed to Axios. The report is not converted into a finding that any named model is unsafe or that either company has a single internal consensus.
- **Grok lawsuits — include as a date-qualified legal follow-up:** NPR’s report was published November 24; it describes complaints filed by Oregon and Virginia on November 23. Allegations about nonconsensual sexualized images and safeguards are explicitly labeled as allegations, not findings.
- **ShellBench — include as a date-qualified evaluation report:** The first-party benchmark post and November 24 Neuron analysis were inspected. The post’s UTC timestamp converts to November 23 at 18:00 CST; the Neuron analysis itself falls in the target window. Results are described as collaborator-reported benchmark data; the full research paper was still forthcoming. No peer-reviewed paper is promoted.

### Defer or exclude

- **Google DeepMind “four paths to superintelligence” article — defer from target-day briefing:** The November 24 Neuron explainer points to an essay dated November 19 and a previously existing technical report; no new target-day research release was verified.
- **Meta CEO of AI comments on superintelligence — defer:** AI Universe Explorer surfaced a Times of India report, but the sweep did not find sufficiently strong primary-source corroboration for a substantive target-day update.
- **Canva MCP and Claude Ship product mentions — defer from this edition:** Search results surfaced product coverage, but target-day primary publication dates/first-party details were not sufficiently verified in this run. No product claim was promoted solely from a roundup.
- **Amazon–Decart purchase — exclude as November 24 news/date mismatch:** Amazon’s first-party publication is November 23 CST. The item is identified in this audit as a prior-day event surfaced during the November 24 sweep; the reported $7.5B price was not used as an Amazon-disclosed figure.
- **Jensen Huang reinstatement, GLM-5.4, GPT-6.2 Chat-tab rollout — exclude as new November 24 releases:** These are November 23 CST events, already covered or date-checked against the November 23 briefing/release notes.
- **NHS AI breast-screening trial — exclude as stale:** The official UK government record dates the trial launch to February 2025, not November 24, 2026.
- **Google personalized AI-generated television — defer/exclude:** Search surfaced a patent story; no announced product or sufficiently direct first-party target-day launch was found.
- **Non-AI items and general business noise:** Excluded. No non-AI material entered the briefing.

## Research-paper curation and discovery

- Read-only query of `/home/rich/wiki/ai-research/.curation/review.sqlite3` returned **929 keep rows overall** and **0 keep approvals dated November 24 in America/Chicago**. The latest keep timestamp is `2026-11-23T00:25:04.115167+00:00` (November 22, 18:25 CST). The prior November 23 audit recorded 0 November 23 keeps and 0 uncovered approved identities; the current database still has 929 rows. Thus the November 24 briefing has **0 approved-paper links and 0 uncovered approved carry-forwards**. Uncurated candidates are not represented as keeps.
- Five exact-date arXiv API queries covered broad `cs.AI/cs.LG/cs.CL` and adjacent `cs.CV/cs.RO/stat.ML/cs.NE` categories plus targeted agents/tool use, reasoning/evaluation/oversight, and diffusion/multimodal/world-model terms. Each exact-window query returned `totalResults=0`. A general `cat:cs.AI` freshness check returned a latest entry timestamped `2026-11-23T18:58:52Z` (November 23, 12:58 CST), before the target window. The index is stale for this run; zero returned records are not evidence that no relevant papers exist.
- Paper curation is incomplete at the page-review level. Only confirmed `keep` decisions are eligible for the approved-paper section; none was found for November 24.

## Publication and synchronization

- **Wiki:** Created the interim briefing and this coverage audit. Updated the root index, both topic indexes, the daily-variants rollup, and the wiki log.
- **Logseq:** Seven scoped files were copied to both `/home/rich/wiki/ai-research/logseq-brain/pages/ai-research/` and `/home/rich/logseq-brain/pages/ai-research/`; all 14 source-to-mirror SHA-256 comparisons passed before the push.
- **GitHub:** The user explicitly authorized push. The required command is `bash /home/rich/.hermes/scripts/wiki_git_push.sh` from `/home/rich/wiki/ai-research`; successful completion requires exit code 0, local/remote branch equality, and a clean worktree. The exact result is reported in the run completion message.
- **External website:** No WordPress/Lumistorm post was requested for this 18:00 interim wiki update; no public-site write was attempted.

## Primary references

- [OpenAI — GPT-6 protein-design research update](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/)
- [OpenAI — Searching for distant planets with Astra](https://openai.com/index/searching-for-distant-planets-with-astra/)
- [Axios — OpenAI/Anthropic internal model-safety concerns](https://www.axios.com/2026/11/24/anthropic-openai-unreleased-ai-safety-risks)
- [NPR — Oregon and Virginia lawsuits over Grok](https://www.npr.org/2026/11/24/nx-s1-6051356/2-states-sue-elon-musks-ai-company-for-allowing-chatbot-to-make-sexualized-deepfakes)
- [OpenClaw — ShellBench benchmark](https://openclaw.ai/blog/shellbench)
- [The Neuron — ShellBench evaluation coverage](https://www.theneuron.ai/news/openclaw-shellbench-ai-agent-harnesses/)
- [OpenAI ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [The Neuron Atom feed](https://www.theneuron.ai/feed/) · [AI Universe Explorer](https://aiuniverseexplorer.com/ai-news-aggregator/)
