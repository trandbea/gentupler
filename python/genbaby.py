#!/usr/bin/env python

import os, glob

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("model", help = "Model/batch name, used to find input files in hadoop.")
parser.add_argument("--nevents","-n", type = int, help = "Number of events to process", default = -1)
parser.add_argument("--user", "-u", default=os.getenv("USER"))
parser.add_argument("--infiles", "-i", default=os.getenv("input files"))
args = parser.parse_args()

if args.infiles:
    infiles =['file:'+fl for fl in glob.glob(args.infiles)]
else:
    indir = '/hadoop/cms/store/user/'+args.user+'/mcProduction/AODSIM/'+args.model+'/'
    infiles =['file:'+fl for fl in glob.glob(indir+'/*.root')]


cmd = "cmsRun bmaker/python/gen_cfg.py"
cmd += " inputFiles="+','.join(infiles)
cmd += " outputFile=genbaby_"+args.model+".root"
cmd += " nEvents="+str(args.nevents)

print cmd
os.system(cmd)
