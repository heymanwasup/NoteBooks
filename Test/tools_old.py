import ROOT as R
from array import array
def write():
    f = R.TFile('test.root','recreate')
    numbers = R.TArrayD(10,array('d',[n for n in range(10)]))
    f.WriteObject(numbers,'numbers')
    f.Close()

def read():
    f = R.TFile('test.root')
    numbers = f.Get('numbers')
    print (numbers[1])
    
    # numbers

read()