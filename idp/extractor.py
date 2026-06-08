"""Intelligent document processor."""
from google.cloud import documentai
from typing import Dict, List
import json, re

class IntelligentDocumentProcessor:
    def __init__(self, project_id: str, processor_id: str, location: str = "us"):
        self.client = documentai.DocumentProcessorServiceClient()
        self.processor_name = self.client.processor_path(project_id, location, processor_id)

    def process_document(self, content: bytes, mime_type: str = "application/pdf") -> Dict:
        request = documentai.ProcessRequest(name=self.processor_name,
            raw_document=documentai.RawDocument(content=content, mime_type=mime_type))
        result = self.client.process_document(request=request)
        doc = result.document
        extracted = {"text": doc.text, "pages": len(doc.pages), "entities": [], "tables": []}
        for entity in doc.entities:
            extracted["entities"].append({"type": entity.type_, "value": entity.mention_text,
                "confidence": entity.confidence, "normalized": entity.normalized_value.text if entity.normalized_value else None})
        for page in doc.pages:
            for table in page.tables:
                rows = [[cell.layout.text_anchor.text_segments[0].start_index
                         if cell.layout.text_anchor.text_segments else ""
                         for cell in row.cells] for row in table.header_rows + table.body_rows]
                extracted["tables"].append({"rows": rows})
        return extracted

    def validate_cnpj(self, cnpj: str) -> bool:
        cnpj = re.sub(r"[./-]", "", cnpj)
        if len(cnpj) != 14 or cnpj == cnpj[0] * 14: return False
        def calc_digit(cnpj, weights):
            s = sum(int(d) * w for d, w in zip(cnpj, weights))
            r = s % 11
            return 0 if r < 2 else 11 - r
        w1 = [5,4,3,2,9,8,7,6,5,4,3,2]; w2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        return int(cnpj[12]) == calc_digit(cnpj, w1) and int(cnpj[13]) == calc_digit(cnpj, w2)
