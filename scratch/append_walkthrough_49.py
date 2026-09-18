import os

walkthrough_path = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\walkthrough.md"

new_section = """
## 49. Redesenho e Ajuste de Espaçamento do Menu Lateral nos Cases (Fim do Esmagamento e Bordas Duplas)

Corrigimos o bug de espaçamento no menu lateral (drawer navigation) de todas as 4 páginas de estudos de caso. O layout anterior sofria com o "esmagamento" dos ícones das redes sociais, que ficavam prensados entre duas linhas divisórias adjacentes muito próximas (uma borda superior própria e a borda superior do botão de voltar), além de carecer de uma estrutura e respiro dedicados para os ícones.

### 1. Melhorias de Design e UX Adotadas:
- **Fim das Bordas Duplas (Layout Unificado)**:
  - Consolidamos a área de rodapé do menu lateral em um único bloco visual (`flex flex-col gap-6 mt-6 pt-6 border-t border-white/10`).
  - Isso eliminou por completo a necessidade de duas linhas divisórias consecutivas, criando exatamente uma única linha separadora limpa de 1px entre a navegação de seções e as ações globais da gaveta.
- **Divisores de Rede Social Premium**:
  - Injetamos pequenos divisores verticais (`<div class="w-px h-4 bg-white/10"></div>`) entre cada um dos quatro ícones (LinkedIn, Pinterest, Medium e GitHub), exatamente como na estética de ponta da página inicial, provendo organização e requinte de grade.
- **Espaçamento e Ergonomia**:
  - Agrupamos o menu com proporções perfeitas usando `gap-6` e `pt-6`, garantindo que o menu seja visualmente harmônico tanto no Desktop quanto no Mobile.
  - Aumentamos o tamanho de toque das redes sociais mantendo o tamanho vetorial ideal de `w-5 h-5`.
- **Efeitos de Hover Consistentes**:
  - Definimos a cor padrão dos ícones como `text-gray-400` para manter a consonância com as cores padrão da navegação.
  - Sob hover, cada ícone de rede social brilha na cor verde neon oficial (`hover:text-[#CCFF00]`) e se expande suavemente com micro-animação de escala (`hover:scale-110 active:scale-95 transition-all duration-300`).

### 2. Arquivos Atualizados de Forma Consistente:
- **Case-Design-System.html**
- **Case-Hub-de-Obras.html**
- **Case-Rebalanceamento-Carteira.html**
- **Case-Tour-Guiado.html**

Com essa alteração, a navegação secundária em todas as páginas de portfólio alcança a mesma qualidade visual e sofisticação da landing page, garantindo uma transição fluida, legível e responsiva em qualquer dispositivo móvel e desktop.
"""

if os.path.exists(walkthrough_path):
    with open(walkthrough_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Append the new section
    if "## 49. Redesenho" not in content:
        with open(walkthrough_path, 'w', encoding='utf-8') as f:
            f.write(content.strip() + "\n" + new_section)
        print("Successfully appended Section 49 to walkthrough.md")
    else:
        print("Section 49 already exists in walkthrough.md")
else:
    print("Walkthrough file not found.")
