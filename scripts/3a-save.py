#!/usr/bin/python36
# 3a-save
# backup de dossier
# 10/11
# Le Cossec


import filecmp
from shutil import make_archive
import signal
import gzip
import os
import sys
import datetime
import shutil

to_save_path = '/root/B2-Python'
nom_archive = 'backup'
arch = nom_archive + '.tar.gz'
direc_save = 'data/'
full_archive_path = direc_save + arch

def saveDirectory(to_save, archive_name):
  make_archive(nom_archive, 'gztar', to_save)

def checkMoveFile():
  if checkExistingArchive() == True:
    same_file = filecmp.cmp(arch, full_archive_path)
    if(same_file == False):
      os.remove(full_archive_path)
      moveArchiveTo(arch, direc_save)
    else:
      os.remove(arch)
  else:
    moveArchiveTo(arch, direc_save)

def checkExistingArchive():
  if (os.path.exists(full_archive_path)):
    return True
  else:
    return False

def moveArchiveTo(archive_file, backup_direcoty):
  shutil.move(archive_file, direc_save)

try:
  saveDirectory(to_save_path, nom_archive)
  checkMoveFile()
  sys.stdout.write('sauvegardé dans ' + direc_save )
except Exception as a:
  sys.stderr.write(str(e) + '\n')
