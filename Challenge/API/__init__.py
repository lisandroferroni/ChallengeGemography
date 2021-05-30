from flask import Flask, jsonify
import requests
import datetime


app = Flask(__name__)


@app.route("/repositories", methods=['GET'])
def getRepos():
    response = {}
    date = datetime.date.today() + datetime.timedelta(days=-30)
    url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc".format(str(date))
    repositories = requests.get(url).json()

    for repo in repositories['items']:
        # If the repo does not have a valid language name, it will not be on the response
        if not isinstance(repo['language'], str):
            continue

        if repo['language'] not in response.keys():
            response[repo['language']] = {}
            response[repo['language']]['count'] = 0
            response[repo['language']]['repos'] = []

        response[repo['language']]['repos'].append(repo)
        response[repo['language']]['count'] += 1

    return jsonify(response)


if __name__ == '__main__':
    app.run()



