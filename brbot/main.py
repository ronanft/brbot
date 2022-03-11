import argparse
from cfg.initializer import AllBots
from databots.b3 import run_bots
# import MetaTrader5 as mt5


if __name__ == "__main__":

    # Parsing command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-mtlogin", help="Login MetaTrader 5", type=int)
    parser.add_argument("-mtpass", help="Senha MetaTrader 5", type=str)
    parser.add_argument("-mtserver", help="Server MetaTrader 5", type=str)
    args = parser.parse_args()

    # Instantiate AllBots
    bot_session = AllBots(vars(args))
    run_bots(bot_session)
