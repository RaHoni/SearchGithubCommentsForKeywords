# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Repo: str = "linux-surface/linux-surface"
issueNumber: int = 91
keywords = ["v4l2loopback", "gst-launch-1.0"]

from github import Github

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    keywords = [x.lower() for x in keywords]
    git = Github(per_page=100)
    repo = git.get_repo(Repo)
    issue = repo.get_issue(issueNumber)
    for comment in issue.get_comments():
        if any([x in comment.body.lower() for x in keywords]):
            print(comment.html_url + ": " + comment.body)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
