import sqlite3
import yfinance as yf
import time 

preco_alvo = 40.00
ticker_simbolo = "PETR4"

# Adicionamos o ".SA" necessário para o mercado brasileiro no Yahoo Finance
ticker_yahoo = f"{ticker_simbolo}.SA"

print(f"Iniciando o robô de monitoramento para {ticker_simbolo}...")

# O "while True" cria um loop infinito. Tudo que está "dentro" dele vai se repetir para sempre.
while True:
    # O comando 'try' tenta executar o código abaixo. 
    # Se algo der errado (ex: sem internet), ele pula direto para o 'except'.
    try:
        print("\nBuscando o preço na internet...")

        ticker = yf.Ticker(ticker_yahoo)
        dados = ticker.history(period="1d")

        if dados.empty:
            print("Nenhum dado retornado. O mercado pode estar fechado ou o Yahoo demorou a responder.")
        else:
            preco_formatado = round(dados['Close'].iloc[0], 2) 
            print(f"Preço atualizado: R$ {preco_formatado}")

            print("Salvando no banco de dados...")

            conexao = sqlite3.connect("acoes.db")
            cursor = conexao.cursor()  
            
            # CORREÇÃO: codigo_acai alterado para codigo_acao
            cursor.execute("UPDATE acoes SET preco = ? WHERE codigo_acao = ?", (preco_formatado, ticker_simbolo))
            conexao.commit()
            conexao.close()

            print("-" * 40)
            if preco_formatado <= preco_alvo:
                print(f"ALERTA: A {ticker_simbolo} caiu para R${preco_formatado}") 
            else:    
                print(f"A {ticker_simbolo} está R$ {preco_formatado}. Acima do alvo (R$ {preco_alvo}). Aguarda.") 
            print("-" * 40)  

    except Exception as erro:
        print(f"Ocorreu um problema de conexão ou no banco: {erro}")  
        # CORREÇÃO: Erros de digitação ajustados
        print("O robô não vai parar. Tentando novamente no próximo ciclo...") 

    print("Aguardando 1 minuto para a próxima checagem...\n")
    time.sleep(60)