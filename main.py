from financy.config import Config
from financy.train.analyze_pdf import AnalyzePDF

c = Config()


pdf = AnalyzePDF(c.azure_form_endpoint, c.azure_form_key)
pdf.analyze("https://neurocode-io.github.io/FiNancy/financy/data/001.pdf")
contact_data = pdf.get_contact_table_data()
living_duration = pdf.get_selected_living_duration()
loan_usage = pdf.get_selected_loan_usage()
loan_decision = pdf.get_loan_decision()

for key, value in contact_data.items():
    print(f"{key}: {value}")

print(f"Living duration: {living_duration}")
print(f"Loan usage: {loan_usage}")
print(f"Loan decision: {loan_decision}")