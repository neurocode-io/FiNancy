from financy.config import Config
from financy.azure_form.pdf import AnalyzePDF
from financy.open_ai.completion import completion
from financy.azure_form.pdf import AnalyzePDF


def analyze(applicant_file: str):
    c = Config()
    pdf = AnalyzePDF(c.azure_form_endpoint, c.azure_form_key)
    
    print(f'Extracting data from PDF from {applicant_file}...')
    pdf.analyze(applicant_file)

    contact_data = pdf.get_contact_table_data()
    living_duration = pdf.get_selected_living_duration()
    loan_usage = pdf.get_selected_loan_usage()

    prompt = ""
    for key, value in contact_data.items():
        prompt += f"{key}: {value}\n"

    prompt += f"Living duration: {living_duration}\n"
    prompt += f"Loan usage: {loan_usage}\n"

    completion = completion(prompt)

    print(completion)