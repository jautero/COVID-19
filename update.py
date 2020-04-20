import git
import covid19

def update_data(repo):
    cmd=repo.git()
    cmd.pull("--rebase",'upstream','master')
    cmd.push()

if __name__ == '__main__':
    repo=git.Repo(".")
    update_data(repo)
