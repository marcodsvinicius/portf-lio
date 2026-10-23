# Revisão da home — portfólio v2

## Direção implementada

- Posicionamento amplo: Product Designer Sênior · AI First · UX/UI, sem restringir a atuação a produtos financeiros ou B2B.
- Título aprovado: “Transformo processos complexos em experiências digitais claras.”
- Ações principais: Ver projetos e Falar comigo. Currículo e LinkedIn como acessos complementares.
- Quatro projetos com o mesmo peso visual, nesta ordem: Tour Guiado, Rebalanceamento, Design System e Hub de Obras.
- Imagens permanentes nos cards em desktop e mobile, com descrição, contribuição e entrega em destaque.
- Hub identificado como Em desenvolvimento · Acesso restrito, com Solicitar acesso por e-mail e Já tenho a senha, que utiliza o modal existente.
- IA apresentada em quatro momentos: entender e organizar, explorar e prototipar, revisar e entregar, gerenciar e otimizar. O quarto bloco conecta a evolução do Design System a skills, agentes e reaproveitamento de componentes. Cada bloco explicita apoio da IA e responsabilidade do designer. A grade usa duas colunas no desktop/tablet e uma no mobile.
- Quatro competências: UX para produtos complexos, UI e Design Systems, design com implementação em mente e colaboração/liderança.
- Três trechos fiéis das recomendações existentes: Bruno Caregnatto, Danyllo Lisboa e Nathasha Fariña. Inglês identificado como tradução.
- Sobre com formação e contexto profissional, quatro experiências selecionadas (OceanPact, Banco do Brasil, Cypher e Nelogica). Ao expandir, as demais entram na mesma lista, ordenada pela data de término, da mais recente à mais antiga, com o vínculo atual primeiro. Não há uma segunda sequência nem duplicação dos vínculos. Dados existentes de cargos e datas preservados.
- Formação resumida; cursos e certificações continuam disponíveis em uma expansão.
- Resumo rápido atualizado para descrever entregas dos cases, sem atribuir redução de churn não mensurada.
- Português e inglês com a mesma estrutura; links de empresa abrem a trajetória quando o cargo está dentro da expansão.

## Ordem da página

1. Abertura.
2. Empresas.
3. Projetos.
4. IA aplicada ao design.
5. Competências.
6. Recomendações.
7. Sobre, experiência e formação.
8. Contato.

## Pendências de conteúdo

- [ ] Revisão do Marco sobre textos, ordem dos projetos, recortes das recomendações e competências.
- [ ] Receber o relato detalhado de IA aplicado ao Hub, para inserção no case e eventual chamada na home.
- [ ] Acrescentar evidências complementares conforme `REVISAO-CASES-V2.md`.
- [ ] Fornecer o endereço do certificado de Figma Avançado: o material anterior tinha um link `#`. O curso permanece listado, com a ação sem destino omitida.

Não foram criadas falas de usuários, métricas, experiências ou certificações. Os ajustes técnicos gerais do ponto 10 permanecem pendentes, conforme solicitado.

## Validação

- `npm run build` concluído.
- Home PT/EN em 320, 390, 768, 1024 e 1440 px: dez combinações.
- Imagens dos quatro cards carregando e visíveis sem hover; grade com quatro cards de mesma largura no desktop.
- Sem rolagem horizontal no documento ou no body nas dez combinações.
- Resumo, menu, navegação para competências, expansão automática da trajetória e modal do Hub verificados.
- Senha inválida rejeitada no modal do Hub; solicitação de acesso preserva link de e-mail.
- Links dos três projetos públicos abrem os cases correspondentes.
- Conferência de regressão das oito páginas de cases em 320, 768 e 1440 px: 24 combinações.
- Sem erros JavaScript durante as verificações; inspeção visual da home e dos cards em desktop e mobile.

## Comparação

- Nova home: `https://marcodsvinicius.github.io/portf-lio/preview/v2/`.
- Versão atual: `https://marcodsvinicius.github.io/portf-lio/`.
- Página de revisão com acessos aos cases: `/preview/v2/revisao.html`.
- Fonte de trabalho: branch `feat/portfolio-v2`; alterações mantidas no PR de revisão.

## Revisão da ordem das experiências

- Seleção visível: OceanPact, Banco do Brasil, Cypher e Nelogica.
- Trajetória completa: OceanPact → Banco do Brasil → GameOn → MAG Seguros → Cypher → Nelogica → Freelance → LivreLab → DarwinX.
- Critério: vínculo atual primeiro, seguido dos demais pela data de término em ordem decrescente.
- Cada experiência ocupa uma única posição no histórico; o botão revela as posições intermediárias e permite retornar à seleção.
- Os links de empresas continuam revelando automaticamente os vínculos que estavam recolhidos.
- Sem JavaScript, a lista completa permanece acessível e o botão de alternância fica oculto.
- Pendência editorial: confirmar se os tipos de vínculo precisam de mais contexto nas atuações com períodos sobrepostos. Datas, durações e empresas foram mantidas, sem inferir regime parcial ou exclusividade.

## Proposta visual para contato

- Estudo separado em `proposta-contato.html`, sem substituir a seção da home nesta etapa de proposta.
- Canvas colaborativo com um desafio e uma interface em construção, acompanhado pelos cursores ilustrativos Você e Marco.
- Texto, disponibilidade, horário do Rio, currículo, e-mail, copiar endereço e redes sociais preservados da seção atual.
- Movimento curto e discreto nos cursores, com preferência por movimento reduzido respeitada.
- A proposta está acessível pelo índice de revisão; aguarda avaliação visual do Marco.
