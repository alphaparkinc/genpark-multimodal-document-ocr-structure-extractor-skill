from client import MultimodalDocumentOcrStructureExtractorClient

def main():
    client = MultimodalDocumentOcrStructureExtractorClient()
    res = client.extract_document("financial_report_2026.pdf", True)
    print(f"OCR Accuracy: {res['ocr_accuracy_pct']}%")
    print("Extracted Table JSON:", res["extracted_tables_json"])

if __name__ == "__main__":
    main()
