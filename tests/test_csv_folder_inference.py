import sys
sys.path.append("../src")


from csv_schema_infer.csv_folder_inference import CsvFolderInference

if __name__ == "__main__":
    folder_path = './data/cricket'
    output_file_path = './output/cricket.json'

    folder_inferer = CsvFolderInference(folder_path, output_file_path, max_rows=10000)
    folder_inferer.perform_inference()


    folder_path = './data/sales'
    output_file_path = './output/sales.json'

    folder_inferer = CsvFolderInference(folder_path, output_file_path, max_rows=10000)
    folder_inferer.perform_inference()
