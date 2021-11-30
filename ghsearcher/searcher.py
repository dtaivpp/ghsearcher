import logging
import argparse
from os import getenv
from pprint import pprint
from dotenv import load_dotenv
from ghapi.all import GhApi
from ghsearcher.helpers import RateLimiter
from ghsearcher.helpers import paginator


load_dotenv()
GH_TOKEN = getenv('GH_TOKEN', None)
DEFAULT_ENDPOINT='code'

#### Logging config
console_out = logging.getLogger("ghsearcher")
consoleOutHandle = logging.StreamHandler()
consoleOutHandle.setLevel(logging.INFO)
consoleOutFormatter = logging.Formatter('%(asctime)s - %(message)s')
consoleOutHandle.setFormatter(consoleOutFormatter)
console_out.addHandler(consoleOutHandle)
console_out.setLevel(logging.INFO)

logger = logging.getLogger("debug")
consoleHandle = logging.StreamHandler()
consoleHandle.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
consoleHandle.setFormatter(formatter)
logger.addHandler(consoleHandle)
logger.setLevel(logging.ERROR)


def get_client() -> GhApi:
  """Return the GitHub Client"""
  logger.debug("Creating GitHub API Object %s GitHub Token",
               'with' if GH_TOKEN is not None else 'without')

  return GhApi(token=GH_TOKEN)


def search(query: str, endpoint:str = DEFAULT_ENDPOINT, client: GhApi = None) -> list:
  """Yeilds search result pages"""
  if client == None:
    client = get_client()

  search_config = {
    'users': client.search.users,
    'code': client.search.code,
    'issues': client.search.issues,
    'commits': client.search.commits,
    'labels': client.search.lables,
    'repositories': client.search.repositories,
    'topics': client.search.topics
  }

  search_gen = paginator(search_config.get(endpoint), q=query)
  rate_limits = RateLimiter(client)

  for results in search_gen:
    logger.debug("Current Rate Limits: %s",
                 rate_limits.get_rate_limits('search'))
    rate_limits.check_safety("search")
    yield results.get('items', default=[])


def query_builder(query=None, scope=None, target=None):
  full_query = [
    query,
    reduce_scope(scope, target)
  ]

  return " ".join(full_query)


def reduce_scope(scope, target) -> str:
  if scope != None and target != None:
    return f"{scope}: {target}"

  return ""


def cli_entry():
  """Parse arguments and kickoff the process"""
  parser = argparse.ArgumentParser(
    description='Search for things in GitHub')


  parser.add_argument(
    '-v',
    '--version',
    action='version',
    version='%(prog)s 0.0.1')


  parser.add_argument(
    '--debug',
    action='store_true',
    help='Set this if you would like to see verbose logging.')


  parser.add_argument(
    '-e',
    '--endpoint',
    choices=[
      'users',
      'code',
      'issues',
      'commits',
      'labels',
      'repositories',
      'topics'
    ],
    default=DEFAULT_ENDPOINT,
    help='Endpoint you would like to search')


  parser.add_argument(
    '-q',
    '--query',
    required=True,
    nargs='+',
    help='Query you would like to use to search')


  args = parser.parse_args()

  if args.debug:
    logger.setLevel(logging.DEBUG)

  client = get_client()

  results = []
  for query in args.querys:
    tmp = search(query, args.endpoint, client)
    pprint(tmp)
    results.extend(tmp)


if __name__=='__main__':
  cli_entry()
