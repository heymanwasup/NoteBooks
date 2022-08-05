#!/usr/bin/env python
# coding: utf-8

# In[15]:


from imp import reload
import ROOT as R
import tools
import os
import sys
import json
reload(tools)

R.gStyle.SetErrorX(0)
R.gStyle.SetPaintTextFormat('4.1f m');

from tools import DrawSensitivity
from tools import CmpSensitivity
from tools import CmpSensitivityX

R.gROOT.SetBatch(1)

DrawSensitivity = tools.DrawSensitivity




def get_all_results():
    tools.version = 'FullRun2'
    tools.dataset = 'Run2%s'%(sys.argv[1])

    tools.isSave = True
    tools.saveDir = './plots/%s_%s/'%(tools.version,tools.dataset)
    os.system('mkdir -p %s'%(tools.saveDir))

    results = {}

    for method in ['A','T']:
        for syst in ['gain_A','gain_T','stdp_A','stdp_T']:
            results['%s_%s'%(method,syst)] = DrawSensitivity(method,syst,[0.5,1.5])[0]

    tools.results = results

    # CmpSensitivity('A')
    # CmpSensitivity('T')
    CmpSensitivityX()

    os.system('mkdir -p results')
    with open('results/%s.json'%(tools.dataset),'w') as f:
        json.dump(results, f,indent=4,sort_keys=True)


def main():
    
    tools.dataset = '%s'%(sys.argv[1])
    method = sys.argv[2]
    syst = sys.argv[3]
    tools.version = sys.argv[4]

    tools.isSave = True
    tools.saveDir = './NoteBooks/plots/%s_%s/'%(tools.version,tools.dataset)
    os.system('mkdir -p %s'%(tools.saveDir))

    results = {}    
    results['%s_%s'%(method,syst)] = DrawSensitivity(method,syst,[0.5,1.5])[0]

    

    
    

    

if __name__ == '__main__':

    main()