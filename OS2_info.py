#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Amer Almadani'
__email__ = 'mad_dev@linuxmail.org'

verion = '0.2'

change_log ='''


2014-08-24

	* removed param from compare arg; empty arg to compare

2014-08-22 

	* added compare class

'''
from fontTools import ttLib
from collections import defaultdict, OrderedDict, Counter
import argparse
import ConfigParser
from os import path, system
import sys


OS2 = [ 'xAvgCharWidth', 
			'usWeightClass',
			'usWidthClass',
			'fsType',
			'ySubscriptXSize',
			'ySubscriptYSize',
			'ySubscriptXOffset',
			'ySubscriptYOffset',
			'ySuperscriptXSize',
			'ySuperscriptYSize',
			'ySuperscriptXOffset',
			'ySuperscriptYOffset',
			'yStrikeoutSize',
			'yStrikeoutPosition',
			'sFamilyClass',
			'ulUnicodeRange1',
			'ulUnicodeRange2',
			'ulUnicodeRange3',
			'ulUnicodeRange4',
			'achVendID',
			'fsSelection',
			'fsFirstCharIndex',
			'fsLastCharIndex',
			'sTypoAscender',
			'sTypoDescender',
			'sTypoLineGap',
			'usWinAscent',
			'usWinDescent'
			]

class GetMetrics:

	def __init__(self, font):
		self.font = font
		self.ttf = ttLib.TTFont(font)

	def metrics(self, cmd):
		'''metrics(cmd) >> return a command;
		   self.ttf['OS/2'].{cmd}'''
		command = []

		for i in OS2:
			if cmd == i:
				out = defaultdict(lambda: OS2, {cmd:i})[cmd]
				fontTools_command = "print '%s =', self.ttf['OS/2'].%s" %(i, out)
				command.append(fontTools_command)

			elif cmd == 'OS/2':
				fontTools_command = "print '%s =', self.ttf['OS/2'].%s" %(i, i)
				command.append(fontTools_command)
		
		return OS2, command
				

	def validate(self, mode, param):
		'''Valid(mode, param) >> exec the command from GetMetrics.metrics(cmd):

		   mode:
		   		all - Return all defined properties(param = None)
		   		singular - Return value of param'''

		if mode == 'all':
			param = None
			a = self.metrics('OS/2')[1]
			for i in a:
				exec i

		elif mode == 'singular':
			a = self.metrics(param)[1]
			for i in a:
				exec i


class Compare:

	def __init__(self, metrics_file):
		self.metrics_file = metrics_file
		self.config = ConfigParser.ConfigParser()

	def readMetrics(self, properties):
		
		values = []
		self.config.read(self.metrics_file)
		section = self.config.sections()
		if properties is not None:
			for i in section:
				values.append(self.config.get(i, properties))
				pass


		return section, values


	def duplicates(self, values):
		'''FIXME if given multi-font metric files and two have an equal value, there is no way to tell which metric file is diff'''
		remove = list(OrderedDict.fromkeys(values))
		if len(remove) > 1:
			print '%s' %remove
		else:
			print 'Values Are Equal\n'
	

if __name__ == '__main__':

	parser = argparse.ArgumentParser(prog=__file__, description='Return OS/2 properties of a given font', 
									 formatter_class=argparse.ArgumentDefaultsHelpFormatter,
									 epilog='''For font list, seperate the paths with ";"
									  e.g OS2_info.py -i "/DroidSansArabic_OLD.otf;/DroidSansArabic.otf" -p achVendID''')
	parser.add_argument('-i', metavar='--input_font', help='Font file', required=False)
	parser.add_argument('-p', metavar='--os2_property', help='Property as per the OS/2 format', default='all')
	parser.add_argument('--compare', action='store_true')

	def operation(font, mode, param):
		OS = GetMetrics(font)
		OS.validate(mode, param)
	file_1 = sys.argv[1]
	file_2 = sys.argv[2]

	def original(file_name, properties, new_value, out_file):
		name = ttLib.TTFont(file_name)
		OS2 = name['OS/2'].__dict__
		OS2[properties] = int(new_value)
		name.save(out_file)

			
	
	if '--compare' in sys.argv:
		compare_file = 'fonts.metrics'
		system("python %s -i '%s %s'" %(__file__, sys.argv[1], sys.argv[2]))
		system("python %s -i '%s %s' >> %s" %(__file__, sys.argv[1], sys.argv[2], compare_file)) 
		c = Compare(compare_file)
			
		for section in c.readMetrics(None)[0]:
			print '%s' %section
		for i in OS2:
			print '%s' %i
			c.duplicates(c.readMetrics(i)[1])
		system('rm %s' %compare_file)

	if '-i' in sys.argv:
		if ' ' in sys.argv[2]:
			font_list = sys.argv[2].split(' ')
			for i in font_list:		
				print '\n[%s]' %i
				operation(i, 'all', None)
				print '\n'

	if '-alt' in sys.argv:
		argv = sys.argv[2:]
		file_name, properties, new_value, out_file = argv
		[original(f, p, n, o) for f, p, n, o in [argv]]
		sys.exit(0)

	if '-p' in sys.argv:
		try:
			argv = sys.argv[2:]
			file_, param = argv
			[operation(f, 'singular', p) for f, p in [argv]]
			
		except ValueError:
			print 'Missing an argument. The correct syntax is\n%s font.ttf param' %__file__

		
	else:
		operation(sys.argv[2], 'all', None)