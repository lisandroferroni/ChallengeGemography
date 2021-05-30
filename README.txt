In order to run the app correctly, run the __init__.py python file and then there will be 2 endpoints available, /repositories and /repositories-summary. Each will return a list of the languages used by the 100 trending public repos on GitHub from the last 30 days. I decided to add a summary endpoint to shorten the response and be able to inspect correctly the result

- [localhost url]/repositories
  Is a GET, and a return example could be:
    {
      [
        "language name": {
          "count" : integer,  #count of repos for this language
          "repos" : [ repo ]  #list of repos with ALL attributes from github API
        }
      ]
    }

- [localhosturl]/repositories-summary
Is a GET, and a return example could be:
    {
      [
        "language name": {
          "count" : integer,  #count of repos for this language
          "repos" : [         #list of id, url and name of the repos
            "id" : integer,
            "name" : string,
            "url" : string
          ]
        }
      ]
    }
    
