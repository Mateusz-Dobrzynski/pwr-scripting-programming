from price_history import PriceHistory
import pandas as pd


class SpreadsheetSaver:
    def save_history_to_file(self, history: PriceHistory, path: str):
        times = history.get_times()
        index = pd.DatetimeIndex(times)
        values = history.get_values()
        input_dict = {"value": values}
        frame = pd.DataFrame(input_dict, index)
        frame.to_excel(path)
