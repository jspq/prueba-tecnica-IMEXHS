from file_processor import FileProcessor

def main():
    base_path = "./resources/files"
    log_file = "./resources/logs/errors.log"

    processor = FileProcessor(base_path, log_file)

    processor.list_folder_contents("", details=True)

    processor.read_csv("sample-02-csv.csv", report_path="./resources/reports_csv", summary=True)

    processor.read_dicom("sample-02-dicom.dcm", tags=[(0x0010, 0x0010)], extract_image=True)

    processor.read_dicom("sample-02-dicom-2.dcm", tags=[(0x0010, 0x0010)], extract_image=True)

if __name__ == "__main__":
    main()