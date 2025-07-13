# 📚 MetaCraft Pro

**An Agentic Metadata & Schema Generator for Libraries**

MetaCraft Pro is a production-grade, agent-powered metadata tool designed for public, academic, and research libraries navigating the evolving role of generative AI and large language models (LLMs). It translates natural language goals into structured metadata schemas for collection development, digital programs, civic feedback, and more.

Using advanced agents built on LLMs, NLP, and transparent rule-based logic, MetaCraft helps library staff define, refine, and deploy metadata frameworks — all with minimal technical intervention.

---

## 🎯 Who It's For

- **Public Libraries** running outreach or digital literacy programs  
- **Academic and Special Collections** managing new media, datasets, or community archives  
- **Library Technologists** building or mapping metadata to digital systems  
- **Archivists** structuring born-digital content  
- **Information Professionals** creating AI-aligned workflows rooted in ethics and context

---

## 🧠 What It Does

> ✍️ _"Collect and organize recent tweets and news articles on Indigenous water stewardship for public library education materials."_

✅ **MetaCraft Pro** interprets this prompt, calls an LLM for domain-specific schema suggestions, enriches results using spaCy NLP and internal logic, and outputs a ready-to-use metadata schema in JSON or BigQuery format.

### Agentic Workflow

1. **Plain-text request**
2. **LLM call (OpenAI or Claude)** to suggest useful fields
3. **spaCy NLP** to extract context-aware keywords
4. **Agent decisions**: required fields (e.g. `id`, `timestamp`, `region`)
5. **Schema output**: ready for BigQuery, Elastic, JSON Schema, or MARC mapping

---

## ✅ Features

- 🤖 OpenAI + Claude support (easily switch between)
- 🧠 spaCy-enhanced field validation
- 📂 Export to BigQuery or JSON Schema
- 🔍 Transparent logging of agent decisions
- ✍️ Local save and versioning of schema files
- 🛡️ Rule-based enhancement (e.g. auto-add source metadata)
- 🔌 Modular and extensible for your ILS, DAM, or archive platform
- 🧪 Built-in unit tests and config layer
- ☁️ GCP-compatible: BigQuery, Cloud Logging ready

---

## 📊 Real Use Case Examples

| Library Task | Example Prompt | Schema Output |
|--------------|----------------|----------------|
| Youth Programming | _"Collect Instagram feedback about teen-led events at the downtown branch."_ | `user_id`, `event_name`, `feedback_text`, `emoji_count`, `sentiment_score` |
| Digital Humanities | _"Metadata for activist zines on housing justice for a university archive."_ | `title`, `creator`, `publication_date`, `theme_tags`, `license`, `location` |
| Civic Participation | _"Schema for cataloging feedback on budget proposals from seniors."_ | `participant_age`, `proposal_id`, `concerns`, `recommendation_type`, `satisfaction_rating` |

---

## 📁 Installation

```bash
git clone https://github.com/yourname/metacraft-pro.git
cd metacraft-pro
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
