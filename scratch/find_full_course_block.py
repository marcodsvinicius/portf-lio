import os
import re

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\pristine_courses.html"

found_blocks = []
if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            # Check if this line contains multiple of our target courses
            if "Fundamentos de Comunicação" in line and "Noloco Certified Expert" in line and "Design System Specialist" in line:
                # Find the block containing Cursos e Especializações
                pos_start = line.find("Cursos e Especializações")
                if pos_start != -1:
                    # Look for the space-y-6 container
                    div_start = line.find('<div class=\\"space-y-6\\"', pos_start)
                    if div_start != -1:
                        # Find where this space-y-6 block ends. 
                        # Since it could be long, let's extract a large chunk and parse it.
                        chunk = line[div_start:div_start+30000]
                        chunk_clean = chunk.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/').replace('\\r', '\r')
                        
                        # Let's count matching opening/closing divs to find the exact end of space-y-6
                        # Or simply find the next major landmark, like Coluna Direita: Experiência Profissional
                        end_landmark = chunk_clean.find("<!-- Coluna Direita")
                        if end_landmark == -1:
                            end_landmark = chunk_clean.find("Experiência Profissional")
                        
                        if end_landmark != -1:
                            # Search backwards from end_landmark to the closing </div> of space-y-6
                            # That is usually right before a </div> or similar.
                            # Let's extract everything from the start up to the landmark and clean it
                            courses_block = chunk_clean[:end_landmark]
                            # Clean up trailing closing divs if necessary so it matches <div class="space-y-6">...</div>
                            # Let's count divs in courses_block
                            open_divs = len(re.findall(r'<div\b', courses_block))
                            close_divs = len(re.findall(r'</div>', courses_block))
                            
                            # We want to match exactly the top-level <div class="space-y-6"> and its contents.
                            # Since it's the very first div in courses_block:
                            # Let's find the closing tag for the space-y-6 div.
                            # It's after all the individual course cards.
                            # We can find the index of the last </div> before the last few spaces and Coluna Direita.
                            # Let's print out the structure to be safe.
                            found_blocks.append((idx, courses_block))

    print(f"Found {len(found_blocks)} matching lines.")
    if found_blocks:
        # Save the last/most recent block
        idx, block = found_blocks[-1]
        print(f"Using block from line {idx}")
        with open(output_path, "w", encoding="utf-8") as out:
            out.write(block)
        print(f"Saved to {output_path}")
    else:
        print("No matching blocks found in history.")
else:
    print("Transcript not found.")
