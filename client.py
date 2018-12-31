import sys
import io

from SPARQLWrapper import SPARQLWrapper, CSV
import pandas as pd

__author__ = "Aisha Mohamed <ahmohamed@qf.org.qa>"


class Client(object):
    """
    class for sparql client that handles communication with a sparql end-point
    over http using the sparql wrapper library.
    """
    def __init__(self, endpoint):
        """
        Constructs an instance of the client class
        :param endpoint: string of the SPARQL endpoint's URI hostname:port
        :type endpoint: string
        """
        # TODO: check that the endpoint string is a URI
        self.endpoint = endpoint

    def is_alive(self, endpoint=None):
        """
        :param endpoint string of the SPARQL endpoint's URI
        :type endpoint string
        :return if endpoint is not None return Ture if endpoint is alive else
            return False. if endpoint is None return True if self.endpoint is
            alive and False otherwise.
        """
        pass

    def get_endpoint(self):
        """
        :return a string of the endpont URI
        """
        return self.endpoint

    def set_endpoint(self, endpoint):
        """
        updates self.endpoint with the new endpoint
        :param endpoint: endpoint uri
        """
        self.endpoint = endpoint

    def execute_query(self, query, output_file=None):
        """
        Connects to the sparql endpoint, sends the query and returns a dataframe
            containing the result of the sparql query.
        :param query: a valid sparql query string.
        :type query: string
        :param return_format: the return format of the output, one of: ["csv",]
        :type return_format: string
        :param output_file: the path to the output file.
        :type output_file: string
        :return: a pandas dataframe representing the result of the query
        """
        #TODO: Allow for the execution of multiple queries if needed
        #TODO: Add the other return formats
        #TODO: check the query and find out if its valid
        #TODO: check if the connection is successful
        client = SPARQLWrapper(self.endpoint)
        client.setQuery(query)
        try:
            client.setReturnFormat(CSV)
            results = client.query().convert() # string
        except Exception as e:
            print(e)
            sys.exit()

        results = results.decode("utf-8")
        f = io.StringIO(results)

        # convert it to a dataframe
        f.seek(0)
        df = pd.read_csv(f, sep=',') # to get the values and the header

        if output_file is not None:
            df.to_csv(output_file)

        return df
