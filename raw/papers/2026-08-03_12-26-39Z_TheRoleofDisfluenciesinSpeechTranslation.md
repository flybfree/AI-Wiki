---
title: The Role of Disfluencies in Speech Translation
published: 2026-08-03T12:26:39Z
authors: Maike Züfle, Maria Teleki, Fabian Retkowski, Vilém Zouhar, Oliver Grabner, Alexander Waibel, James Caverlee, Jan Niehues
url: http://arxiv.org/abs/2608.02138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Role of Disfluencies in Speech Translation

## Abstract
Current speech translation systems, including SpeechLLMs, are trained on cleaned text and tend to strip disfluencies like filled pauses and false starts rather than translate them. We show this comes at a cost: disfluencies carry meaning that gets lost when speech is cleaned up. To study this systematically, we introduce Uh-Mazing, a benchmark of human-translated, disfluency-annotated Switchboard speech covering English into eight target languages. Across these languages and several architectures, we find that false starts and self-repairs, not filled pauses or discourse markers, drive most of the translation-quality loss, and that models which fail to preserve a disfluency tend to omit it rather than mistranslate it. We show inference-time decoding can mitigate this without retraining, and release the benchmark and code.

## Metadata
- **Published**: 2026-08-03T12:26:39Z
- **Authors**: Maike Züfle, Maria Teleki, Fabian Retkowski, Vilém Zouhar, Oliver Grabner, Alexander Waibel, James Caverlee, Jan Niehues
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02138v1)