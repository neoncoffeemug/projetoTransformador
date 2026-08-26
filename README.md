# Projeto Transformador II
Qual técnica de domain adaptation generaliza melhor protocolos de domain shift em datasets de crimes no Brasil?

## Features utilizadas no projeto
| Campos | Descrição | Feature Engieneering
|---|---|--|
|NOME_MUNICIPIO	| Município de registro	| Não			
|DESC_PERIODO | Período da ocorrência | Não
|DESCR_TIPOLOCAL | Descreve subgrupo de tipos de locais, ex: residência| Sim		
|RUBRICA | Natureza jurídica da ocorrência | Não
|MÊS | Mês da ocorrẽncia, extraida da data | Sim 
|DIA_SEM | Dia da semana da ocorrência, extraida de data | Sim
|FERIADO | Retorna um valor booleano se o dia for feriado | Sim

## Target
| Campo | Descrição | Feature Engieneering
|---|---|--|
|DESC_PERIODO | Período da ocorrência | Não

## Baseline do domain-shift
Treino em quatro municípios com distribuição semelhante, teste em um município com distribuição semelhante.

## Modelos
TabFM\
TabPFN\
Random Forest

## Métricas
Accuracy\
Macro F1\
Weighted F1\
Recall


