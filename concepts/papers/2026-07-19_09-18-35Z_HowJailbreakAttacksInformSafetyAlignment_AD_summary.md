# Summary: 2026-07-19_09-18-35Z_HowJailbreakAttacksInformSafetyAlignment_ADefender.md
Saved: 2026-07-24 00:10
Source: 2026-07-19_09-18-35Z_HowJailbreakAttacksInformSafetyAlignment_ADefender.md
Model: None

---

## Summary  
The paper proposes a defender‑centric evaluation framework for jailbreak attacks on large language models, arguing that safety improvement is more relevant than attack success rate. It introduces A‑MESS, a set‑agnostic Shapley‑based method to attribute and select minimal effective attacks from black‑box utility observations. By shifting focus from attacker success to safety impact, the work offers a novel paradigm for responsible AI testing.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 5 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 1 backlink; 13 summary/topic terms overlap
- [[concepts/papers/2026-08-01_13-21-55Z_Select_And_Extract_ALightweightPluginforRet_summary.md|Summary: 2026-08-01_13-21-55Z_Select_And_Extract_ALightweightPluginforRetrieval_.md]] — 4 title terms overlap; 11 summary/topic terms overlap; semantic match 0.11

## Key Contributions  
- Finding 1: Defender‑centric evaluation of jailbreak attacks prioritizes safety improvements over attack success rate.  
- Finding 2: A‑MESS provides a set‑agnostic Shapley‑based attribution and selection framework for black‑box utility data.  
- Finding 3: Direct subset optimization outperforms attacker‑centric rankings and attribution‑only selection in enhancing safety.

## Methodology  
The authors adopt a defender perspective, treating jailbreak attacks as resources for training safety. They collect utility observations (safety improvements) from using attack subsets, then apply A‑MESS to estimate AttackSHAP scores via Shapley value approximation, selecting compact subsets under budget constraints using greedy or surrogate optimization. The Shapley‑based AttackSHAP score quantifies each attack's marginal contribution to safety gains.

## Results  
Experiments on controlled utility landscapes and real LLM safety tasks show that ASR rankings correlate poorly with defender‑centric utility. AttackSHAP estimates accurately with few queries, and greedy subset selection yields higher safety gains than alternative methods. The framework reduces attack sets while preserving or improving safety outcomes.

## Significance  
This work reframes jailbreak evaluation to align with real‑world safety goals, offering a principled way to curate attacks for training and mitigating unintended harms. It bridges attribution theory (Shapley values) with practical LLM deployment, encouraging safer AI development.

## Related Concepts  
- Jailbreak attacks on LLMs  
- Defender‑centric evaluation  
- Shapley value and AttackSHAP  
- Black‑box subset utility  
- Greedy optimization for resource selection
