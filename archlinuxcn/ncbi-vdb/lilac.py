from lilaclib import *

def pre_build():
  update_pkgver_and_pkgrel(_G.newver[0])

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

