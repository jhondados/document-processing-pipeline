# 📑 Intelligent Document Processing Pipeline

[![Volume](https://img.shields.io/badge/Volume-1M%2B%20docs%2Fday-blue)](.) [![Accuracy](https://img.shields.io/badge/Table%20Detection-96.4%25-green)](.) [![Languages](https://img.shields.io/badge/OCR%20Languages-23-orange)](.)

> Enterprise IDP processing **1M+ documents/day** across 23 languages. Table detection with TATR (96.4%), form field extraction, CNPJ/CPF validation and structured JSON output for downstream systems.

## 📄 Document Types Supported
- Brazilian bank statements, boletos, notas fiscais (NF-e)
- Contracts, petitions, court documents (Portuguese legal)
- Medical records, TISS XML, SADT forms
- International: invoices, purchase orders, shipping documents

## 🏗️ Processing Pipeline
```
Document → Pre-processing (deskew, denoise) → OCR (23 languages)
        → Layout Analysis (tables, forms, text) → Structure Extraction
        → Entity Recognition (NER: dates, values, parties)
        → Validation (business rules) → JSON output
```
