from financy.config import Config
from financy.azure_form.pdf import AnalyzePDF
from financy.open_ai.jsonl import write_entry, Entry


def extract_data(pdf_url: str):
    c = Config()
    pdf = AnalyzePDF(c.azure_form_endpoint, c.azure_form_key)
    
    print(f'Extracting data from PDF from {pdf_url}...')
    pdf.analyze(pdf_url)

    contact_data = pdf.get_contact_table_data()
    living_duration = pdf.get_selected_living_duration()
    loan_usage = pdf.get_selected_loan_usage()
    loan_decision = pdf.get_loan_decision()

    prompt = ""
    for key, value in contact_data.items():
        prompt += f"{key}: {value}\n"

    prompt += f"Living duration: {living_duration}\n"
    prompt += f"Loan usage: {loan_usage}\n"

    write_entry(Entry(prompt, loan_decision))
    print("Extraction complete!")