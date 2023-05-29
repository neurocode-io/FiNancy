from financy.config import Config
from financy.train.analyze_pdf import AnalyzePDF

c = Config()


pdf = AnalyzePDF(c.azure_form_endpoint, c.azure_form_key)
pdf.analyze("")
