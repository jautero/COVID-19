import git, glob, covid19

def update_data(repo):
    cmd=repo.git()
    cmd.pull('upstream','master')
    cmd.push()
    create_list("peaked.md")
    repo.index.add("peaked.md")
    repo.git.commit('-m',"Updated 'peaked.md'.")

def update_docs(repo):
    covid19.create_topchart_files("docs")
    repo.index.add(glob.glob("docs/*.png"))
    repo.git.commit('-m',"Updated images in docs/")
    repo.git.push()

def create_list(filename):
    df=covid19.get_data('infected',False)
    countrylist=covid19.peaked_countries(df)
    newfile=open(filename,"w")
    newfile.writelines(map(lambda x: "# {0:s}\n".format(x),countrylist))
    newfile.close()

if __name__ == '__main__':
    repo=git.Repo(".")
    update_data(repo)
    update_docs(repo)
