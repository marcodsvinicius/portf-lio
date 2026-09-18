import os
import sys

files_to_check = [
    "scratch/all_certificates_found.txt",
    "scratch/extracted_courses.txt",
    "scratch/extracted_individual_clean.txt",
    "scratch/found_courses_output.txt",
    "scratch/full_original_courses.txt",
    "scratch/original_noloco_layout.txt"
]

output_log = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\txt_files_summary.txt"

with open(output_log, "w", encoding="utf-8") as out_f:
    for filepath in files_to_check:
        abs_path = os.path.join(r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio", filepath)
        if os.path.exists(abs_path):
            size = os.path.getsize(abs_path)
            out_f.write(f"File: {filepath}, Size: {size} bytes\n")
            with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read(2500) # read more characters
                out_f.write("--- FIRST 2500 CHARS ---\n")
                out_f.write(content)
                out_f.write("\n" + "="*80 + "\n\n")
        else:
            out_f.write(f"File: {filepath} does not exist\n\n")

print("Successfully wrote summary to", output_log)
