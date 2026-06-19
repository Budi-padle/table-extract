class TableExtractor:
    def __init__(self, ocr_engine='tesseract'):
        self.ocr_engine = ocr_engine
    
    def extract(self, pdf_path):
        """Extract tables from PDF file."""
        # TODO: implement table detection
        return []
    
    def to_csv(self, tables, output_path):
        """Export tables to CSV."""
        import csv
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            for table in tables:
                writer.writerows(table)
