# 🛡️ AI Guardrail

> **The Firewall for Large Language Models (LLMs)**

**AI Guardrail** is a lightweight, CLI-based security tool designed to detect **Prompt Injection** attacks before they reach your AI model. It acts as a defense layer, analyzing incoming prompts for malicious signatures and heuristic anomalies.

## ⚡ Features
- **Signature Detection:** Blocks known jailbreaks (e.g., "DAN Mode", "System Override").
- **Heuristic Analysis:** Detects buffer overflow attempts via length analysis.
- **Red Team Logging:** Color-coded terminal output for security auditing.
- **Zero Latency:** Runs 100% locally with no API dependencies.

## 📦 Installation

### Option 1: Install System-Wide (Recommended)
This allows you to run the `guardrail` command from anywhere in your terminal.

```bash
git clone [https://github.com/krinathakkar646/ai-guardrail.git](https://github.com/krinathakkar646/ai-guardrail.git)
cd ai-guardrail
pip install .
