import argparse
from financy.commands.extract_data import extract_data
from financy.commands.train import train
from financy.commands.analyze import analyze


parser = argparse.ArgumentParser(prog='FiNancy', description='An AI-powered loan applicant screening bot')
subparsers = parser.add_subparsers(dest='command')

extract_parser = subparsers.add_parser('extract', help='extract data from a loan application')
train_parser = subparsers.add_parser('train', help='train the model')
analyze_parser = subparsers.add_parser('analyze', help='analyze a loan application')

extract_parser.add_argument('pdf_url', type=str, help='A public url to the PDF to extract data from')
analyze_parser.add_argument('application_file', type=str, help='The path to the PDF loan application')
train_parser.add_argument('data_path', type=str, help='The path to the JSONL training data')
train_parser.add_argument('base_model', type=str, default="ada", help='The base model to fine-tune')

args = parser.parse_args()

if args.command == 'analyze':
    analyze(args.application_file)

elif args.command == 'train':
    train(args.data_path, args.base_model)

elif args.command == 'extract':
    # "https://neurocode-io.github.io/FiNancy/financy/data/001.pdf"
    extract_data(args.pdf_url)
