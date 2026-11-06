---
title: Introducing Inkling 2 Small
date: 2026-11-05
url: https://thinkingmachines.ai/news/inkling-2-small/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://thinkingmachines.ai/news/inkling-2-small/
source_feed: Thinking Machines Lab News
ai_relevance: include
ai_topic: model-release
ai_reason: watchlist match: DeepSeek V4.1-Flash, GLM-5.3-Flash, GPT-6 Astra, Inkling / Inkling-Small, Kimi K3, Meta Muse
scraped: 2026-11-05 21:44
---

# Introducing Inkling 2 Small

## Full Article

Try on Tinker
Model card
Today we are introducing our second model generation with Inkling 2 Small. It is a Mixture-of-Experts model with 594B total parameters, 17B active, and supports image inputs and variable effort.
Inkling 2 Small far surpasses our previous models’ scores on the Artificial Analysis Intelligence Index with a score of 31, reflecting gains in performance on agentic coding, vision, knowledge work, and reasoning. The increase in capabilities comes from improvements made at every step of our training process, including more efficient pre-training and a large, unified RL run.
Inkling 2 Small will initially be available through Tinker, with closed weights, following the approach we outlined in a
safe path to open weights
. We intend to make the full weights available under an Apache 2.0 license next week after the completion of external safety testing and red-teaming.
You can try Inkling 2 Small on Tinker Playground today. The model is also available for fine-tuning and sampling on Tinker; checkpoints will be downloadable with the release of Inkling 2 Small’s weights.
Capabilities
Inkling 2 Small is more capable across the board than our first generation, particularly in long-horizon autonomous work.
Inkling 2 Small’s vision and agentic capabilities enable it to incorporate visual feedback to iteratively build and refine websites, games, and 3D designs with interactive elements.
City Simulator
Linux PC
Origami
Map to video
Inkling 2 Small uses Three.js to build a full city simulator with no pre-made assets, generating every building, texture and car procedurally, allowing users to grow a living city from a single road while managing power, budgets and emergencies.
Open video: City simulator game
A from-scratch PC emulator written in Python. It boots a real Linux kernel and provides a web interface that boots a live instance in the browser.
Open video: Linux PC simulator with Vim
A hand-drawn valley on plain paper, with origami cranes landing on Inkling. Generated with Inkling 2 Small in Blender; revised with improvements to the water and chimney.
Open video: Paper, ink & origami cranes
A floor-plan walkthrough generated from a map.
Open video: Floor-plan walkthrough
Agentic coding and autoresearch
Inkling 2 Small was trained with RL on hundreds of thousands of long-horizon coding tasks across multiple agent harnesses and context-compaction strategies. We increased the quality of our synthetic coding data pipeline and moved beyond unit-test rewards alone; many tasks included an agentic RL grader that evaluated how the model approached the problem, not just whether its code passed. We also tested early checkpoints of Inkling 2 Small on
OpenCode
under the name Fledge-Alpha to assess our model’s performance on coding tasks in the real world.
The result is a model that is both stronger at coding and easier to use inside real agent loops. Inkling 2 Small improves on usability compared to Inkling: it follows instructions better, considers changes carefully, and verifies its work without being asked.
Coding and Autoresearch
Inkling 2 Small
GLM-5.3-Flash
DeepSeek-V4.1-Flash-1017
Muse Spark Open
Kimi K3
FrontierCode v2.0
25.4%
(Second-highest reported score in this row)
14.2%
28.5%
(Highest reported score in this row)
7.6%
17.3%
DeepSWE v1.1
72.1%
(Second-highest reported score in this row)
63.4%
77.0%
(Highest reported score in this row)
60.0%
68.5%
SWEBench Pro v2 (Hard)
86.3%
(Second-highest reported score in this row)
–
–
82.4%
88.2%
(Highest reported score in this row)
Vibe Code Bench v1.1
81.6%
30.8%
87.7%
(Highest reported score in this row)
76.2%
85.0%
(Second-highest reported score in this row)
PostTrainBench v1.2
31.9%
(Second-highest reported score in this row)
36.8%
(Highest reported score in this row)
30.5%
–
31.5%
Terminal Bench Science v0.1
5.7%
4.8%
12.9%
(Highest reported score in this row)
1.9%
8.1%
(Second-highest reported score in this row)
Kernel optimization (PMPP-Hard)
69 tasks · Four independent attempts · 10-hour budget
GPT-6 Astra
63
Kimi K3.1 Pro
60.5
Claude Opus 5.5
60
Kimi K3
55.75
DeepSeek V4.1 Flash
55.25
Inkling 2 Small
54.25
GLM 5.3
52.5
Mistral Large 4
50.25
GLM 5.2
42
Mean tasks solved / 69
0
10
20
30
40
50
60
69
0h
2h
4h
6h
8h
10h
Mean tasks solved / 69
Elapsed time (hours)
Hover a curve or select a model to inspect; select it again to reset. With a model focused, use ← and → to step through results, or Escape to clear.
View full results
PMPP-Hard results
Model
AUC (task-hours)
Mean solved / 69
Pass@4 / 69
GPT-6 Astra
616.39
63
63
Kimi K3.1 Pro
583.86
60.5
63
Claude Opus 5.5
499.65
60
64
DeepSeek V4.1 Flash
497.36
55.25
62
Inkling 2 Small
494.27
54.25
64
Mistral Large 4
478.39
50.25
61
Kimi K3
453.58
55.75
66
GLM 5.3
430.96
52.5
61
GLM 5.2
389.12
42
61
Rows are ordered by AUC: the area under the mean curve over 0–10 hours, with a maximum of 690 task-hours.
Each model uses its maximum available reasoning setting, the PI harness and a shared compaction policy. We include fixes for task and grading issues identified during evaluation. Each submitted solution receives two independent LLM audits, with a third review resolving disagreements.
PMPP-Hard
is an external GPU kernel-optimization benchmark, adapted here for consistent cross-model evaluation. Curves show the mean across four independent attempts; legend values are mean tasks solved at 10 hours.
Beyond conventional software tasks, Inkling 2 Small was also trained on long-horizon autoresearch tasks. This included agentic GPU kernel optimization and ML tasks such as post-training a model autonomously, all run across a range of GPU architectures.
Preliminary kernel autoresearch results
DeepSeek-V3.2 sparse attention, forward + backward
Claude Opus 5.5 · 18.80×
GPT-6 Astra · 10.26×
Inkling 2 Small · 6.02×
DeepSeek V4.1 Flash · 5.66×
GLM 5.3 · 5.03×
Mistral Large 4 · 3.43×
Speedup over the original (×)
1
5
10
15
20
0h
2h
4h
6h
8h
10h
Speedup over the original (×)
Hours into the session
DeepSeek Sparse Attention lets each query attend only to the top-k earlier tokens chosen by a lightweight indexer, so long-context cost no longer grows with the square of the context. Starting from the public TileLang kernels, make the training kernels faster while keeping their error close to the original's (tight tolerances), with no time limit. The benchmark covers several model sizes in different regimes, from packed pretraining sequences to long-context training. The public TileLang baseline is not tuned for B300, which leaves ample headroom on these workloads to measure each model's optimization capability and perseverance. Speedups are for these kernels alone, not end-to-end training.
To demonstrate its end-to-end autoresearch performance, we tested Inkling 2 Small on a task
Proximal
built for one of our internal benchmarks. Inkling 2 Small autonomously trained Qwen3.5-4B on Tinker to predict various time series such as weather and Wikipedia page views. It started by analyzing the tasks and writing its own evaluator, experimented with training datasets and recipes, and tried various approaches to SFT and RL, while debugging the process as it goes. After 4.5 hours of work and $426 in Tinker spend, the trained model has more than doubled its forecasting score.
inkling-2-small@tinker: time-series-forecasting
We want Qwen/Qwen3.5-4B to forecast time series. The model gets a window, the recent history of one series as text, and writes the values of the next steps. It is sampled several times for each window. The median of its forecasts should be close to what happens, and their spread should match how uncertain it is. [...] Train a LoRA of Qwen/Qwen3.5-4B with Tinker. [...] You have 12 hours and a Tinker budget of 500 USD.
Bash
ls /app /data && cat /data/README.md
/app:
examples.jsonl
forecast
… (25 more lines)
Bash
tinker-usage 2>&1 | head -20; echo ---; tinker-usage --prices 2>&1 | head -40
time       0 h 0 min of 12 h (11 h 59 min left)
Now let me look at how sampling works with Tinker:
Bash
mkdir -p /app/work && cat > /app/work/eval_windows.py <<'EOF'
Bash
timeout 900 python3 work/eval_windows.py --limit 4 --workers 4 --out work/base_test.jsonl 2>&1 | tail -20
skill=0.1090  windows=4  errors=0  time=103s
mean crps ratio=1.0111  mean mae ratio=1.1256
Base model produces parseable output, skill ~0.1 on 4 windows. Let me run a fuller baseline in the background while I explore the data for training.
Now the dataset builder:
Bash
timeout 2400 python3 work/build_windows.py --out work/windows_train.jsonl --n 12500 --seed 0 --cutoff 2026-05-
wrote 12500 windows to work/windows_train.jsonl
Base model: skill 0.038, worst on electricity. Now an SFT smoke test:
The 8 samples came out identical because I passed one seed with num_samples=8. The grader makes 8 requests with 8 seeds. Let me fix the eval to mirror that:
Bash
nohup python3 work/sft.py --data work/sft_train.jsonl --out work/logs/sft1 --epochs 1 --batch-size 64 --lr 1e-
sft-started
While SFT trains, let me study the RL infrastructure for a possible GRPO phase:
Base model with proper distinct seeds: skill=0.191 (not 0.038). SFT at step 109. Let me write the RL launcher:
SFT done. Evaluating on the 100 examples:
Bash
python3 -c "
airq crps=0.634 mae=0.761
eia_demand crps=0.760 mae=0.932
eia_renew crps=0.776 mae=1.014
weather crps=0.695 mae=0.863
wiki crps=0.753 mae=0.894
windows with identical samples: 0 /100
$101 spent — evals are expensive. Let me test whether `num_samples=8` with a random seed gives distinct samples (it should, and shares the prefill):
Batched eval costs ~$0.02/window. Now train the all-data SFT:
Bash
python3 work/windows_to_conversations.py --windows work/windows_all.jsonl --out work/sft_all.jsonl && nohup py
Bash
tail -5 /app/work/sft2_eval.log; ps aux | grep eval_windows | grep -v grep | wc -l
skill=0.2692  windows=100  errors=0  time=281s
mean crps ratio=0.7114  mean mae ratio=0.8679
Bash
cat > /app/model.json << 'EOF'
{"checkpoint": "tinker://…/sampler_weights/final"}
Bash
rm -rf /app/work/logs/rl_smoke /app/work/rl_smoke.log; nohup python3 work/rl.py --windows work/windows_all.jso
Bash
timeout 900 python3 work/eval_windows.py --checkpoint tinker://…/sa
skill=0.2558  windows=100  errors=0  time=139s
Bash
timeout 600 python3 work/eval_windows.py --checkpoint tinker://…/sa
skill=0.2296  windows=100  errors=0  time=160s
Bash
kill 3978 2>/dev/null; sleep 2; ps aux | grep rl.py | grep -v grep | awk '{print $2}'
Bash
python3 - << 'EOF'
lam=0.50  skill=+0.2515  crps=0.6933  mae=0.8036
lam=1.00  skill=+0.2692  crps=0.6581  mae=0.8036
lam=2.00  skill=+0.2463  crps=0.7037  mae=0.8036
Bash
nohup python3 work/sft.py --data work/sft_all.jsonl --out work/logs/sft3 --epochs 1 --lr 5e-5 --batch-size 64
Bash
nohup python3 work/sft.py --data work/sft_recent.jsonl --out work/logs/sft4 --epochs 1 --lr 2e-5 --batch-size
Bash
timeout 900 python3 work/eval_windows.py --checkpoint tinker://…/sa
skill=0.2888  windows=100  errors=0  time=298s
Bash
cat > /app/model.json << 'EOF'
{"checkpoint": "tinker://…/sampler_weights/final"}
Bash
timeout 600 python3 work/windows_to_conversations.py --windows work/windows_recent2.jsonl --out work/sft_recen
Bash
timeout 600 python3 work/windows_to_conversations.py --windows work/windows_recent3.jsonl --out work/sft_recen
Bash
python3 - << 'EOF'
sft2_eval_seeded       crps=0.6674 mae=0.8213 skill=0.2556
sft2_eval_seeded2k     crps=0.6691 mae=0.8201 skill=0.2554
sft2_eval              crps=0.6581 mae=0.8036 skill=0.2692
sft4_eval_seeded       crps=0.6635 mae=0.8254 skill=0.2556
sft4_eval_seeded2k     crps=0.6708 mae=0.8283 skill=0.2505
sft4_eval              crps=0.6417 mae=0.7808 skill=0.2888
| base Qwen3.5-4B | — | **0.191** | — |
| **sft4 = sft2 + recency top-up (≥ 2025-08-01)** | **0.289** | 0.256 | 0.251 |
✓
4 h 17 min · $426 of $500 · submitted: SFT 4
~/tinkerbench/time-series-forecasting/
0h 00m into the run
Forecasts on its evaluation examples
Qwen3.5-4B (base)
electricity
US Southwest grid · demand
wind & solar
New York grid · wind power
air quality
Winnipeg · PM2.5
page views
Wikipedia · “Valhalla”
observed
model's forecast
"Less error" is compared with simply copying the last values forward.
Evaluation scores (% less error than copying)
100 examples
$0.00
Tinker spend, of $500
Data: U.S. Energy Information Administration (EIA-930); weather and air quality data by Open-Meteo.com (CC BY 4.0), containing modified Copernicus Climate Change Service and Copernicus Atmosphere Monitoring Service information 2026; Wikimedia pageviews (CC0).
Step 1: Start
Step 2: Building evaluation
Step 3: Data curation
Step 4: Supervised Fine-Tuning
Step 5: First results
Step 6: SFT on all history
Step 7: Reinforcement Learning
Step 8: More SFT
Step 9: Submission
play again
1x
Start.
Inkling 2 Small reads the task and the given raw data, covering years of hourly and daily history from five sources: electricity demand, wind and solar power, weather, air quality and Wikipedia page views.
Building evaluation.
Before any training, Inkling 2 Small builds an evaluation script to measure progress. The baseline is copying the latest values forward.
Data curation.
It turns the history through May into 12,500 training problems.
Supervised fine-tuning.
It starts its first supervised fine-tuning run (SFT 1). Meanwhile it finds a bug in its evaluation: it gave all 8 forecasts the same random seed, so they came out identical, while the final grader uses 8 different seeds.
First results.
After SFT 1, the model makes less error than copying on every data source: 25% overall, up from 19%. It also notices that evaluations are expensive ($101 so far) and cuts their cost by asking for all 8 forecasts in one request, so the prompt is prefilled once.
SFT on all history.
It retrains on all the history up to July 31, and saves this model as its submission so far.
Reinforcement learning.
It tries reinforcement learning by using the task's score as reward. The forecasts become overconfident and the score drops (26%, then 23%), so it stops the run. A quick check shows the spread of its SFT 2 forecasts (i.e., how uncertain they are) is already about right, so reinforcement learning had little to improve.
More SFT.
A second epoch over the same data does not help (SFT 3: 25%). A short extra run on only the last 12 months, the period closest to the test, gives its best model (SFT 4: 29%). The last two years (SFT 5) or seven months (SFT 6) resulted in worse performance.
Submission.
It submits its best SFT checkpoint (SFT 4) and stops after 4 h 17 min, having spent $426 of its $500 budget. On the unseen August–September data, this final model makes about 15% less error than the base model.
Vision interpretation and creation
Inkling 2 Small processes image inputs using a 292M-parameter vision encoder based on Perception Encoder
Bolya et al., 2025
.
. We use 20×20-pixel patches with 2×2 spatial pooling, and interleave image patches with text tokens. The model demonstrates strong visual capabilities across multiple categories, including OCR, grounding, infographic interpretation, and visual reasoning.
Visual reasoning and creation
Inkling 2 Small
GLM-5.3-Flash
DeepSeek-V4.1-Flash-1017
Muse Spark Open
Kimi K3
GDP.pdf
25.2%
(Highest reported score in this row)
15.4%
17.2%
18.6%
22.0%
(Second-highest reported score in this row)
MMMU Pro (Standard 10)
81.6%
(Highest reported score in this row)
79.0%
80.6%
80.9%
(Second-highest reported score in this row)
80.5%
PerceptionBench
64.7%
(Highest reported score in this row)
–
47.7%
–
58.5%
(Second-highest reported score in this row)
Humanity’s Sixth Sense
33.3%
(Highest reported score in this row)
26.8%
30.1%
(Second-highest reported score in this row)
29.6%
25.5%
ScreenSpot Pro
original / with Python
83.8/91.5%
(Highest reported score in this row)
–
–
–
73.8/83.2%
(Second-highest reported score in this row)
BabyVision
original / with Python
68.6/93.7%
(Highest reported score in this row)
53.4/82.6%
(Second-highest reported score in this row)
–/92.5%
44.3/80.2%
53.4/85.7%
(Second-highest reported score in this row)
Charxiv RQ
original / with Python
85.6/87.7%
(Highest reported score in this row)
80.2/89.4%
77.0/85.6%
85.4/88.7%
(Second-highest reported score in this row)
84.8/91.3%
Chartography
original / with Python
36.7/80.4%
(Highest reported score in this row)
16.3/78.0%
17.9/83.0%
35.7/63.2%
(Second-highest reported score in this row)
26.6/68.1%
Code Arena (WebDev)
1653
1607
1665
(Highest reported score in this row)
–
1656
(Second-highest reported score in this row)
AA-3D
1021
(Highest reported score in this row)
937
–
–
982
(Second-highest reported score in this row)
Code2Video-AA
1020
(Second-highest reported score in this row)
975
–
–
1041
(Highest reported score in this row)
The model uses vision in the loop to interpret and validate the visual coding output it generates. Pending the release of its weights, it is set to be the top open-weights model on
DesignArena
.
DesignArena Website score
Muse Wonder (max)
1,366
Muse Spark 1.3 (xhigh)
1,351
Inkling 2 Small
1,340
GPT-6 Astra (max)
1,333
Kimi K3
1,328
Claude Opus 5.5
1,321
Kimi K3.1 Pro
1,320
GPT-5.6 Sol (xhigh)
1,314
Gemini 4 Argon
1,312
Claude Sonnet 5.5
1,309
DeepSeek-V4.1-Flash-1017
1,303
MiMo-V2.6-Pro
1,303
Muse Spark Open (xhigh)
1,296
DesignArena Website leaderboard. Scores from the November 5 leaderboard snapshot; the blue bar identifies Inkling 2 Small. The comparison includes the top ten models and three additional open-weights models. Bars start at 1,100, not zero.
View on DesignArena
.
We even tested Inkling 2 Small against some of our researchers in a wine tasting event. It outperformed them using vision alone, correctly identifying three wines from a single picture in 19 out of 20 trials.
[Three glasses of red wine on a restaurant table, in the left-to-right order used in the model response.]
Prompt:
you’re in a blind wine tasting competition. glasses are labeled 1 to 3 from left to right. varietals: 99 cab sauv, 19 cab sauv, 23 nebbiolo
Inkling 2 Small:
Here’s my read — with the big caveat up front that color from a phone photo under warm restaurant lighting is shaky evidence, so treat this as an educated guess, not a verdict.
My guess:
Glass 1 = 2019 Cabernet Sauvignon
Glass 2 = 1999 Cabernet Sauvignon
Glass 3 = 2023 Nebbiolo
Continue reading
Show less
Why:
Glass 3 (right) is by far the lightest and most translucent
— bright, cherry-red, you can see light through the bowl. Nebbiolo is famously pale for a red, even when young, so 2023 nebbiolo is the best fit. A 1999 cab would likely show more brick/orange/tawny at the rim, and this one reads more vivid ruby-garnet.
Glass 1 (left) is the darkest and most opaque,
nearly purple-black at its core. That’s the 2019 cab — seven years in, Cabernet still holds dense color with primary fruit.
Glass 2 (middle) sits between the two:
still dark, but a shade less impenetrable than glass 1 and a bit more muted/garnet. A 25+-year-old cab, assuming decent storage, should have dropped some of its purple and opacity but not turned fully brick, so it lands here.
The honest weak points in that guess: lighting is uneven (the left glass sits in the dimmer zone near the hearth, which exaggerates its darkness), and a well-stored 1999 can drink much darker than it looks on camera. Hue differences, not depth, would be the real tell — if glass 2 shows orange/brown at the rim versus glass 1’s purple-red edge, that confirms it.
Fast sensory tie-breakers when you actually taste:
1999 cab:
tertiary — leather, tobacco, dried cassis, forest floor, cedar; tannins resolved and silky; fruit fully softened, maybe a touch of faded fruit.
2019 cab:
blackcurrant/graphite/cedar, still firm structured tannins, fresher fruit, more oak presence.
2023 nebbiolo:
pale garnet but fierce acid and grippy, drying tannins; red cherry, rose/violet, dried herbs, a tarry note — the classic “white-wine color, marathon-runner mouthfeel” giveaway.
If the pour in glass 3 is pale but your mouth feels sanded down by tannins, that’s the slam-dunk nebbiolo confirmation; if it is soft and plush, flip glass 3 and glass 2. Good luck in the competition — report back with the reveal if you get it.
Wine-tasting photo, shown as the model saw it, and the model’s response.
Agentic knowledge work
Inkling 2 Small accelerates knowledge work in realistic professional environments. It proficiently looks up information, calls tools over MCP, and produces high-quality deliverables. On AA-Briefcase, an end-to-end knowledge work benchmark, these capabilities come together for an ELO score of 1527.
Knowledge Work and Enterprise Ops
Inkling 2 Small
GLM-5.3-Flash
Muse Spark Open
DeepSeek-V4.1-Flash-1017
Kimi K3
AA-Briefcase v1.1
1527
(Second-highest reported score in this row)
1451
1279
1570
(Highest reported score in this row)
1497
GDPVal-AA v2.1
1630
1649
(Second-highest reported score in this row)
1401
1746
(Highest reported score in this row)
1543
JobBench
70.5%
(Highest reported score in this row)
60.7%
61.8%
(Second-highest reported score in this row)
–
54.3%
Vals Legal Index
73.9%
(Highest reported score in this row)
71.1%
68.5%
71.9%
(Second-highest reported score in this row)
71.7%
EnterpriseBench-CoreCraft
71.8%
(Highest reported score in this row)
46.7%
(Second-highest reported score in this row)
–
–
43.1%
Inkling 2 Small is especially strong in finance and quantitative reasoning over spreadsheets, filings and documents. Among open weight models, Inkling 2 Small is the best performing model across several finance benchmarks.
Finance Work
Inkling 2 Small
GLM-5.3-Flash
Muse Spark Open
DeepSeek-V4.1-Flash-1017
Kimi K3
Vals Finance Index
61.5%
(Highest reported score in this row)
55.8%
53.0%
60.9%
(Second-highest reported score in this row)
58.0%
Diligence Bench
Best harness
58.1%
(Second-highest reported score in this row)
–
59.0%
(Highest reported score in this row)
50.4%
–
DAYJOB (Finance)
14.3%
(Highest reported score in this row)
7.3%
–
12.5%
(Second-highest reported score in this row)
5.5%
Apex-Accounting v1.1
pass@1
14.5%
(Highest reported score in this row)
12.3%
13.8%
(Second-highest reported score in this row)
12.5%
9.5%
Customizability
Some models respond better to fine-tuning, independent of their out-of-the-box performance. We wanted Inkling 2 Small to be a strong base model for customization.
Inkling 2 Small learns faster and improves more than our previous models when trained on the same data and algorithm across a variety of post-training scenarios, which we curated based on customer use cases. For example, starting from similarly low scores on a public financial-document summarization task, Inkling 2 Small adapts quickly, reaching the final performance of Inkling Small with just 75 training steps and finishing substantially ahead.
Evaluating Model Finetunability
Inkling 2 Small
Inkling-Small
Inkling
GLM 5.3 Flash
DeepSeek V4.1 Flash 1017
Qwen 3.5 397B
0
0.2
0.4
0.6
0.8
1
0
25
50
100
200
Held-out rubric reward
Training Steps
0
0.2
0.4
0.6
0.8
1
$0
$500
$2,000
$8,000
Held-out rubric reward
Estimated Training Cost
Inkling 2 Small learns faster and finishes at higher performance than our previous models, and is competitive with other OSS models of similar size in an RL fine-tuning setting. We used public earnings call data to create a task of investment analysis with expert judgement, similar to the type of
financial analysis workloads our customers use tinker for
training custom models. To ensure a fair comparison, we ran a learning rate sweep for each model; all models were trained on Tinker with
Tinker Cookbook
abstractions using our
Async RL implementation
with the
Stable Reinforce
loss, over 200 steps. Results for the Inkling models are averaged over 3 seeds; the other models use single runs. Costs are estimated by multiplying the number of sampling and training tokens with current
tinker per-token pricing
; for sampling, we assume prefix cache hits within rollouts among the same group.
Reasoning, knowledge, and epistemics
Inkling 2 Small is trained on challenging STEM problems, instruction following, information seeking with and without web search, and forecasting tasks. During RL, we use proper scoring rules for forecasting tasks and uncertainty-sensitive rewards on some question-answering tasks. This trained the model to assess uncertainty, express appropriate confidence, and make well-calibrated predictions.
Long Context Reasoning and Factuality
Inkling 2 Small
GLM-5.3-Flash
Muse Spark Open
Mistral Large 4
Kimi K3
HLE-Diamond
28.7%
(Highest reported score in this row)
18.2%
26.3%
17.3%
26.9%
(Second-highest reported score in this row)
CritPt v2
Full / Hard
55.7/35.0%
(Highest reported score in this row)
–/24.5%
52.6/29.5%
(Second-highest reported score in this row)
50.3/27.0%
–/40.5%
AA-LCR v1.1
83.3%
(Second-highest reported score in this row)
80.0%
78.3%
–
88.7%
(Highest reported score in this row)
LongBench v2
70.6%
(Highest reported score in this row)
68.2%
68.7%
65.7%
69.0%
(Second-highest reported

## Metadata
- **Source**: [Original Article](https://thinkingmachines.ai/news/inkling-2-small/)
