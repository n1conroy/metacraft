# MetaCraft Pro

MetaCraft Pro is an agentic schema and metadata generation system designed for libraries. It supports public, academic, and research libraries by generating structured metadata schemas from plain language collection or program goals. The system leverages large language models (LLMs), natural language processing (spaCy), and transparent rule-based logic to translate prompts into BigQuery schemas, JSON schema, or ElasticSearch mappings.

MetaCraft Pro is part of a broader suite of open tools supporting library-facing use of AI and agents for metadata, discovery, digital collections, and community information work.

## Purpose

Libraries are increasingly tasked with collecting and managing non-traditional digital content, such as social media commentary, community stories, public engagement data, and born-digital zines, podcasts, or videos. These materials often lack predefined metadata standards or require custom schemas that support local or civic priorities.

MetaCraft Pro addresses this challenge by enabling librarians and information professionals to define metadata schemas using natural language, reducing technical barriers while preserving transparency and interoperability.

## Example Use Case

Prompt:

Collect and organize recent tweets and news articles on Indigenous water stewardship for public library education materials.

Generated Schema Output:

```json
[
  {"name": "id", "type": "STRING"},
  {"name": "timestamp", "type": "STRING"},
  {"name": "source_platform", "type": "STRING"},
  {"name": "author", "type": "STRING"},
  {"name": "region", "type": "STRING"},
  {"name": "theme", "type": "STRING"},
  {"name": "intended_audience", "type": "STRING"}
]
```

The schema can be exported in formats compatible with BigQuery, JSON Schema, or ElasticSearch.

## Features

- Plain-language input describing data collection needs
- OpenAI or Claude-powered LLM processing (user configurable)
- Named entity and keyword validation using spaCy
- Schema post-processing with required field injection and metadata normalization
- Configurable output to JSON Schema, BigQuery, or ElasticSearch mappings
- Transparent agentic decision logging
- Library-focused vocabulary enrichment
- Modular and extensible Python architecture
- Optional GCP integrations (BigQuery schema loader, logging)

## Installation

```bash
git clone https://github.com/n1conroy/metacraft.git
cd metacraft
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
```

You will be prompted to enter your API key and a natural language request. The resulting schema will be printed and optionally saved.

## Use Cases

| Context | Prompt | Output Fields |
|--------|--------|---------------|
| Community Programming | Collect Instagram feedback about youth-led library events | user_id, event_name, comment_text, sentiment, timestamp |
| Special Collections | Metadata for a digital exhibit of housing justice zines from the 1980s | title, author, publication_date, theme, region, format |
| Civic Data | Collect public Facebook comments about accessibility in local parks | source_platform, location, issue_type, sentiment, suggestion |

## Roadmap

MetaCraft Pro is the first tool in an ongoing development of LLM-based, agent-driven library utilities. Additional modules in progress:

- PromptForge: authoring and cataloguing reusable prompts for teaching, reference, and metadata
- QueryTuner: translating librarian reference queries to ElasticSearch, SQL, or linked data
- AgentAtlas: visualization of agent workflows, decisions, and schema traceability
- StackTrace: hybrid discovery interface combining LLMs with local knowledge sources and open APIs

## Collaboration

This project welcomes collaboration from library and information professionals. Contributions may include:

- Vocabulary enrichment (Dublin Core, schema.org, LCSH mappings)
- Metadata mapping (to MARC, MODS, RDF)
- Platform integration (Omeka, Islandora, ArchivesSpace)
- Pilot use cases and applied workshops

To contribute or collaborate, please contact nadia.k.conroy@gmail.com or open a GitHub issue.

## About

Developer: Nadia Conroy, PhD, MLIS  
Background: Information science researcher, former staff at Toronto Public Library, 8 years in machine learning and data architecture.

MetaCraft Pro was developed to support public and research libraries as they navigate the adoption of LLMs and autonomous agents. It is built to provide transparency, agency, and interoperability in AI-supported metadata workflows.

Repository: https://github.com/n1conroy/metacraft  
License: MIT (or TBD)
