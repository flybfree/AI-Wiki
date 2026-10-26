# Summary: 2026-10-22_05-44-41Z_WhatOpen_SourceProjectsTellTheirCodingAgents_ACens.md
Saved: 2026-10-25 21:55
Source: 2026-10-22_05-44-41Z_WhatOpen_SourceProjectsTellTheirCodingAgents_ACens.md
Model: None

---

## Summary
This paper presents a comprehensive census of instruction files, specifically AGENTS.md and CLAUDE.md, within popular open-source GitHub repositories to understand how developers guide coding agents. The study analyzes these files across thirteen programming languages to identify the types of directives provided, ranging from project knowledge to workflow rules. By employing model-assisted annotation combined with human review, the author reveals significant patterns in how projects instruct AI agents, highlighting discrepancies in attribution policies and the prevalence of automated generation. The work contributes a detailed taxonomy of agent instructions and releases annotated datasets to facilitate further research into the emerging practice of repository-level agent guidance.

## Key Contributions
- **Prevalence and Structure of Agent Instructions:** The study finds that agent instruction files appear in a significant portion of active repositories, with CLAUDE.md frequently pointing to AGENTS.md when both exist, suggesting a standardization trend or hierarchical structure in how projects manage agent directives.
- **Analysis of Directive Content and Rationale:** Annotations reveal a mix of project-specific knowledge and operational rules. Notably, while collaboration rules specify concrete requirements like test plans and commit formats, a substantial percentage of directives lack explicit reasoning, which may hinder agent interpretability.
- **Inconsistencies in AI Attribution Policies:** The paper highlights conflicting norms regarding AI contributions: commit message rules tend to prohibit AI attribution, whereas pull request rules more often require disclosure, indicating a lack of consensus on transparency standards for AI-assisted coding.
- **Impact of Automated Generation and Editing:** A significant portion of instruction sets contain generator-associated signatures or tool-inserted blocks, yet four out of five are edited after creation. This suggests that while automation initiates these files, human curation remains critical to their final form and effectiveness.

## Methodology
The authors conducted a systematic census by identifying popular, active GitHub repositories across thirteen different programming languages. Each repository’s root-level AGENTS.md and CLAUDE.md files were treated as a unified instruction set for analysis. The methodology involved extracting these files and analyzing their statements through a hybrid approach: model-assisted annotation was used to categorize instructions into taxonomies (e.g., code rules, building processes, workflow guidelines), followed by human review to validate and refine these classifications. The study also examined the provenance of these files, checking for generator signatures, shared text blocks, and creation commits marked as AI-generated, while tracking post-creation edits to assess human involvement.

## Results
The analysis shows that agent instructions are present in a notable fraction of repositories, with higher adoption rates among the most-starred projects. The content analysis reveals that directives often focus on practical project knowledge and strict workflow rules, such as specific commit formats or test requirements. However, many directives lack explanatory context. Regarding attribution, there is a clear divergence: commit-level rules discourage AI credit, while pull-request guidelines encourage transparency about AI involvement. Furthermore, the study finds that LLM and agent-related projects are over-represented among adopters of these files. Crucially, the results indicate that different language models agree closely with each other on topic assignments but diverge significantly from human reviewers, highlighting a potential bias or limitation in using automated tools for semantic annotation of such instructions.

## Significance
This research is significant because it provides the first large-scale empirical evidence on how open-source projects are adapting to the era of AI coding agents. By documenting the content and structure of AGENTS.md and CLAUDE.md files, the paper offers insights into best practices and emerging norms for human-AI collaboration in software development. It highlights critical gaps, such as the lack of reasoning in directives and inconsistent attribution policies, which could inform better tool design and policy-making for AI-assisted coding. Additionally, the caution regarding model agreement versus human judgment serves as a vital warning for researchers relying on automated annotation for understanding developer intent and agent behavior.

## Related Concepts
- **AGENTS.md / CLAUDE.md:** Standardized instruction files used to guide coding agents within repositories.
- **Model-Assisted Annotation:** Using LLMs to classify text, validated by human review.
- **AI Attribution Policies:** Norms regarding how AI contributions are credited in commits and pull requests.
- **Repository-Level Agent Guidance:** The practice of embedding agent instructions directly into codebases.
- **Taxonomy of Agent Instructions:** Categorization of directives into project knowledge, code rules, and workflow processes.
