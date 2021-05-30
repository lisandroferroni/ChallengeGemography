from flask import Flask, jsonify

from Challenge.API.RepoService import RepoService

app = Flask(__name__)
service = RepoService()


@app.route("/repositories", methods=['GET'])
def getRepos():
    return jsonify(service.GetRepos(False))


@app.route("/repositories-summary", methods=['GET'])
def getReposSummary():
    return jsonify(service.GetRepos(True))


if __name__ == '__main__':
    app.run()



