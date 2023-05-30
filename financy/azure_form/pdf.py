from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient, AnalyzeResult

class AnalyzePDF:
    result: AnalyzeResult
    client: DocumentAnalysisClient

    def __init__(self, endpoint, key):
        self.client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    
    def get_loan_decision(self):
        for page in self.result.pages:
            for line in page.lines:
                if "Decision:" in line.content:
                    return line.content.split(":")[1]

    def get_selected_loan_usage(self):
        categories = ["business launching", "home improvement", "education", "house buying", "investment", "other"]
        if len(self.result.pages) < 1:
            raise Exception("Invalid input")

        first_page = self.result.pages[0]
        for i, selection_mark in enumerate(first_page.selection_marks):
            if selection_mark.state == "selected":
                return categories[i]

        return None

    def get_selected_living_duration(self):
        categories = ["0-1", "1-2", "3-4", "5+"]
        if len(self.result.pages) < 2:
            raise Exception("Invalid input")

        second_page = self.result.pages[1]     
        for i, selection_mark in enumerate(second_page.selection_marks):
            if selection_mark.state == "selected":
                return categories[i]

        return None

    def get_contact_table_data(self):
        cells_dict = {}
        for table in self.result.tables:
            cells = table.cells
            for i in range(0, len(cells), 2):
                key_cell = cells[i]
                value_cell = cells[i+1] if (i+1) < len(cells) else None
                if value_cell is not None:
                    cells_dict[key_cell.content] = value_cell.content

        return cells_dict

    def analyze(self, document_url):
        poller = self.client.begin_analyze_document_from_url("prebuilt-layout", document_url)
        self.result = poller.result()
