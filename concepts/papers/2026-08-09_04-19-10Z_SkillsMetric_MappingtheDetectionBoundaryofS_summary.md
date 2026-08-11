# Summary: 2026-08-09_04-19-10Z_SkillsMetric_MappingtheDetectionBoundaryofStaticAn.md
Saved: 2026-08-10 23:12
Source: 2026-08-09_04-19-10Z_SkillsMetric_MappingtheDetectionBoundaryofStaticAn.md
Model: None

---

## Summary  
The paper introduces **SkillsMetric**, a five‑stage static analysis framework designed to evaluate the security of skill packages that augment LLM‑based agents. By scoring skills across pattern density, statistical anomaly, dataflow taint, import anomaly, and capability mismatch dimensions, SkillsMetric aims to map the detection boundary between benign and malicious skill usage. The authors demonstrate that their approach can achieve high performance on a large adversarial dataset while revealing fundamental blind spots in current static‑analysis techniques.  

## Key Contributions  
- [Finding 1] SkillsMetric provides a comprehensive five‑stage scoring model that quantifies risk across multiple security dimensions for skill packages.  
- [Finding 2] The authors construct an adversarial evaluation set of 2,266 skills covering 16 attack types and assess the framework on the full SkillMD‑138K corpus.  
- [Finding 3] They identify two critical blind spots: host‑destruction attacks evade all five stages (0 % detection) and prompt‑injection attacks achieve only 42 % detection.  

## Methodology  
The methodology follows a five‑stage static analysis pipeline. First, pattern density measures how many known malicious patterns appear in the skill code. Second, statistical anomaly detects deviations from typical skill usage statistics. Third, dataflow taint checks whether the skill can leak or modify sensitive data. Fourth, import anomaly flags suspicious external library or command imports. Finally, capability mismatch evaluates if the skill’s declared abilities conflict with its actual behavior. The authors build an adversarial dataset of 2,266 skills spanning code‑level, system‑level, and semantic threats, then evaluate SkillsMetric on the SkillMD‑138K corpus using 5‑fold cross‑validation.  

## Results  
The framework achieves an AUC of 0.93 and a 5‑fold cross‑validated F1 score of 73.4 % ± 0.5 %. It detects data exfiltration attacks with 93 % precision and steganographic payloads with 93 % recall, indicating strong performance on high‑impact threats. However, the detection rates drop to 0 % for host‑destruction attacks and 42 % for prompt‑injection attacks, confirming the identified blind spots.  

## Significance  
These results show that static analysis alone cannot reliably secure skill packages; it misses low‑level destructive commands and subtle natural‑language manipulations. The findings motivate a defense‑in‑depth architecture that combines fast static pre‑screening with deeper semantic review to catch the remaining vulnerabilities.  

## Related Concepts  
Agent Skills, static analysis, SkillMD‑138K corpus, AUC, F1 score, data exfiltration, steganography, prompt injection, defense‑in‑depth, pattern density, statistical anomaly, dataflow taint, import anomaly, capability mismatch.
