__author__ = ["Gabriel Cerioni", "Francisco Junior"]
__copyright__ = "Copyright 2021, Gabs the Creator"
__credits__ = ["Gabriel Cerioni", "Francisco Junior"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = ["Gabriel Cerioni", "Francisco Junior"]
__email__ = "gabriel.cerioni@harness.io"
__status__ = "Production"

import re
import os
import random
import logging
import time

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.requests import log as requests_logger

# Configs (if this gets bigger, I'll provide a config file... or even Hashicorp Vault)
# logging.basicConfig(filename='gabs_graphql.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
requests_logger.setLevel(logging.WARNING)

# API_KEY = "<YOUR_KEY>"
# API_ENDPOINT = "https://app.harness.io/gateway/api/graphql?accountId=<ACC_ID>"
API_KEY = os.environ.get('HARNESS_GRAPHQL_API_KEY')
HARNESS_ACCOUNT = os.environ.get('HARNESS_ACCOUNT')
API_ENDPOINT = "https://app.harness.io/gateway/api/graphql?accountId={0}".format(HARNESS_ACCOUNT)


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
    print("mutation_result:" + str(result))
    return result


def get_harness_account_users_to_be_deleted():
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
                id
      email
      userGroups(limit:5) {
        nodes {
          name
          id
        }
      }
            }
        }
        }'''

        generic_query_result = generic_graphql_query(query)
        loop_user_list = generic_query_result["users"]["nodes"]
        print(loop_user_list)
        for i, val in enumerate(loop_user_list):

            if not val["userGroups"]["nodes"]:
                obj = {}
                obj["id"] = val["id"]
                obj["email"] = val["email"]
                total_user_list.append(obj)
        # total_user_list.extend(loop_user_list)

        #total = generic_query_result["users"]["pageInfo"]["total"]
        has_more = bool(generic_query_result["users"]["pageInfo"]["hasMore"])

        if has_more:
            offset = offset + 100
    return total_user_list


def delete_users(user_list):
    logging.info("Usrs tp n{0} ".format(len(user_list)))
    paginated_list = [user_list[i:i+100]
                      for i in range(0, len(user_list), 100)]

    for i, user_list in enumerate(paginated_list):
        final_graph_ql = "mutation {\n"
        for i, user in enumerate(user_list):
            final_graph_ql += generate_user_delete_graphql(user, i)
        final_graph_ql += "}"
        print("#############################")
        print("####Batch to delete #########")
        print("#############################")

        print(final_graph_ql)

        # call mutation to delete
        generic_graphql_mutation(final_graph_ql, {})
        # check results

        # sleep for 2 seconds for server to breath
        time.sleep(2)

        #query_variables = {"user": {"name": name, "email": email, "clientMutationId": str(hash_mutation), "userGroupIds": usergroupids_list}}

        #generic_graphql_mutation(mutation_query, query_variables)


def generate_user_delete_graphql(user, index):
    user_id = user.get('id')
    email = user.get('email')
    mutation_query = '''
        user''' + str(index) + ''': deleteUser(input: {id: "''' + user_id + '''", clientMutationId: "''' + email + '''"}) {
            clientMutationId
        } \n'''

    return mutation_query


if __name__ == '__main__':
    logging.info("Starting the Program...")

    logging.info("Getting all users to be deleted from your Harness Account")
    logging.info("Users with no Groups")
    result_from_query = get_harness_account_users_to_be_deleted()
    print("Users to be deleted {0}".format(len(result_from_query)))
    delete_users(result_from_query)

    #logging.info("Done! You have {0} users in your Account!".format(len(result_from_query)))
    print("")
    logging.info("Printing the Deleted User List on your STDOUT")

    print(result_from_query)

    logging.info("Program Exited!")
