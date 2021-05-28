__author__ = "Gabs the CSE"
__copyright__ = "Copyright 2021, Gabs the Creator"
__credits__ = ["Gabriel Cerioni"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Gabriel Cerioni"
__email__ = "gacerioni@gmail.com"
__status__ = "Production"

import re
import os
import random
import logging

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.requests import log as requests_logger

# Configs (if this gets bigger, I'll provide a config file... or even Hashicorp Vault)
# logging.basicConfig(filename='gabs_graphql.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
requests_logger.setLevel(logging.WARNING)

# API_KEY = "<YOUR_KEY>"
# API_ENDPOINT = "https://app.harness.io/gateway/api/graphql?accountId=<ACC_ID>"
API_KEY = os.environ.get('HARNESS_GRAPHQL_API_KEY')
API_ENDPOINT = os.environ.get('HARNESS_GRAPHQL_ENDPOINT')


def generic_graphql_query(query):
    req_headers = {
        'x-api-key': API_KEY
    }

    _transport = RequestsHTTPTransport(
        url=API_ENDPOINT,
        headers=req_headers,
        use_json=True,
    )

    # Create a GraphQL client using the defined transport
    client = Client(transport=_transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    generic_query = gql(query)

    # Execute the query on the transport
    result = client.execute(generic_query)
    return result


def generic_graphql_mutation(mutation_query, params):
    req_headers = {
        'x-api-key': API_KEY
    }

    _transport = RequestsHTTPTransport(
        url=API_ENDPOINT,
        headers=req_headers,
        use_json=True,
    )

    # Create a GraphQL client using the defined transport
    client = Client(transport=_transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    generic_query = gql(mutation_query)

    # Execute the query on the transport
    result = client.execute(generic_query, variable_values=params)
    return result


def multiple_dummy_users_loader(user_amount, name_template, email_template, usergroupids_list):

    for i in range(1, user_amount+1):
        name = "{0}_{1}".format(name_template, i)
        email = re.sub(r'(@)', r'_{0}\1'.format(i), email_template)
        hash_mutation = random.getrandbits(32)

        mutation_query = '''
        mutation createUser($user: CreateUserInput!) {
          createUser(input: $user) {
            user {
              id
              email
              name
              userGroups(limit: 5) {
                nodes {
                  id
                  name
                }
            }
          }
          clientMutationId
            }
        }
        '''

        query_variables = {"user": {"name": name, "email": email, "clientMutationId": str(hash_mutation), "userGroupIds": usergroupids_list}}

        generic_graphql_mutation(mutation_query, query_variables)

def get_harness_account_users():
    offset = 0
    has_more = True
    total_user_list = []

    while has_more:
        query = '''{
        users(limit: 100, offset: ''' + str(offset) + ''') {
            pageInfo {
                total
                limit
                hasMore
                offset
            }
            nodes {
                name
            }
        }
        }'''

        generic_query_result = generic_graphql_query(query)
        loop_user_list = generic_query_result["users"]["nodes"]
        total_user_list.extend(loop_user_list)

        #total = generic_query_result["users"]["pageInfo"]["total"]
        has_more = bool(generic_query_result["users"]["pageInfo"]["hasMore"])

        if has_more:
            offset = offset + 100

    return total_user_list


if __name__ == '__main__':
    logging.info("Starting the Program...")

    logging.info("Getting all users from your Harness Account")
    result_from_query = get_harness_account_users()
    logging.info("Done! You have {0} users in your Account!".format(len(result_from_query)))
    print("")
    logging.info("Printing the User List on your STDOUT")

    print(result_from_query)

    logging.info("Program Exited!")


