import sys
sys.path.append("../src")

from csv_schema_infer.csv_schema_inference import CsvSchemaInference
from csv_schema_infer.csv_delimiter_detector import CsvDelimiterDetector

if __name__ == "__main__":
    csv_file_path = './data/sales/fast_food_sales.csv'

    delim_detector = CsvDelimiterDetector(csv_file_path, 100)
    delimiter = delim_detector.detect_delimiter()

    print(f"Detected delimiter: '{delimiter}'")

    type_detector = CsvSchemaInference(delimiter, csv_file_path, 1000000)
    type_detector.infer_schema()
    type_detector.build_metadata()
