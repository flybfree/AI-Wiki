---
title: NemotronLabs VoiceChat: An Open Full-duplex Speech-to-Speech Model with Tool Calling Capabilities
published: 2026-09-18T16:27:22Z
authors: Jagadeesh Balam, Travis Bartley, Edresson Casanova, Sanjay Chauhan, Chen Chen, Zhehuai Chen, Zijia Chen, Francesco Ciannella, Slyne Deng, Mikyas Desta, Harishchandra Dubey, Slim Essid, Nourchene Ferchichi, Boris Ginsburg, Mariana Graterol Fuenmayor, Negar Habibi, Kevin Hu, Anand Joseph, Viraj Karandikar, Myungjong Kim, Viacheslav Klimkov, Seelan Lakshmi Narasimhan, Lily Lee, Jason Li, Eileen Long, Ameya Mahabaleshwarkar, Aditya Malte, Adi Margolin, Sasha Meister, Valentin Mendelev, Oluwatobi Olabiyi, Ankita Pasad, Yifan Peng, Elena Rastorgueva, Jayda Ritchie, Jason Roche, Nikhil Srihari, Yuanhang Su, Yoshi Suhara, Viet Anh Trinh, Jinhan Wang, Piotr Zelasko, Hui Wang, Puhui Meng, Chaosen Zhang, Yunsheng Liu, Shawn Wang, Wenjing Li, Zhonglei He
url: http://arxiv.org/abs/2609.21967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NemotronLabs VoiceChat: An Open Full-duplex Speech-to-Speech Model with Tool Calling Capabilities

## Abstract
We introduce NemotronLabs VoiceChat, an open full-duplex speech-to-speech model with native tool-calling capabilities. NemotronLabs VoiceChat combines a streaming speech encoder and decoder-only language model with parallel specialized output streams for agent text and structured function calls, an auxiliary RNN-T branch for incremental user transcription, and a streaming TTS decoder. This design enables the model to listen, transcribe, reason, invoke tools, and speak within a unified streaming architecture while preserving the temporal behavior required for natural conversation. On Full-Duplex-Bench 1.0, NemotronLabs VoiceChat achieves the lowest pause-handling takeover rates among evaluated open-weight systems, 100\% takeover following user interruptions, and a 4.33/5 post-interruption response-quality score. On Full-Duplex-Bench 1.5, it resumes its response after user backchannels in 93\% of cases. NemotronLabs VoiceChat obtains a 55.1 normalized average on VoiceBench and, on Full-Duplex-Bench 3.0 (FDB 3.0), achieves 82.5\% tool-selection F1, while argument accuracy and end-to-end tool execution remain areas for improvement. These results demonstrate that full-duplex interaction, speech recognition and generation, general language capabilities, and external tool use can be integrated in a single open speech-to-speech model without sacrificing real-time conversational behavior.

## Metadata
- **Published**: 2026-09-18T16:27:22Z
- **Authors**: Jagadeesh Balam, Travis Bartley, Edresson Casanova, Sanjay Chauhan, Chen Chen, Zhehuai Chen, Zijia Chen, Francesco Ciannella, Slyne Deng, Mikyas Desta, Harishchandra Dubey, Slim Essid, Nourchene Ferchichi, Boris Ginsburg, Mariana Graterol Fuenmayor, Negar Habibi, Kevin Hu, Anand Joseph, Viraj Karandikar, Myungjong Kim, Viacheslav Klimkov, Seelan Lakshmi Narasimhan, Lily Lee, Jason Li, Eileen Long, Ameya Mahabaleshwarkar, Aditya Malte, Adi Margolin, Sasha Meister, Valentin Mendelev, Oluwatobi Olabiyi, Ankita Pasad, Yifan Peng, Elena Rastorgueva, Jayda Ritchie, Jason Roche, Nikhil Srihari, Yuanhang Su, Yoshi Suhara, Viet Anh Trinh, Jinhan Wang, Piotr Zelasko, Hui Wang, Puhui Meng, Chaosen Zhang, Yunsheng Liu, Shawn Wang, Wenjing Li, Zhonglei He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21967v1)