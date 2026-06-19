---
title: "Open Notebook — Open Source Notebook LM Alternative"
date: 2026-06-13
source: "GitHub"
url: "https://github.com/lfnovo/open-notebook"
tags: [notebook-lm, open-source, self-hosted, podcast-generation, multimodal, ai-tools]
---

## Summary

Placeholder summary — please add a concise summary of this article.


# Open Notebook — Open Source Notebook LM Alternative



**Source**: [Original Article](https://github.com/lfnovo/open-notebook)
**Source**: [Original Repo](https://github.com/lfnovo/open-notebook)

## Overview

Open Notebook is a privacy-focused, self-hosted alternative to Google's Notebook LM. It provides research, content organization, and AI-powered media generation with full data sovereignty.

## Key Features

### Core Capabilities
- **Privacy-First**: Self-hosted, zero cloud dependencies, complete data control
- **Multi-Model AI**: Supports 18+ providers (OpenAI, Anthropic, Ollama, Google, Azure, Mistral, etc.)
- **Universal Content**: PDFs, videos, audio, web pages, Office docs
- **Professional Podcasts**: 1-4 speakers with custom profiles and full script control
- **Intelligent Search**: Full-text and vector search across all content
- **Context-Aware Chat**: AI conversations powered by your research materials
- **Multi-Language UI**: EN, PT, ZH, JA, RU, BN

### Advanced Capabilities
- **Reasoning Model Support**: DeepSeek-R1, Qwen3, and other thinking models
- **Content Transformations**: Customizable summarization and insight extraction
- **Full REST API**: Programmatic access for custom integrations and automation
- **Security**: Optional password protection, fine-grained context control, source citations

## Open Notebook vs. Google Notebook LM

| Feature | Open Notebook | Google Notebook LM |
|---|---|---|
| **Privacy & Control** | Self-hosted, your data | Google cloud only |
| **AI Provider Choice** | 18+ providers | Google models only |
| **Podcast Speakers** | 1-4 speakers w/ custom profiles | 2 speakers only |
| **Content Transformations** | Custom & built-in | Limited options |
| **API Access** | Full REST API | No API |
| **Deployment** | Docker, cloud, or local | Google hosted only |
| **Citations** | Basic references (improving) | Comprehensive w/ sources |
| **Customization** | Open source, fully customizable | Closed system |
| **Cost** | Pay only for AI usage | Free tier + subscription |

## Supported AI Providers

Powered by the [Esperanto](https://github.com/lfnovo/esperanto) library. Supports LLM, Embedding, STT, and TTS across 18+ providers:

- **Full Suite (LLM + Embedding + STT + TTS)**: OpenAI, Google GenAI, Azure OpenAI, Mistral, OpenAI Compatible (LM Studio, etc.)
- **LLM + Embedding**: Vertex AI, Ollama, OpenRouter, Voyage
- **LLM + STT**: Groq
- **LLM + TTS**: xAI, Deepgram, ElevenLabs
- **LLM Only**: Anthropic, Perplexity, DeepSeek, DashScope (Qwen), MiniMax

## Quick Start

### Prerequisites
- Docker Desktop installed
- API keys configured later in the UI

### docker-compose.yml

```yaml
services:
  surrealdb:
    image: surrealdb/surrealdb:v2
    command: start --log info --user root --pass root rocksdb:/mydata/mydatabase.db
    user: root
    ports:
      - "8000:8000"
    volumes:
      - ./surreal_data:/mydata
    restart: always

  open_notebook:
    image: lfnovo/open_notebook:v1-latest
    ports:
      - "8502:8502"
      - "5055:5055"
    environment:
      - OPEN_NOTEBOOK_ENCRYPTION_KEY=change-me-to-a-secret-string
      - SURREAL_URL=ws://surrealdb:8000/rpc
      - SURREAL_USER=root
      - SURREAL_PASSWORD=root
      - SURREAL_NAMESPACE=open_notebook
      - SURREAL_DATABASE=open_notebook
    volumes:
      - ./notebook_data:/app/data
    depends_on:
      - surrealdb
    restart: always
```

Start with `docker compose up -d`, then access **http://localhost:8502**.

## Roadmap
- **Upcoming**: Live Front-End Updates, Async Processing, Cross-Notebook Sources, Bookmark Integration
- **Recently Completed**: Next.js Frontend, Comprehensive RAG pipeline
