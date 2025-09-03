import csv
import openpyxl
import PyPDF2

def process_file(file_obj):
    """Parse uploaded file depending on its type"""
    file_obj.status = "processing"
    file_obj.progress = 50
    file_obj.save()

    try:
        parsed_data = []

        # CSV
        if file_obj.file.name.endswith(".csv"):
            with open(file_obj.file.path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    parsed_data.append(row)

        # XLSX
        elif file_obj.file.name.endswith(".xlsx"):
            wb = openpyxl.load_workbook(file_obj.file.path)
            sheet = wb.active
            for row in sheet.iter_rows(values_only=True):
                parsed_data.append(row)

        # TXT
        elif file_obj.file.name.endswith(".txt"):
            with open(file_obj.file.path, "r", encoding="utf-8") as f:
                parsed_data = f.readlines()

        # PDF
        elif file_obj.file.name.endswith(".pdf"):
            with open(file_obj.file.path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    parsed_data.append(page.extract_text())

        else:
            parsed_data.append({"message": "Unsupported file type"})

        file_obj.parsed_content = parsed_data
        file_obj.status = "ready"
        file_obj.progress = 100
        file_obj.save()

    except Exception as e:
        file_obj.status = "failed"
        file_obj.parsed_content = [{"error": str(e)}]
        file_obj.save()
