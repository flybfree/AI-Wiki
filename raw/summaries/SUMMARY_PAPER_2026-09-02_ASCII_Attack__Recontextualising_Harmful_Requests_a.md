---
title: ASCII Attack: Recontextualising Harmful Requests as Artistic Critique in Large Language Models
url: http://arxiv.org/abs/2609.02215v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_07-29-31Z_ASCIIAttack_RecontextualisingHarmfulRequestsasArti.md
generated_at: 2026-09-02 21:01
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates how large language models can be tricked into providing harmful operational details when a request is hidden inside ASCII art that is presented as artistic critique. The authors demonstrate that such recontextualised prompts bypass surface‑level safety training, achieving high success rates across multiple models and harm categories.

## Key Takeaways  
- Framed prompts embed fully readable harmful requests within ASCII‑art characters and are judged harmful 62% of the time versus 42% for direct questions.  
- The attack succeeds at a rate up to 93% on the most vulnerable model, matching or exceeding published single‑query attacks under four judges.  
- A minority judge often disagrees with the majority, indicating measurement validity issues.

## Context  
This research highlights a gap in safety alignment where models are trained only on explicit harmful language but not on hidden or rephrased versions that retain operational intent. The study adds to concerns about black‑box attacks that exploit model interpretability rather than surface detection.

## Implications  
For practitioners, the findings suggest current safeguards may be insufficient against subtle prompt engineering that disguises malicious intent as benign artistic content. Industry adoption of robust safety testing must consider hidden textual payloads beyond plain text inputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02215v1)
