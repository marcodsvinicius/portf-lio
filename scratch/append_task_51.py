task_path = r"C:\Users\mvsilva23\\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\task.md"

new_task_section = """
# Checklist: Resolução do Travamento de Rolagem (Scroll Lock)

- [x] Rastrear causa raiz de travamento de scroll vertical em dispositivos móveis e desktop
- [x] Identificar e corrigir container `fixed` (cabeçalho) não fechado na linha 83 (adicionando tag `</div>` correspondente)
- [x] Rastrear e validar nível de profundidade de aninhamento (depth 0) de todas as seções principais (`#hero`, `#projects`, `#skills`, `#about`, `#contact`)
- [x] Identificar e remover bloco de dependências e scripts duplicados redundantes (Montserrat, Tailwind e Lucide) no meio do documento
- [x] Validar que todas as tags `div` e `section` estão 100% balanceadas e fechadas em todo o ecossistema do portfólio
- [x] Assegurar 100% de paridade byte a byte entre `index.html` e `index.jhtml` usando o validador `compare.py`
- [x] Documentar o progresso no histórico do portfólio em `walkthrough.md`
"""

with open(r"C:\Users\mvsilva23\..gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\task.md" if False else task_path, "r", encoding="utf-8") as f:
    content = f.read()

updated_content = content.strip() + new_task_section

with open(task_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(updated_content)

print("task.md successfully updated!")
