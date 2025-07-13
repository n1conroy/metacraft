# 📚 MetaCraft Pro

**An Agentic Metadata & Schema Generator for Libraries**

MetaCraft Pro is a production-grade tool designed for public, academic, and research libraries navigating the challenges and opportunities of the LLM era. Using natural language prompts, it generates metadata schemas and data architecture plans tailored to educational, cultural, or civic use cases.

Built on modern AI tools like OpenAI, Claude, and spaCy, MetaCraft Pro helps libraries go from ambiguous data collection goals to clear, structured, machine-readable metadata — no engineering team required.

---

## 🎯 Who It's For

- **Public Libraries** managing community data, feedback, or program outcomes  
- **Digital Humanities Teams** designing collections, exhibits, or cultural datasets  
- **Library Data Architects** building cross-platform metadata plans  
- **Archivists & Special Collections** curating content across social or digital platforms  
- **Information Professionals** exploring AI-integrated workflows

---

## 🧠 What It Does

> ✍️ _"Schema for collecting TikTok posts about youth mental health for teen outreach programs."_  
>  
> ⛏️ MetaCraft Pro parses the prompt → engages an LLM → extracts domain-specific terms → maps to structured metadata fields → outputs a clean JSON or BigQuery schema.

### Core Pipeline

1. **User Prompt** → Describe data collection need in plain language
2. **Agentic Coordination** → Orchestrates spaCy, LLM, rules
3. **LLM Schema Synthesis** → Asks OpenAI / Claude for schema field suggestions
4. **spaCy NLP Layer** → Validates with entity and noun-phrase extraction
5. **Rule-based Enhancer** → Enforces defaults like `id`, `timestamp`, `privacy_flags`
6. **Export** → Outputs valid schema in BigQuery or JSON Schema format

---

## ✅ Features

- 🔄 Multi-provider LLM support: OpenAI, Claude, or local mock  
- 📚 Library-specific schema enrichment (education, civic, GLAM-focused)  
- 🧠 spaCy-assisted keyword validation  
- 📊 Exports BigQuery, JSON Schema, or Elastic mappings  
- 🔍 Transparent decision log of how fields were chosen  
- 💾 Save + version schema definitions locally  
- 🧪 Unit-tested core logic for reliability  
- 🧩 Extensible: plug in your own logic or metadata templates  
- ☁️ Optional GCP integrations (BigQuery, Cloud Logging)

---

## 🧭 Example Use Cases

| Use Case | Prompt | Output |
|----------|--------|--------|
| Youth Programs | _“Collect feedback from Instagram stories about teen library events”_ | Fields: `user_id`, `story_text`, `event_hashtag`, `feedback_rating`, `sentiment_score` |
| Accessibility | _“Schema for cataloging community stories about accessibility challenges”_ | Fields: `narrator`, `location`, `barrier_type`, `resolution`, `timestamp` |
| Collection Design | _“Metadata for a digital collection of activist zines about housing justice”_ | Fields: `title`, `creator`, `theme_tags`, `location`, `publication_year`, `license_type` |

---

## 🏗️ Installation

```bash
git clone https://github.com/yourname/metacraft-pro.git
cd metacraft-pro
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
