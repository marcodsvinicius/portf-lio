# Revisão da home — portfólio v2

## Direção implementada

- Posicionamento amplo: Product Designer Sênior · AI First · UX/UI, sem restringir a atuação a produtos financeiros ou B2B.
- Título aprovado: “Transformo processos complexos em experiências digitais claras.”
- Ações principais: Ver projetos e Falar comigo. Currículo e LinkedIn como acessos complementares.
- Quatro projetos com o mesmo peso visual, nesta ordem: Tour Guiado, Rebalanceamento, Design System e Hub de Obras.
- Imagens permanentes nos cards em desktop e mobile, com descrição, contribuição e entrega em destaque.
- Hub identificado como Em desenvolvimento · Acesso restrito, com Solicitar acesso por e-mail e Já tenho a senha, que utiliza o modal existente.
- IA apresentada em três momentos: entender e organizar, explorar e prototipar, revisar e entregar. Cada bloco explicita apoio da IA e responsabilidade do designer.
- Quatro competências: UX para produtos complexos, UI e Design Systems, design com implementação em mente e colaboração/liderança.
- Três trechos fiéis das recomendações existentes: Bruno Caregnatto, Danyllo Lisboa e Nathasha Fariña. Inglês identificado como tradução.
- Sobre com formação e contexto profissional, três experiências selecionadas e expansão para o restante da trajetória. Dados existentes de cargos e datas preservados.
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
