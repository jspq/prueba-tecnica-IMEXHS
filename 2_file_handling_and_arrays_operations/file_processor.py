import os
import logging
import time #revisar si es la dependencia correcta
import pandas as pd
import numpy as np
import pydicom
from pydicom.data import get_testdata_file
from PIL import Image
from typing import Optional, List, Tuple

class FileProcessor:
    def __init__(self, base_path: str, log_file: str):
        self.base_path = base_path
        self.logger = logging.getLogger("FileProcessor")
        self.logger.setLevel(logging.ERROR)
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def list_folder_contents(self, folder_name: str, details: bool = False) -> None:
        folder_path = os.path.join(self.base_path, folder_name)
        try:
            if not os.path.exists(folder_path):
                raise FileNotFoundError(f"Folder not found: {folder_path}")

            items = os.listdir(folder_path)
            print(f"Folder: {folder_path}")
            print(f"Number of elements: {len(items)}")

            for item in items:
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    info = f"- {item} (Folder)"
                    if details:
                        last_modified = os.path.getmtime(item_path)
                        info += f", Last Modified: {time.ctime(last_modified)}"
                else:
                    info = f"- {item} (File)"
                    if details:
                        size = os.path.getsize(item_path) / (1024 * 1024)
                        last_modified = os.path.getmtime(item_path)
                        info += f" ({size:.2f} MB, Last Modified: {time.ctime(last_modified)})"
                print(info)
        except Exception as e:
            self.logger.error(f"Error listing folder contents: {e}")

    def read_csv(self, filename: str, report_path: Optional[str] = None, summary: bool = False) -> None:
        file_path = os.path.join(self.base_path, filename)
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"CSV file not found: {file_path}")

            data = pd.read_csv(file_path)
            print(f"CSV Analysis: ")
            print(f"Columns: {list(data.columns)}")
            print(f"Rows: {len(data)}")

            numeric_cols = data.select_dtypes(include=[np.number]).columns
            for col in numeric_cols:
                mean = data[col].mean()
                std_dev = data[col].std()
                print(f"- {col}: Average = {mean:.2f}, Std Dev = {std_dev:.2f}")

            if summary:
                non_numeric_cols = data.select_dtypes(exclude=[np.number]).columns
                for col in non_numeric_cols:
                    unique_values = data[col].value_counts()
                    print(f"- {col}: Unique Values = {len(unique_values)}")
                    print(unique_values)

            if report_path:
                os.makedirs(report_path, exist_ok=True)
                report_file = os.path.join(report_path, f"{os.path.splitext(filename)[0]}_report.txt")
                with open(report_file, 'w') as f:
                    for col in numeric_cols:
                        mean = data[col].mean()
                        std_dev = data[col].std()
                        f.write(f"- {col}: Average = {mean:.2f}, Std Dev = {std_dev:.2f}\n")
                print(f"Saved summary report to {report_file}")

        except Exception as e:
            self.logger.error(f"Error reading CSV file: {e}")

    def read_dicom(self, filename: str, tags: Optional[List[Tuple[int, int]]] = None, extract_image: bool = False) -> None:
        file_path = os.path.join(self.base_path, filename)
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"DICOM file not found: {file_path}")

            dicom_data = pydicom.dcmread(file_path)
            print(f"Patient Name: {dicom_data.get('PatientName', 'Unknown')}")
            print(f"Study Date: {dicom_data.get('StudyDate', 'Unknown')}")
            print(f"Modality: {dicom_data.get('Modality', 'Unknown')}")

            if tags:
                for tag in tags:
                    value = dicom_data.get(tag, 'Not Found')
                    print(f"Tag {tag}: {value}")

            if extract_image and hasattr(dicom_data, 'pixel_array'):
                image = Image.fromarray(dicom_data.pixel_array)
                output_path = os.path.join(self.base_path, f"{os.path.splitext(filename)[0]}.png")
                image.save(output_path)
                print(f"Extracted image saved to {output_path}")

        except Exception as e:
            self.logger.error(f"Error reading DICOM file: {e}")