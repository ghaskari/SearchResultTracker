import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
from setup import SetupSearchEngine


class SearchApp:
    def __init__(self):
        SearchEngine = SetupSearchEngine()
        self.perform_search = SearchEngine.perform_search
        self.process_results = SearchEngine.process_results
        self.create_dataframe = SearchEngine.create_dataframe

    def show_search_results(self):
        query = self.entry.get()
        search_results = self.perform_search(query)
        ranking, site_name, results = self.process_results(search_results)
        search_results_df = self.create_dataframe(ranking, site_name, results)

        results_window = tk.Toplevel(self.root)
        results_window.title("Search Results")

        text_box = scrolledtext.ScrolledText(results_window, width=60, height=20)
        text_box.pack()

        for result in search_results:
            text_box.insert(tk.END, result + '\n')

        text_box.config(state=tk.DISABLED)

        data_results = pd.DataFrame()
        for query_name, df in search_results_df.items():
            data_results = pd.concat([data_results, df], ignore_index=True, axis=1)

        data_results.columns =['Ranking', 'Site', 'Link']
        data_results.to_csv(f'Sample/{query.strip()}_search_history.csv', index=False)

    def run(self):
        self.root = tk.Tk()
        self.root.title("Search Box Example")

        label = tk.Label(self.root, text="Enter your search query:")
        label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        search_button = tk.Button(self.root, text="Search", command=self.show_search_results)
        search_button.pack()

        self.root.mainloop()
