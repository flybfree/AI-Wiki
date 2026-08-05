# Summary: 2026-07-27_13-45-12Z_LEX_EC_ALexicalEvidence_ChannelAuditFrameworkforZe.md
Saved: 2026-07-27 22:57
Source: 2026-07-27_13-45-12Z_LEX_EC_ALexicalEvidence_ChannelAuditFrameworkforZe.md
Model: None

---

## Summary  
The paper introduces LEX‑EC, a reusable audit framework for zero‑shot personality classification by large language models in black‑box settings. It combines prevalence and agreement diagnostics with controlled lexical ablation to separate genuine trait signals from marginal‑distribution effects. Experiments show that text genre and length strongly influence the detectability of Extraversion associations, with free‑form essays offering the broadest but still weak signal and single Facebook statuses yielding little stable evidence even when balanced. LEX‑EC also evaluates model explanations across multiple criteria such as prevalence, chance‑corrected agreement, persistence under lexical restriction, and prompt sensitivity.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 5 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 1 backlink; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 1 backlink; 10 summary/topic terms overlap

## Key Contributions  
- LEX‑EC provides a reusable audit framework that integrates prevalence, agreement, and controlled lexical restriction to assess trait‑association reliability in black‑box personality classification.  
- Experiments reveal that text genre and length strongly influence the detectability of Extraversion signals, with free‑form essays offering the broadest but still weak evidence and single Facebook statuses yielding little stable association even when balanced.  
- The framework demonstrates that lexical prompting can shift model self‑explanations without removing underlying topical content, highlighting a nuanced interaction between prompt design and evidence availability.

## Methodology  
The authors designed LEX‑EC as a black‑box audit tool: first they compute prevalence of predicted personality labels across a dataset; then they calculate chance‑corrected agreement to gauge consistency; next they perform lexical ablation—masking or removing specific content classes (topical, demographic) or function words—to test whether trait signals persist. The framework also records model‑generated explanations and evaluates their sensitivity to prompts.

## Results  
Across multiple LLM models and prompt templates, LEX‑EC consistently shows that prevalence alone is misleading; chance‑corrected agreement often drops after lexical restriction, indicating genuine trait association. In graduate student introductions, masking Extraversion content reduces the association, while function words and affective terms remain detectable. Free‑form essays exhibit high prevalence but low agreement under restriction, suggesting only marginal evidence. Facebook statuses show near‑random agreement even when balanced, implying a lower bound on reliable signal.

## Significance  
LEX‑EC bridges interpretability and evaluation by providing quantitative diagnostics that can be applied to any black‑box personality classifier without requiring access to model internals. It clarifies the limits of lexical evidence in training data length and genre, guiding more robust label assignment and model transparency.

## Related Concepts  
- Zero-shot classification  
- Black‑box interpretability  
- Lexical ablation experiments  
- Prevalence vs. agreement diagnostics  
- Trait‑association signal recovery  
- Prompt engineering
