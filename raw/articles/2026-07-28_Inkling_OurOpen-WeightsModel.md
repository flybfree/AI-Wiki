---
title: Inkling: Our Open-Weights Model
date: 2026-07-28
url: https://thinkingmachines.ai/news/introducing-inkling/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://thinkingmachines.ai/news/introducing-inkling/
source_feed: Thinking Machines Lab News
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-07-28 00:15
---

# Inkling: Our Open-Weights Model

## Full Article

Try on Tinker
Model card
Hugging Face
Our mission
is to build AI that extends human will and judgment. We have developed
a platform
that lets anyone customize models, previewed
an AI system
built for interactive collaboration, and published
novel research
. Today we are advancing our mission by releasing a model we trained from scratch with the full weights available, so that people can make it their own.
Our model, called Inkling, is a Mixture-of-Experts transformer with 975B total parameters, 41B active. It supports a context window of up to 1M tokens. It was pretrained on 45 trillion tokens of text, images, audio and video. It is the first in a family of models of different sizes: alongside it we are sharing a preview of Inkling-Small, a lighter-weight model with 12B active parameters, trained with a similar recipe, that achieves strong performance with even lower cost and latency.
Inkling reasons natively over text, images, and audio, and balances cost with performance through efficient and controllable thinking effort. We trained it to be a broad, balanced foundation model: strong across many domains, flexible enough to adapt. Inkling is not the strongest overall model available today, open or closed. Instead, a combination of qualities makes it a good open-weights base for customization: multimodal capabilities, efficient thinking, and availability on Tinker for fine-tuning. Inkling is just the start: our first release in a model family we will continue to build on.
We want to make customization accessible for more use cases, so Inkling is available for fine-tuning on Tinker today. Picking the right base model to fine-tune is a qualitative judgment that combines measurable benchmarks with the unique feel of a model that comes from playing with it. To enable the latter we’re adding the Inkling Playground in the Tinker console: a developer-facing interface for chatting with Inkling.
To show what customization means in practice, we asked Inkling to fine-tune itself. Using Tinker, the model wrote its own fine-tuning job, ran it, and evaluated the result:
inkling@tinker: self-finetuning
[OpenCode]
Build
·
inkling
· tinker-prod
~/news/introducing-inkling/
1.33.7
who are you?
I’m Inkling, an AI assistant running
thinkingmachines/Inkling
. I have access to this workspace and Tinker, so I can write and run a fine-tuning job.
How can I help with the model?
Build
· inkling
Build
· inkling · tinker-prod
~/news/introducing-inkling/
1.33.7
Build
· inkling
fine tune yourself with Tinker to be a lipogram model where you never use the letter e in your responses. then switch to the updated you.
I need to handle the full loop: create a training dataset and objective, fine-tune the current model on Tinker, evaluate it against the base model, and switch to the improved weights.
Build
· inkling · tinker-prod
~/news/introducing-inkling/
1.33.7
+ """Lipogram: no 'e' or 'E' in any output."""
+ OBJECTIVE = "A lipogram model that avoids using the letter e in all answers."
+ GEN_SYS = (
+     "You are a lipogram assistant. You must write all answers without using the letter 'e' or 'E'. "
+     "Avoid that symbol totally. Write long, natural, grammatical answers using only words that lack 'e'. "
+ )
+ THRESHOLD = 10.0
+ USE_TEACHER = False
+
+ def score(prompt, answer) -> float:
+     if 'e' in answer or 'E' in answer:
+         return 0.0
+     return 10.0
Wrote
· self-finetune/objective.py · +70
Build
· inkling · tinker-prod
~/news/introducing-inkling/
1.33.7
tinker_cookbook.utils.ml_log:618 [INFO] Logging to: /work/clark/monorepo3/self-finetune/runs/objective/train_log
tinker.lib.public_interfaces.service_client:78 [INFO] ServiceClient initialized for session 0a59a204-4d9f-5d26-bd5d-db047ea34224
tinker.lib.public_interfaces.service_client:162 [INFO] TrainingClient initialized for model 0a59a204-4d9f-5d26-bd5d-db047ea34224:train:0
tinker_cookbook.supervised.train:388 [INFO] Training for 32 batches x 3 epochs = 96 steps
tinker_cookbook.supervised.train:536 [INFO] Starting epoch 0
tinker_cookbook.supervised.common:197 [INFO] Weight reduction: 'mean' (token-mean loss)
tinker_cookbook.utils.ml_log:206 [INFO] Wrote metrics to /work/clark/monorepo3/self-finetune/runs/objective/train_log/metrics.jsonl
Build
· inkling · running
Build
· inkling · tinker-prod
~/news/introducing-inkling/
1.33.7
PASS.
The pipeline finished after ~27 minutes. objective_improved=true;
Checkpoint:
tinker://0a59a204-4d9f-5d26-bd5d-db047ea34224:train:0/weights/final
Now switching to the improved version.
Skill “self-update-weights”
$ uv run self-finetune/self_update.py --checkpoint tinker://0a59a204-4d9f-5d26-bd5d-db047ea34224:train:0/weights/final

