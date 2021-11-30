import logging
import argparse
from os import getenv
from dotenv import load_dotenv
from ghapi.all import GhApi
from ghsearcher.helpers import RateLimiter
from ghsearcher.helpers import paginator


load_dotenv()
GH_TOKEN = getenv('GH_TOKEN', None)

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


def search(query: str, client: GhApi):
  """Yeilds results pages"""
  search_gen = paginator(client.search.code, q=query)
  rate_limits = RateLimiter(client)

  for results in search_gen:
    logger.debug("Current Rate Limits: %s",
                 rate_limits.get_rate_limits('search'))
    rate_limits.check_safety("search")
    yield results


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


def main(debug, config):
  """Main logic of the program"""
  if debug:
    logger.setLevel(logging.DEBUG)


  for key, value in input:
    input[key]["query"] =f"{value['find']} {value['scope']}:{key}"
  
  client = get_client()
  results = []

  for gh_object in input.values():
    logger.debug("Running query: %s", gh_object["query"])

    for result in search_results(gh_object["query"], client):
      updated_results = [{"query": gh_object["query"], **item} for item in result["items"]]
      results.extend(updated_results)


  

def cli_entry():
  """Parse arguments and kickoff the process"""
  parser = argparse.ArgumentParser(
    description='Search and replace text in GitHub repositories')


  parser.add_argument(
    '-v',
    '--version',
    action='version',
    version='%(prog)s 0.0.1')


  parser.add_argument(
    '-c',
    '--config',
    default='config.yaml',
    help='Config file for what to find and replace')


  parser.add_argument(
    '--debug',
    action='store_true',
    help='Set this if you would like to see verbose logging.')


  args = parser.parse_args()
  main(**vars(args))


if __name__=='__main__':
  cli_entry()
