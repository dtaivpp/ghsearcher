# GitHub Searcher
ghsearcher is a utility for searching GitHub from the command line.

## Usage

1. Install with pip `pip install ghsearcher`
2. (Optional) you can either export an environment variable named "GH_TOKEN" or include it in a local .env file to ensure you can make the most requests. See ["Creating a personal access token"](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for more information on how to do so.

```
usage: ghsearcher [-h] [-v] [--debug] [-e {users,code,issues,commits,labels,repositories,topics}] -q QUERY [QUERY ...]

Search for things in GitHub

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --debug               Set this if you would like to see verbose logging.
  -e {users,code,issues,commits,labels,repositories,topics}, --endpoint {users,code,issues,commits,labels,repositories,topics}
                        Endpoint you would like to search
  -q QUERY [QUERY ...], --query QUERY [QUERY ...]
                        Query you would like to use to search
```

<!--
Here is a simple example:
```
# The source is a repo and it is running against the gh_dorks_test.txt file
ghdorker -s repo -d samples/dorks.txt dtaivpp/NewsTicker
```

Additionally you can create a yaml config file like so for using only specific dorks on repos.
```yaml
dtaivpp/cloud_haiku:
  scope: repo, org, user
  find: "Testing code long time"
  replace_with: "NO"
  branch_name: "GHRipper_Replacement"
  commit_message: "Testing code long time -> NO"
  push: False
```

This would run all the dorks that fall under the cloud section of the YAML.
```
ghdorker -s repo dtaivpp/NewsTicker -d samples/dorks.yaml --options all.cloud
```

This would run all the dorks that fall under the aws and the identity sections. It's okay to duplicate entries under different sections as on the backend it is checking each entry for uniqueness.
```
ghdorker -s repo dtaivpp/NewsTicker -d samples/dorks.yaml --options all.cloud.aws all.identiy
```

And finally here is an example of how you could output the results to either a json or csv file.
```
ghdorker -s user dtaivpp -d samples/dorks.yaml --options all.cloud.aws all.test -o output.json
```
This is always output to the console:
```
2021-11-18 06:47:57,847 - dork: rds.amazonaws.com password user:dtaivpp, repository: dtaivpp/gh-dorker, path: samples/dorks.yaml, score: 1.0
2021-11-18 06:47:57,848 - dork: rds.amazonaws.com password user:dtaivpp, repository: dtaivpp/gh-dorker, path: README.md, score: 1.0
2021-11-18 06:48:05,171 - dork: extension:md user:dtaivpp, repository: dtaivpp/dtaivpp, path: README.md, score: 1.0
2021-11-18 06:48:05,172 - dork: extension:md user:dtaivpp, repository: dtaivpp/gh-dorker, path: CONTRIBUTING.md, score: 1.0
2021-11-18 06:48:05,172 - dork: extension:md user:dtaivpp, repository: dtaivpp/gh-dorker, path: README.md, score: 1.0
2021-11-18 06:48:05,172 - dork: extension:md user:dtaivpp, repository: dtaivpp/OpenSearch-Utilization, path: README.md, score: 1.0
2021-11-18 06:48:05,172 - dork: extension:md user:dtaivpp, repository: dtaivpp/DevOps-Template, path: README.md, score: 1.0
```

And in addition here is what it looks like as JSON:
```json
[
    {
        "dork": "rds.amazonaws.com password user:dtaivpp",
        "repository": "dtaivpp/gh-dorker",
        "path": "samples/dorks.yaml",
        "score": 1.0
    },
    {
        "dork": "rds.amazonaws.com password user:dtaivpp",
        "repository": "dtaivpp/gh-dorker",
        "path": "README.md",
        "score": 1.0
    },
    {
        "dork": "extension:md user:dtaivpp",
        "repository": "dtaivpp/dtaivpp",
        "path": "README.md",
        "score": 1.0
    },
    {
        "dork": "extension:md user:dtaivpp",
        "repository": "dtaivpp/gh-dorker",
        "path": "CONTRIBUTING.md",
        "score": 1.0
    },
    {
        "dork": "extension:md user:dtaivpp",
        "repository": "dtaivpp/gh-dorker",
        "path": "README.md",
        "score": 1.0
    }
]
```

As an aside, rate limiting is already built into the codebase. It will not allow you to make more requests than allowable. GH-Dorker grabs your real rate limits live from GitHub so it will make the maximim amount of requests permittable in a given timeframe.

## Contributing

For how to contribute please see [CONTRIBUTING.md]("CONTRIBUTING.md").


## Credits
Reference points for creating GitDorker and compiling dorks lists

- [@techgaun](https://github.com/techgaun/github-dorks) - This was the primary repo I was looking to for inspiration when writing this dorker
- [@obheda12](https://github.com/obheda12/GitDorker) - You have one of the cleanest README's ive read in a while and if you couldn't tell has inspired much of this project's structure
-->