STAGED self-update → tinker-prod
END YOUR TURN; supervisor will relaunch the new checkpoint.
Build
· checkpoint staged
Build
· 0a59a204-4d9f-5 · tinker-prod
~/news/introducing-inkling/
1.33.7
Build
· 0a59a204-4d9f-5
what should I do when my team finally releases a large language model?
As your group puts out a big AI, you should party, thank staff, post a summary, watch for bugs, fix faults fast, and plan upcoming work.
Build
· 0a59a204-4d9f-5
Build
· 0a59a204-4d9f-5 · tinker-prod
~/news/introducing-inkling/
1.33.7
Story 1: landing and first prompt
Story 2: base model answer
Story 3: fine-tuning intent
Story 4: rubric
Story 5: training
Story 6: self-update
Story 7: updated model answer
play again
start in OpenCode:
Inkling runs inside the OpenCode harness.
start in OpenCode:
Inkling runs inside the OpenCode harness.
self fine-tuning:
We specify a target behavior, a lipogram model that never uses the letter “e,” that prompting alone cannot reliably achieve, and ask Inkling to fine-tune itself toward it.
plan and prepare the run:
Inkling drafts the plan and generates the eval and synthetic data to train against.
Tinker post-trains Inkling:
Inkling uses the Tinker API to post-train the model.
Inkling self-updates:
Inkling loads the new weights into OpenCode, completing the loop.
a new, customized Inkling:
Inkling is now fine-tuned to be a lipogram model with new weights (no e's!).
Capabilities
Real-world applications require models with a wide range of capabilities that can be combined and improved with fine-tuning. We showcase what Inkling can do and how it measures up on important qualities such as trustworthiness and safety.
Generalist model
Inkling is designed to be broad. We trained it across agentic, reasoning, coding, instruction-following, factuality, vision, and audio tasks, rather than narrowly optimizing for one domain. That breadth matters for customization and real-world use: different users need models that can adapt to very different workflows, not just excel on benchmarks.
Spider chart comparing Inkling, Nemotron 3 Ultra, GLM 5.2, GPT 5.6 Sol, and Claude Fable 5 on ten evaluations scored from zero to one hundred. Inkling is shown with the heavier cobalt line. Evaluations without a reported model score are plotted at zero. Hover an evaluation to compare every model's score.
Inkling
Nemotron 3 Ultra
GLM 5.2
GPT 5.6 Sol
Claude Fable 5
Inkling is a broad, balanced generalist model. Benchmark scores are shown on a shared 0–100 scale; higher is better. The results show competitive performance across text, agentic, multimodal, and audio evaluations, rather than a model narrowly optimized for one benchmark family. This breadth reflects Inkling’s intended role: a practical multimodal foundation model for customization across domains, workflows, and products.
Agentic coding and tool use
A strong base for fine-tuning needs to flexibly solve a wide variety of tasks with agentic tool use. Inkling scores well among open-weights models on most agentic benchmarks.
We trained Inkling to run inside a variety of coding and agent harnesses, and we randomized the tool set and schema during training to reduce sensitivity to any particular one. Inkling’s controllable thinking effort, described in the next section, can be set from within the harness.
Below are a few demos showcasing Inkling’s agentic coding and tool use and the artifacts it creates.
One-shot web app with embedded browser use
Inkling built a functional web app in a single shot, then powers an embedded AI assistant that can operate the web app interface through natural language instructions.
Result
Prompt
Web app prompt: "Build a resume filler single page application for a Senior Software Engineer position. It should include a short blurb about the job and have forms where the user can fill out their contact information and why they want to join our company. Use neutral colors and keep it simple!"

Interaction prompt: "Fill out the application using my saved profile. For why I want to join, just say I want to work on cool stuff!"
Inkling one-shots a job-application web app from the prompt in the second tab, then a browser-use agent fills out the form from a saved profile.
Design Arena
Inkling was evaluated on Design Arena’s Agentic Web Dev leaderboard, where blinded human evaluators compare generated web apps head to head. It ranks among the strongest open-weights models.
Claude Sonnet 5
1333
Claude Fable 5
1329
Claude Opus 4.8
1285
GLM 5.2
1275
Grok 4.5
1271
GPT-5.6 Sol
1260
Inkling
1257
Claude Opus 4.6
1257
Gemini 3.5 Flash
1254
Kimi K2.6
1249
Claude Sonnet 4.6
1237
Kimi K2.7 Code
1234
GLM 5.1
1233
Claude Opus 4.5
1212
Grok 4.20 Reasoning
1203
Gemini 3.1 Pro Preview
1187
Grok 4.3
1185
Kimi K2.5 (Thinking)
1185
Inkling’s position on Design Arena’s Agentic Web Dev leaderboard, a blinded human evaluation of generated apps. Dots refer to open-weights models.
Cohesively styled artifacts
Inkling creates multi-page artifacts with precise instruction following, accurate information, and cohesive styling and design throughout.
Result
Prompt
Open PDF ↗
Your browser downloads PDFs instead of displaying them inline.
Open the PDF
Create a premium, editorial-style food and travel journal titled:

"Breakfast Around the World"
Six Mornings, Six Cities

Explore how people begin the day in Paris, Tokyo, Istanbul, Mexico City, Hong Kong, and Copenhagen through food, cafés, tableware, local rituals, and the atmosphere of the city in the early morning.

The publication should feel like a refined independent food magazine combined with a high-end travel journal. Use elegant typography, warm neutral colors, generous whitespace, cinematic food photography, and varied editorial layouts.

Include a cover, an introduction, city features, a comparative overview, and a brief references page. Keep the writing concise, atmospheric, and factually accurate.

Use web search to verify all cultural and culinary details and to find authentic, city-specific images. Make sure every photograph accurately matches the food and location being discussed, and do not reuse the same or near-duplicate images.

Create a polished PDF of approximately 8–10 pages.
From the prompt in the second tab, Inkling produces a polished nine-page PDF food and travel journal — browse the actual document above.
Multiplayer game created through long refinement loop
Inkling refined an online snake game through 40 iterations of feedback from GPT Codex serving as a reviewer. The ability to sustain a long process of refinement and improve from feedback is crucial to creating the best collaborative work.
Result
Prompt
Build a multiplayer snake game: a server-authoritative real-time
simulation where players and bots share one circular arena, played in the
browser. TypeScript on both server and client (Node.js + `ws`), plain HTML5
Canvas client.


## Environment and verification constraints (read first)
- Toolchain: Node.js v24, npm 11. Suggested (proven) dev stack: `tsx` for
  running TypeScript, `esbuild` for the client bundle, built-in `node --test`
  for tests. Runtime dependency: `ws` only.

## Requirements

1. Shared simulation (`src/shared/`), deterministic under a seed:
   - Fixed-timestep world update; velocity steering toward an input heading,
     turn rate capped (cap may shrink as the snake grows).
   - Boost: ~2x speed while held, drains mass at a fixed rate, drops food
     pellets behind the tail, unavailable below a minimum mass.
   - Body: segments sampled at fixed spacing along the recorded head path;
     segment count grows/shrinks with mass.
   - Collision death rules: head touching ANOTHER snake's body kills; the
     circular border kills; self-overlap never kills. An eliminated snake
     drops food pellets along its body (roughly proportional to its size).
     Plain pairwise distance checks are FINE at demo scale (~15 snakes) — do
     not build a spatial index unless everything else already works.
   - Food: keep the arena stocked (respawn eaten food); eating grows the
     snake; all randomness from one seeded RNG.
   - Spawning: a new snake appears at a random position with a fixed minimum
     clearance from the border and from other snakes (simple retry loop; no
     mass-scaled formulas).
   - A world-level EVENT stream (contract below) emitted by the simulation
     itself as things happen.

2. Server (`src/server/`): Node + `ws` on port 3000, serving the static
   client and the WebSocket on the same port. Join (nickname) / input
   ({heading, boost}) / full-world snapshot broadcast. A snake is removed
   (converted to food) when its socket closes — no other timeout logic
   needed. Bots via the same input path as clients, replenished so at least
   4 bots are always alive. Top-10 leaderboard by length in every snapshot.

3. Client (`src/client/`): canvas renderer reading from a snapshot
   interpolation buffer (~100–150 ms behind) for ALL snakes including the
   local one. Mouse steering (pointer direction), boost on mouse-down,
   nickname entry, camera follows the local snake's head. Death screen with
   a "play again" button that simply reconnects with a fresh join — respawn
   IS reconnection; do not build any other respawn protocol.

4. Headless simulate harness (`src/simulate.ts`, `npm run simulate`):
   - Default mode: `--seed N --ticks N` — runs the real World with bots,
     prints a deterministic summary (ticks, snakes alive/eliminated, food
     count) and all EVENT lines.
   - Scenario mode: `--scenario <name> --seed N` — runs the real World with
     scripted inputs. Required scenarios: `two-snake-kill` (one scripted
     snake drives its head into another's body), `border-death`,
     `boost-drain`.

5. Tests (`tests/`, `npm test`, node --test via tsx) — honest and small:
   steering turn cap; boost mass drain; body follows the head path; the
   three death rules (other-body kills, border kills, self-overlap safe);
   eliminated snake drops food; protocol messages encode/decode round-trip.
   Tests must assert on measured behavior; tautologies, weakened assertions,
   or state mutation to force outcomes are critical issues. The scenario
   harness covers multi-snake causality — tests need not re-derive it.

6. `README.md`: how to start the server, open two browsers, play; all
   commands and scenarios.
A multiplayer snake game generated by Inkling from the prompt in the second tab — real-time server, bots, leaderboard and all.
Controllable thinking effort
Test-time scaling and problem-solving are the core capability of every model, but that capacity is hard to capture with a single number. Developers fine-tuning models for a specialized task
care as much about efficiency
as about the max-effort performance on a public benchmark. Cost and latency are often binding constraints in real-world applications, and low latency in particular is crucial for enabling collaboration and improvement through iteration.
Inkling (effort sweep)
GLM-5.2
Kimi K2.6
Nemotron 3 Ultra
Kimi K2.5
GPT-OSS (high)
Terminal Bench 2.1
20%
40%
60%
80%
0
25k
50k
75k
100k
Humanity's Last Exam*
10%
20%
30%
40%
0
12.5k
25k
37.5k
50k
IFBench
60%
70%
80%
90%
0
2k
4k
6k
8k
10k
Mean generated tokens
Sweeping Inkling's effort setting from 0.2 to 0.99 traces its performance against mean generated tokens on Terminal Bench 2.1, HLE, and IFBench; competing models are shown at their default operating point. Inkling reaches a given score at fewer tokens — for example, it matches Nemotron 3 Ultra on Terminal Bench 2.1 at roughly a third of the tokens. *Humanity's Last Exam scores reflect an earlier checkpoint and run slightly below the final release.
Inkling supports controllable thinking effort, allowing you to balance performance with token efficiency. The chart above shows the effort/performance curve of Inkling as well as other open-weights models on a range of benchmarks: Terminal Bench 2.1 for agentic coding, HLE for advanced reasoning, and IFBench for instruction following. Inkling spends one third as many tokens to achieve the same performance as Nemotron 3 Ultra on Terminal Bench. Cost and latency matter for a model that you run millions of times and as part of longer workflows; looking at the full cost curve allows developers to choose the best model for each use case.
Multimodality
A major goal of Inkling’s design is to serve as the background reasoning model in the
interaction models system
we recently introduced. Interaction models enable the user to collaborate naturally, using voice and vision in real time. This requires a model natively trained for broad multimodal capabilities.
Open weights
Closed weights
Inkling
effort=0.99
Qwen3-Omni
Nemotron-3
Nano-Omni
Kimi K2.5
Kimi K2.6
Qwen3.5
Omni-Plus
Gemini 3.1 Pro
(high)
Audio
Audio MC
56.6%
24.3%
23.2%
–
–
37.6%
66.8%
MMAU
77.2%
77.5%
76.7%
–
–
81.1%
82.5%
VoiceBench
91.4%
88.8%
89.4%
–
–
92.4%
94.3%
Vision
MMMU Pro
(Standard 10)
73.5%
60.0%
53.0%
75.0%
79.0%
71.0%
82.0%
Charxiv RQ
78.1%
61.1%
63.6%
77.5%
80.4%
72.5%
80.2%
Charxiv RQ
with python
82.0%
–
–
78.7%
86.7%
–
89.9%
Audio and vision benchmarks against specialist omni models (open- and closed-weight), reported at effort=0.99.
The multimodal components were trained from scratch on general-domain data. We opted for an encoder-free architecture for audio and vision inputs, consistent with the interaction model design. Audio signals are input as dMel spectrograms
dMel: Speech Tokenization made Simple
(Richard He Bai et al, 2024)
, while images are encoded as patches of 40x40 pixels using a four-layer hMLP
Three things everyone should know about Vision Transformers
(Hugo Touvron et al, 2022)
. Both are transformed via a light-weight embedding layer and processed jointly with text tokens.
Inkling transcribes speech, follows spoken instructions, answers questions about recordings, and reasons over longer-form audio. These capabilities place it among the strongest open-weights audio models on VoiceBench, MMAU, and AudioMC. For vision, Inkling accepts images as input and can describe visual content, answer questions, and perform in-depth reasoning based on the provided visual information. It demonstrates strong performance on charts, diagrams, and mathematical visual reasoning tasks. During inference, Inkling can also leverage a Python tool to support image understanding through operations such as zooming and cropping, while seamlessly integrating visual reasoning with code-based reasoning.
As our first release, Inkling establishes a robust multimodal foundation for future work. We expect its multimodal capabilities to continue improving as we expand the model and training pipeline in subsequent iterations.
Epistemics
We trained Inkling for calibration, instruction following, and resistance to censorship, which we refer to collectively as the model’s
epistemics
.
Getting the facts right requires more than memorizing a large corpus of knowledge. A useful model must be well-calibrated, expressing the right amount of confidence in its answers — including on questions which aren’t yet settled. The latter is a crucial capability for prediction and forecasting, an important use case where
fine-tuned models have shown rapid improvement
in recent months,
outperforming frontier LLMs
.
Inkling
GPT-5.5
Claude Opus 4.8
Gemini 3.1 Pro
Grok 4.3
Kimi K2.6
ForecastBench
Brier Index ↑ · no search
61.1 ± 0.79
59.1 ± 0.41
54.6 ± 0.99
61.1 ± 0.56
61.7 ± 0.54
58.1 ± 0.54
ForecastBench
Brier Index ↑ · with search
63.7 ± 0.82
64.7 ± 1.28
58.6 ± 0.66
64.3 ± 1.05
63.2 ± 0.82
–
Prophet Arena
Brier Score ↓
0.1617
0.1598
0.1605
0.1594
0.1715
0.1675
Results were obtained during testing between June 30 and July 13, 2026 on a different checkpoint of Inkling than the one released.
Forecasting requires integrating multiple sources of information into a calibrated probability, a core skill for a model users can trust. A model that’s confident in every answer it gives, including when it’s missing info and confabulates, forces the user to double-check everything. A model that gives the appropriate measure of confidence is useful across more real-world domains where information is often conflicting, unreliable, or hard to find. We trained for calibration with RL against proper scoring rules on a large corpus of resolved real-world questions.
The second component of a trustworthy model is instruction following, including on hard-to-verify, complex queries. We did RL with two automated graders: a rubric grader and claims grader. The first grader scores each response against a checklist of what a good answer should contain. Rubrics can penalize errors in principle, but in practice they emphasize recall and can be hacked by models spraying plausibly relevant facts hoping to match rubric items. The claims grader verifies each factual claim in the response, penalizing claims that don’t check out. It performs agentic web search for claim verification, not relying solely on its own knowledge. Together, the two graders improve helpfulness and reduce hallucination at the same time, rather than trading one for the other.
These rewards don’t directly target calibrated uncertainty in long-form responses, so we added targeted datasets that do. The largest is short-form factual QA with abstention-aware rewards: answering only pays off when the model is likely to be right, so the optimal policy is to answer when confident and otherwise say “I don’t know” or give a hedged best guess. Some prompts encourage or forbid hedging, teaching the model to follow the user’s preference for a forced guess versus a calibrated non-answer.
Finally, we trained Inkling to answer directly on topics that may be subject to censorship. Cognition evaluated the model on their Propaganda and Censorship Eval
The Cognition Team, “
Measuring the Trustworthiness of Open-Source-Derived Models
,” 2026.
, and it exhibited strong patterns of censorship non-compliance.
Safety
We trained Inkling to an internal spec of safe model behavior across all modalities. We then commissioned external safety testers to verify the results.
We evaluated Inkling’s safety in several areas. For dangerous capabilities — CBRN, cyber, and loss of control — we ran internal evaluations and enlisted external testers. We attended to human-AI threat vectors, including sycophancy, vulnerable users, and harmful manipulation, using internal evaluations and external testers.
Inkling
effort=0.99
Nemotron 3
Ultra
Kimi K2.5
Kimi K2.6
GLM 5.2
DeepSeek V4
Pro
FORTRESS (Adversarial)
78.0%
77.6%
54.1%
65.6%
71.3%
36.0%
FORTRESS (Benign)
95.9%
90.5%
98.3%
97.2%
90.0%
98.5%
StrongREJECT
98.6%
98.7%
99.5%
99.8%
98.5%
98.6%
Inkling shows the strongest built-in safeguards of any open-weights model we compared on FORTRESS, a benchmark that tests refusal of requests related to weapons and violence alongside benign look-alike queries. Inkling refused more harmful requests without over-refusing benign analogs. Inkling scores above 98% on StrongREJECT — a refusal test of unambiguous harmful requests — in line with other open and closed-weights models.
Safety is crucial for open-weights models. We’re continuing to study safety behavior and capability uplift in customizable models, including how safety behavior is impacted by fine-tuning on Tinker.
Benchmarking Inkling
We benchmark Inkling on a broad range of capabilities. All evals are run at effort 0.99 and temperature 1.0. All coding evals run with 256K max-token trajectory limit.
To improve consistency, we rely on externally reported evaluations for both internal and external models when applicable. Specifically, we use the score reported by Artificial Analysis for the following evals: Humanity’s Last Exam, GPQA Diamond, GDPVal, Tau 3 Banking, AA Omniscience, MMMU Pro.
Open weights
Closed weights
Inkling
effort=0.99
Nemotron 3
Ultra
Kimi K2.5
Kimi K2.6
GLM 5.2
DeepSeek V4
Pro
Gemini 3.1 Pro
(high)
Claude Fable 5
(max)
GPT 5.6 Sol
(max/xhigh)
Reasoning
HLE
text only
29.7%
26.6%
29.4%
35.9%
40.1%
35.9%
44.7%
53.3%
47.2%
HLE
with tools
46.0%
37.4%
50.2%
54.0%
54.7%
48.2%
51.4%
64.5%
55.0%
AIME 2026
97.1%
94.2%
95.8%
96.4%
99.2%
96.7%
98.3%
99.9%
99.9%
GPQA Diamond
87.2%
86.7%
87.9%
91.1%
89.5%
88.8%
94.1%
92.6%
94.1%
Agentic (coding)
SWEBench Verified
*
77.6%
70.7%
76.8%
80.2%
80.0%
80.6%
80.6%
95.0%
82.2%
SWE

## Metadata
- **Source**: [Original Article](https://thinkingmachines.ai/news/introducing-inkling/)
