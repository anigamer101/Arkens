import git
REPO = "https://github.com/anigamer101/Arkens"
PATH = "C:/Users/admin/Desktop/Parental%15Controls/Tokens"
repo = git.Repo.clone_from(REPO, PATH)
print("Done")