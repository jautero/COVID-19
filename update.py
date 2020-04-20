import git, glob, covid19

def update_data(repo):
    cmd=repo.git()
    cmd.pull('upstream','master')
    cmd.push()

def update_docs(repo):
    covid19.create_topchart_files("docs")
    repo.index.add(glob.glob("docs/*.png"))
    repo.git.commit('-m',"Updated images in docs/")
    repo.git.push()


if __name__ == '__main__':
    repo=git.Repo(".")
    update_data(repo)
    update_docs(repo)
