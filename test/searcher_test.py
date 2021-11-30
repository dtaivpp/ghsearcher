from ghsearcher import searcher

def test_search():
  results = searcher.search("ghripper repo:dtaivpp/ghripper", endpoint='code')

  final_result = []
  for result in results:
    final_result.extend(result)

  assert len(final_result) >= 5
