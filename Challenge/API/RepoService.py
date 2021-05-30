import requests
import datetime


class RepoService (object):
    def __init__(self):
        pass

    @staticmethod
    def GetRepos(isSummary):
        response = {}
        totalReposCount = 0
        page = 1
        date = datetime.date.today() + datetime.timedelta(days=-30)

        while totalReposCount < 100:
            url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page={1}".format(str(date), page)
            repositories = requests.get(url).json()

            for repo in repositories['items']:
                # If the repo does not have a valid language name, it will not be on the response
                if not isinstance(repo['language'], str):
                    continue

                if repo['language'] not in response.keys():
                    response[repo['language']] = {}
                    response[repo['language']]['count'] = 0
                    response[repo['language']]['repos'] = []

                if isSummary:
                    repoSummary = {}
                    repoSummary['id'] = repo['id']
                    repoSummary['name'] = repo['name']
                    repoSummary['url'] = repo['url']
                    response[repo['language']]['repos'].append(repoSummary)
                else:
                    response[repo['language']]['repos'].append(repo)

                response[repo['language']]['count'] += 1
                totalReposCount += 1
                if totalReposCount == 100:
                    break

            page += 1
        return response
