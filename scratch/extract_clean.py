import os
import re

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")

courses_to_find = [
    ("Fundamentos de Comunicação", "Fundamentos de Comunica"),
    ("Big Data e Inteligência Artificial", "Big Data"),
    ("IA Generativa para Profissionais Criativos", "IA Generativa para Profissionais"),
    ("Liderança com Inovação", "Lideran"),
    ("Introdução à Inteligência Artificial", "Introdu"),
    ("Fundamentos de Agentes de IA", "Agentes de IA"),
    ("Prompt Engineering", "Prompt Engineering"),
    ("Fundamentos da Inteligência Artificial Generativa", "Fundamentos da Intelig\u00eancia Artificial Generativa"),
    ("Salesforce Platform", "Salesforce"),
    ("Noloco Certified Expert", "Noloco"),
    ("Planejamento e Gestão Ágil", "Planejamento e Gest"),
    ("Design System Specialist", "Design System Specialist"),
    ("Figma Avançado", "Figma Avan"),
    ("UX/UI Design", "UX/UI Design")
]

results = {}
if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            for course_name, key in courses_to_find:
                if course_name in results:
                    continue
                if key in line and ("Visualizar Certificado" in line or "Visualizar" in line):
                    # Let's search for a div pattern
                    idx = line.find(key)
                    # Search backwards for '<div' or '<!-- Certificado'
                    start = max(0, idx - 800)
                    chunk = line[start:idx+1200]
                    
                    # Clean up backslashes and json escapes
                    chunk_clean = chunk.replace('\\"', '"').replace('\\n', '\n').replace('\\/', '/')
                    
                    # Find last '<div class="group">' before the course name
                    div_match = list(re.finditer(r'<div class="group">', chunk_clean))
                    if div_match:
                        start_pos = div_match[-1].start()
                        end_div = chunk_clean.find('</div>', start_pos)
                        if end_div != -1:
                            results[course_name] = chunk_clean[start_pos:end_div+6]

# Let's write the results to a python file or txt file so we have them clean
output_file = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\extracted_individual_clean.txt"
with open(output_file, "w", encoding="utf-8") as out:
    for course_name, html in results.items():
        out.write(f"=== {course_name} ===\n")
        out.write(html)
        out.write("\n\n")

print(f"Extracted {len(results)} clean courses to scratch/extracted_individual_clean.txt")
