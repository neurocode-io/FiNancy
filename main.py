from financy.config import Config
from financy.train.analyze_pdf import AnalyzePDF
from financy.train.jsonl import write_entry, Entry

c = Config()

pdf = AnalyzePDF(c.azure_form_endpoint, c.azure_form_key)
pdf.analyze("https://neurocode-io.github.io/FiNancy/financy/data/001.pdf")
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