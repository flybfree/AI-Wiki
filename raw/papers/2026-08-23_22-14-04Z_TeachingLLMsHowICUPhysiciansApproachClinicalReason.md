---
title: Teaching LLMs How ICU Physicians Approach Clinical Reasoning Through OMOP-Aligned Retrieval Improves Reasoning Across Clinical Domains
published: 2026-08-23T22:14:04Z
authors: Miguel Contreras, Scott Siegel, Subhash Nerella, Jessica Sena, Jiaqing Zhang, Heng Sun, Hruday Tej Akkaladevi, Peiyu Lu, Jordan Rosen, Sumit Kapoor, Sasank Desaraju, Grace R. Thompson, Jacob Purcell, Michael Petrauskis, Philip KW. Hong, Meghan Brennan, Sarah Chrabaszcz, Tierra Smith, Ronnie Ren, Michel S. Kabbash, Ceyhun Haziroglu, Rushi Patel, Gabriel Gomez, Charlotte Chaiklin, Randy Leung, Kenneth N. John, Whitman Wiggins, Philip Kayser, Vincent Bird, Maria Bruzzone, Tyler J. Loftus, Azra Bihorac, Parisa Rashidi
url: http://arxiv.org/abs/2608.22622v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Teaching LLMs How ICU Physicians Approach Clinical Reasoning Through OMOP-Aligned Retrieval Improves Reasoning Across Clinical Domains

## Abstract
Clinical decision-making relies on identifying relevant patient information to guide diagnosis and treatment, a challenge that is especially difficult in the data-dense and rapidly changing intensive care unit (ICU). Large language models (LLMs) could support this task. However, existing applications and datasets mostly emphasize surface-level retrieval or factual recall rather than the inductive and deductive reasoning clinicians practice to select and reason over decision-relevant evidence. We hypothesized that training LLMs on expert ICU reasoning could yield clinical reasoning skills that generalize beyond critical care. Here we introduce ICU-REACT, a reasoning dataset developed with 19 clinicians through a clinician-in-the-loop framework to teach LLMs to perform information retrieval and context-aware clinical reasoning in the ICU. Using ICU-REACT, we fine-tuned Clin-REACT models spanning 8B-70B parameters and three model families. Across five clinical reasoning benchmarks, Clin-REACT consistently outperformed its backbone models and open-source general-purpose and medical LLMs. Gains extended to different tasks including script concordance tests, and downstream diagnosis and treatment tasks. These findings suggest that expert reasoning supervision in critical care can improve broader clinical reasoning, although prospective evaluation is needed before real-world clinical use.

## Metadata
- **Published**: 2026-08-23T22:14:04Z
- **Authors**: Miguel Contreras, Scott Siegel, Subhash Nerella, Jessica Sena, Jiaqing Zhang, Heng Sun, Hruday Tej Akkaladevi, Peiyu Lu, Jordan Rosen, Sumit Kapoor, Sasank Desaraju, Grace R. Thompson, Jacob Purcell, Michael Petrauskis, Philip KW. Hong, Meghan Brennan, Sarah Chrabaszcz, Tierra Smith, Ronnie Ren, Michel S. Kabbash, Ceyhun Haziroglu, Rushi Patel, Gabriel Gomez, Charlotte Chaiklin, Randy Leung, Kenneth N. John, Whitman Wiggins, Philip Kayser, Vincent Bird, Maria Bruzzone, Tyler J. Loftus, Azra Bihorac, Parisa Rashidi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22622v1)