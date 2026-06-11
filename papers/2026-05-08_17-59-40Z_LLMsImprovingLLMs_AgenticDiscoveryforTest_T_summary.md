# Summary: 2026-05-08_17-59-40Z_LLMsImprovingLLMs_AgenticDiscoveryforTest_TimeScal.md
Saved: 2026-05-10 22:54
Source: 2026-05-08_17-59-40Z_LLMsImprovingLLMs_AgenticDiscoveryforTest_TimeScal.md
Model: None

---


## Summary  
The paper introduces AutoTTS, an environment‑driven framework that automatically discovers test‑time scaling (TTS) strategies instead of relying on handcrafted heuristics. By formulating TTS as a controller synthesis problem over pre‑collected reasoning trajectories and probe signals, the authors enable cheap evaluation without repeated LLM calls, thereby improving the accuracy–cost tradeoff for large language models.

## Key Contributions  
- [Finding 1] AutoTTS provides an automated environment that discovers TTS heuristics from scratch.  
- [Finding 2] The width‑depth TTS problem is cast as controller synthesis where controllers decide when to branch, continue, probe, prune, or stop using trajectory and probe data.  
- [Finding 3] Beta parameterization makes the search tractable and supplies fine‑grained feedback to diagnose why a discovered program fails.

## Methodology  
The authors build a discovery environment that evaluates each controller cheaply through synthetic probes rather than invoking the LLM repeatedly. Reasoning trajectories are collected from model inference, and controllers synthesize TTS programs that control branching, probing, pruning, or stopping decisions. Beta parameters guide the search space and provide diagnostic signals to refine the discovered strategies.

## Results  
Experiments on mathematical reasoning benchmarks show that AutoTTS‑discovered strategies outperform strong manually designed baselines in overall accuracy–cost tradeoff. The methods generalize across held‑out benchmarks and various model scales. The entire discovery process costs only $39.9 and takes 160 minutes; the code is open‑source at https://github.com/zhengkid/AutoTTS.

## Significance  
Automating TTS design reduces research effort, eliminates costly LLM calls during evaluation, and democratizes access to better test‑time scaling improvements, enabling scalable model enhancements without prohibitive resource expenditure.

## Related Concepts  
Test‑Time Scaling (TTS), controller synthesis, environment‑driven discovery, beta parameterization, reasoning trajectories, probe signals, width‑depth TTS.

[[LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling]]