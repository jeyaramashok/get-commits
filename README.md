# get-commits

## Getting Started

```bash
$ git clone https://github.com/jeyaramashok/get-commits.git
$ virtualenv -p python3 venv
$ pip install -r requirements.txt
$ python get_commits.py stable/jenkins --user jeyaramashok --token <personal-access-token> --since 2019-05-01T00:00:00Z
4 new commits.

fix wrong pod selector in jenkins-backup (#13542)
allow templating of customInitContainers (#13536)
fix #13467 (wrong deprecation message) (#13511)
Correct customInitContainers Name example. (#13405)
```