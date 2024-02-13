import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv

load_dotenv()
service_name = os.environ.get("SERVICE_NAME")
index_name = os.environ.get("INDEX_NAME")
key = os.environ.get("ADMIN_KEY")

endpoint = f"https://{service_name}.search.windows.net/"


class QueryResults:
    def __init__(self, search_text):
        self.search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))
        self.search_text = search_text

    def get_search_results(self):
        """
        Searches for the given query and provides the results accordingly.
        :return: Query Results
        """
        try:
            query = self.search_text
            return self.search_client.search(query, include_total_count=True)
        except Exception as error:
            print(f"Exception has occurred. {error}")

    def get_dataset_length(self):
        """
        Get the length of dataset
        :return: Length
        """
        return self.search_client.get_document_count()


if __name__ == "__main__":

    if text_to_be_searched := input("Enter a value to be searched based on Department/Gender/JobRole : "):
        query_results_obj = QueryResults(search_text=text_to_be_searched)
        print(f"The length of dataset is {query_results_obj.get_dataset_length()}")
        query_results = query_results_obj.get_search_results()
        query_results_length = query_results.get_count()
        if query_results_length > 0:
            print(f"Found {query_results_length} results for {text_to_be_searched}.")
            for result in query_results:
                print(f"JobRole : {result['JobRole']}, "
                      f"Department : {result['Department']}, "
                      f"Age : {result['Age']}, "
                      f"Gender : {result['Gender']}")
        else:
            print(f"No results found for {text_to_be_searched}")
    else:
        print("Please provide a value to be searched.")
