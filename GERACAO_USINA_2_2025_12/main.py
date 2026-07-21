import pandas as pd
import matplotlib.pyplot as plt

def processar_geracao_energia():
    try:
        # --- CARREGAMENTO ÚNICO (Fora do Loop) ---
        print("Carregando base de dados... Isso pode levar alguns segundos.")
        df = pd.read_excel('dados/GERACAO_USINA-2_2026_02.xlsx')
        
        # Tratamento de Datas feito apenas uma vez para otimizar memória
        df['din_instante'] = pd.to_datetime(df['din_instante'])
        df['Dia'] = df['din_instante'].dt.day
        df['Hora'] = df['din_instante'].dt.hour
        
        # --- LOOP PRINCIPAL DE INTERAÇÃO ---
        # Este loop mantém o programa vivo até o comando 'sair'
        while True:
            # Linha separadora para limpar visualmente o console a cada nova execução
            print("\n" + "="*60)
            print("ANÁLISE DE GERAÇÃO DE ENERGIA - ONS")
            print("="*60)
            
            # PASSO 4: Interatividade e Validação
            # Usamos .strip() para remover espaços acidentais que o usuário possa digitar
            input_dia = input("Selecione o dia que você deseja ver (1 a 24) ou digite 'sair' para encerrar: ").strip()
            
            # 1. Verificação de saída (Independente de maiúsculas/minúsculas)
            if input_dia.lower() == 'sair':
                print("\nEncerrando o programa. Até logo!")
                break # Quebra o loop principal e finaliza a função
                
            # 2. Validação da entrada numérica
            try:
                dia_selecionado = int(input_dia)
                if not (1 <= dia_selecionado <= 24):
                    print("Aviso: Escolha um dia válido entre 1 e 24 de fevereiro de 2026.")
                    continue # Pula o resto do código e volta para o início do loop (pedir input)
            except ValueError:
                print("Erro: Entrada inválida. Digite um número inteiro ou a palavra 'sair'.")
                continue # Volta para o início do loop

            # --- PASSO 5: Filtragem e Agregação ---
            # Como o input foi validado, prosseguimos com a análise do dia escolhido
            print(f"Gerando gráfico para o dia {dia_selecionado}... (Feche a janela do gráfico para consultar outro dia)")
            
            df_dia = df[df['Dia'] == dia_selecionado]
            ger_hora = df_dia.groupby('Hora')['val_geracao'].sum().reset_index()

            # --- PASSO 6: Configuração da Visualização (Matplotlib) ---
            plt.figure(figsize=(15, 8))
            
            barras = plt.bar(ger_hora['Hora'], ger_hora['val_geracao'], 
                           color='#2ecc71', edgecolor='black', alpha=0.8)

            # Rótulos de dados (Data Labels)
            for bar in barras:
                valorY = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, valorY + (ger_hora['val_geracao'].max() * 0.01), 
                         f'{int(valorY)}', ha='center', va='bottom', fontsize=9, fontweight='bold')

            # Customização de Títulos e Eixos
            plt.title(f'Quanta energia é gerada no Brasil a cada hora?\n(Dia {dia_selecionado:02d}/02/2026)', 
                      fontsize=16, pad=20, fontweight='bold')
            plt.xlabel('Hora do Dia (00h - 23h)', fontsize=12)
            plt.ylabel('Geração Total (MW)', fontsize=12)
            
            plt.xticks(range(0, 24))
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            
            # Exibe o gráfico. 
            # NOTA: O código ficará "pausado" aqui até o usuário fechar a janela do gráfico.
            # Quando a janela fechar, o loop recomeça naturalmente.
            plt.show()

    except FileNotFoundError:
        print("\n Erro: O arquivo 'dados/GERACAO_USINA-2_2026_02.xlsx' não foi encontrado.")
    except Exception as e:
        print(f"\n Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    processar_geracao_energia()

    # --- MELHORIAS IMPLEMENTADAS ---
#
# 1. Eficiência de Memória: Tirei o pd.read_excel e os .dt.day / .dt.hour de dentro do loop. 
# Agora o arquivo é lido e tratado uma única vez. O loop serve apenas para filtrar a tabela 
# que já está pronta na memória e desenhar o gráfico. Isso deixa o programa 100x mais 
# rápido entre as pesquisas.
#
# 2. Uso de .strip() e .lower(): Ao pegar o input, input_dia.lower() == 'sair' garante 
# que "SAIR", "Sair", ou "sair" funcionem. O .strip() garante que se o usuário bater no 
# espaço sem querer (ex: "sair "), o programa ainda reconheça a palavra.
#
# 3. Controle de Fluxo com continue: Substituí o antigo while True aninhado pelo comando 
# continue. Se o usuário digitar "abacate" ou "30", o código exibe o erro e usa o continue 
# para jogar a execução de volta para a primeira linha do loop, pedindo a data novamente de 
# forma limpa.
#
# 4. Alerta de UX (Experiência do Usuário): Adicionei um print avisando o usuário que ele 
# precisa fechar a janela do gráfico para conseguir fazer a próxima consulta, já que o 
# comando plt.show() paralisa a execução do Python enquanto a janela estiver aberta.


"""
Resumido:
- Eficiência de Memória: Tirei o pd.read_excel e os .dt.day / .dt.hour de dentro do loop...
- Uso de .strip() e .lower(): Ao pegar o input, input_dia.lower() == 'sair' garante...
- Controle de Fluxo com continue: Substituí o antigo while True aninhado...
- Alerta de UX (Experiência do Usuário): Adicionei um print avisando o usuário...
"""