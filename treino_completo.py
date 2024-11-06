# Importando bibliotecas necessárias
from datetime import datetime, timedelta

# Função para gerar treino baseado nos parâmetros do usuário


def gerar_treino(biotipo, objetivo, dias_disponiveis, tipo_exercicio):
    treino = ""
    if biotipo == "Ectomorfo" and objetivo == "Ganho de Massa":
        if dias_disponiveis == 3:
            treino = "Treino ABC: A) Peito e Tríceps, B) Costas e Bíceps, C) Pernas e Ombros."
        elif dias_disponiveis >= 5:
            treino = "Treino ABCDE: divisão específica para hipertrofia."
    elif biotipo == "Endomorfo" and objetivo == "Perda de Peso":
        treino = "Treino com foco em HIIT + cardio para otimizar queima de gordura."
    else:
        treino = "Treino personalizado de resistência."
    return treino

# Função de aquecimento e alongamento


def aquecimento(tipo_exercicio):
    if tipo_exercicio == "Funcional":
        return "Aquecimento: 5 minutos de alongamento dinâmico e mobilidade."
    elif tipo_exercicio == "Peso Livre":
        return "Aquecimento: 10 minutos com pesos leves."
    else:
        return "Aquecimento: 10 minutos de cardio leve."

# Função para sugestões de recuperação


def sugestoes_recuperacao():
    return "Sugestão: 7-8 horas de sono, foam rolling e hidratação adequada."

# Função para verificar a hidratação e recomendar nutrição


def acompanhamento_nutricional():
    return "Lembrete de hidratação: Beba água entre séries. Dica nutricional: Consuma proteínas e carboidratos após o treino."

# Função para monitorar e ajustar o treino de acordo com feedback


def feedback_treino(dificuldade):
    if dificuldade == "fácil":
        return "Aumente a intensidade do treino na próxima sessão."
    elif dificuldade == "difícil":
        return "Mantenha o nível atual por mais duas semanas."
    else:
        return "Nível adequado, continue assim."

# Função principal para rodar o copilot


def copilot_exercicio(biotipo, objetivo, dias_disponiveis, tipo_exercicio, feedback):
    print("=== Seu Treino Personalizado ===")
    print(gerar_treino(biotipo, objetivo, dias_disponiveis, tipo_exercicio))
    print(aquecimento(tipo_exercicio))
    print(sugestoes_recuperacao())
    print(acompanhamento_nutricional())
    print(feedback_treino(feedback))
    print("=================================")


# Exemplo de execução
copilot_exercicio(
    biotipo="Ectomorfo",
    objetivo="Ganho de Massa",
    dias_disponiveis=3,
    tipo_exercicio="Peso Livre",
    feedback="adequado"
)
