from cfg.initializer import AllBots
from datetime import *
import MetaTrader5 as mt5
import pandas as pd
import pytz


# Seta configurações
timezone = pytz.timezone("America/Sao_Paulo")

# Decorator que garante acesso ao terminal mt5 e shutdown ao final
def mt5_conn(mt5_instructions):
    def wrapper(bot_data: AllBots):
        try:
            if not mt5.initialize(**bot_data.meta5_login):
                print("initialize() failed, error code =", mt5.last_error())
                quit()
            mt5_instructions()
            # print('não deu erro')
        finally:
            mt5.shutdown()

    return wrapper


@mt5_conn
def run_bots():
    dt_from = datetime(2016, 1, 10, tzinfo=timezone)
    ticks = mt5.copy_rates_from("DI1F18", mt5.TIMEFRAME_D1, dt_from, 1000)
    print(ticks)

    # print(mt5.terminal_info())

    # di_symbols=mt5.symbols_get("DI1F*")
    # for di in di_symbols:
    #     print(di.name)

    # rates = mt5.copy_rates_range("PETR3", mt5.TIMEFRAME_D1, datetime(2016,1,2), datetime(2022,2,25))
    # ticks_frame = pd.DataFrame(rates)
    # ticks_frame.to_csv('dihistorico.csv')

    # 1 BATCH
    #   Lista de ativos
    #   - DI
    # Especifica fontes dos dados
    # Data Getter: cria conexão, realiza a busca e finaliza
    # estabelecemos a conexão com o terminal MetaTrader 5 para a conta especificada

    # 2 STREAM: serviço separado em mql5 ou c++?
