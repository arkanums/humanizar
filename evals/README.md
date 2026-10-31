# Testes

Cada caso em `cases.json` tem um texto de IA, as expressões que têm de desaparecer (`must_not_contain`) e os factos que têm de ficar (`must_keep`). Use-os antes e depois de mudar o `SKILL.md` ou `references/pt-pt.md`, para ver se a mudança melhorou ou piorou o resultado.

1. Ver os casos: `python3 scripts/check-eval.py --list`
2. Dar o `input` de um caso à skill no seu agente (por exemplo, `/humanizar` e colar o texto).
3. Guardar só a versão final num ficheiro, por exemplo `saida.txt`.
4. Verificar: `python3 scripts/check-eval.py pt-anuncio saida.txt`

O script só apanha frases exatas. Leia sempre a reescrita: um teste que passa pode ter inventado um facto ou soar mal.

Para acrescentar um caso, use texto real (sem dados privados) e escreva nas `notes` o que o caso testa.
