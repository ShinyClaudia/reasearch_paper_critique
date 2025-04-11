---
title: Research Paper Critique Generator
emoji: 📚
colorFrom: indigo
colorTo: purple
sdk: streamlit
sdk_version: 1.44.1
app_file: app.py
pinned: true
---

<p align="center">
  <img src="https://huggingface.co/spaces/your-username/research-critique-app/resolve/main/assets/banner.png" width="80%" alt="Research Critique Generator Banner"/>
</p>

<h1 align="center">Research Paper Critique Generator</h1>

<p align="center"><b>Summarize. Critique. Improve.</b></p>

<p align="center">
  An AI-based app that analyzes academic papers and provides intelligent feedback with section-wise summaries, research gaps, and suggestions for improvement — all without requiring API keys.
</p>

---

## 🚀 Features

- **PDF Upload**: Drag and drop research papers in `.pdf` format.
- **Section Detection**: Automatically identifies Abstract, Introduction, Methods, Results, and Conclusion.
- **Local Summarization**: Uses Hugging Face's `distilbart-cnn-12-6` model (no OpenAI keys needed).
- **Critique Generator**: Provides research gap detection and improvement tips via built-in templates.
- **Clean UI**: Minimal, elegant, and fast — built with Streamlit.

---

## 📸 Interface Preview

<p align="center">
  <img src="https://huggingface.co/spaces/your-username/research-critique-app/resolve/main/assets/interface_preview.png" width="85%" alt="App Screenshot">
</p>

---

## 🧠 How It Works

```mermaid
graph LR
A[Upload PDF] --> B[Extract Text]
B --> C[Detect Sections]
C --> D[Summarize Each Section]
D --> E[Generate Critique]
E --> F[Display Results]

git add README.md
git commit -m "Update README for Hugging Face"
git push

<img src="https://huggingface.co/spaces/your-username/project/resolve/main/assets/banner.png">
