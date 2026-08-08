class MultimodalDocumentOcrStructureExtractorClient:
    def extract_document(self, document_file_path: str, extract_tables: bool = True) -> dict:
        return {
            "structured_markdown": "# Financial Statement 2026\n| Quarter | Revenue |\n| Q1 | $1.2M |\n",
            "extracted_tables_json": [{"quarter": "Q1", "revenue": "$1.2M"}],
            "ocr_accuracy_pct": 99.4
        }
