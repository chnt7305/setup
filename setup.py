#-*-coding:utf-8 -*-
#本程序旨在将Python脚本编译成exe可执行文件
from distutils.core import setup
import py2exe
import sys
import os

sys.argv.append('py2exe')

setup(
		options = {'py2exe':{'bundle_files':1}},	#如果bundle_files不为1、2，则dist文件夹中还会包括一些dll文件和pyd文件（Python Dll文件）。如果bundle_files为2，dist文件夹会包括一个python##.dll文件，如果为1则不会。
		console = ["XXX.py"],		#XXX.py是要编译的目标文件
		zipfile = None
		)
		
