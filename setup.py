from googlesearch import search
import pandas as pd


class SetupSearchEngine:

    @staticmethod
    def perform_search(query):
        try:
            return list(search(query, num_results=100))
        except ImportError:
            print("No module named 'google' found")
            return []

    @staticmethod
    def process_results(results):
        ranking_list = []
        site_name_list = []
        results_list = []

        for rank, result in enumerate(results, start=1):
            result = result.replace('www.', '')
            print(result)
            ranking_list.append(rank)
            print(ranking_list)
            site_name_list.append(result.split('/')[2])
            results_list.append(result)

        return ranking_list, site_name_list, results_list

    @staticmethod
    def create_dataframe(ranking, site_name, results):
        data = {'Ranking': ranking, 'Site Name': site_name, 'Results': results}
        return pd.DataFrame(data)
