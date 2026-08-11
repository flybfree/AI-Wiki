# Summary: 2026-07-30_08-03-36Z_STEREODISCO_DiscoveringStereotypicalityinLLMs.md
Saved: 2026-07-30 21:41
Source: 2026-07-30_08-03-36Z_STEREODISCO_DiscoveringStereotypicalityinLLMs.md
Model: None

---

## Summary  
The paper proposes STEREODISCO, a framework that maps LLM internal representations onto geometric axes derived from WordNet antonym pairs, enabling systematic detection of stereotypical semantic associations within language models. By probing the model’s activation space for these axes and applying statistical tests, it reveals which stereotypes are encoded more strongly than those documented in social psychology. The study applies STEREODISCO to LLAMA‑3‑8B‑INSTRUCT and MISTRAL‑7B‑INSTRUCT, showing agreement among models exceeds human judgments on certain group ratings. It also uncovers previously unexamined axes such as humble vs proud and cowardly vs brave.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- Finding 1: STEREODISCO identifies a large set (~2000) of candidate semantic axes from WordNet antonyms, providing a systematic basis for stereotype analysis.  
- Finding 2: The framework demonstrates that LLMs exhibit stronger stereotypical associations on social group dimensions than human annotators, indicating divergence between model‑encoded and psychological stereotypes.  
- Finding 3: STEREODISCO uncovers novel axes (humble vs proud, narrow‑minded vs broad‑minded, cowardly vs brave) that were not investigated in prior work.

## Methodology  
The authors construct candidate axes by extracting antonym pairs from WordNet synsets and treating each pair as a geometric axis in the high‑dimensional activation space of LLMs. They recover these axes via probing queries that measure the model’s response to stimulus words, yielding projection vectors for each concept. A statistical test compares the variance along each axis across model outputs, flagging axes with significant stereotype signals.

## Results  
Experiments on two instruction fine‑tuned LLMs show that both models agree more closely with each other than with human raters when rating social groups (e.g., “aggressive” vs “calm”). The statistical test reveals high significance for axes like humble–proud and cowardly–brave, confirming their stereotypical nature. These findings extend prior work by offering a quantitative, model‑internal perspective on stereotype representation.

## Significance  
STEREODISCO bridges social psychology and AI research, providing an empirical method to detect hidden biases within LLMs that may affect downstream applications such as content moderation or recommendation systems. By exposing axes not previously studied, it opens avenues for targeted debiasing strategies.

## Related Concepts  
- Semantic differential  
- Social stereotypes  
- WordNet antonym pairs  
- LLM probing  
- Stereotypicality
