import ROOT as R
import os
R.gStyle.SetOptFit(1111)


dataset = 'Run2C' # default dataset
isSave = False


def CmpSensitivity(method):
    nam_map = {
        'gain_A' : 'Gain Amp.',
        'gain_T' : 'Gain #tau',
        'stdp_A' : 'STDP Amp.',
        'stdp_T' : 'STDP #tau',
    }

    c = R.TCanvas()


    sensitivity_cmp = R.TH1D('senesitivity','%s %s-method sensitivity'%(dataset,method),4,0,4)

    n=1
    for syst in ['gain_A','gain_T','stdp_A','stdp_T']:
        sensitivity_cmp.GetXaxis().SetBinLabel(n,nam_map[syst])
        sensitivity_cmp.SetBinContent(n,results['%s_%s'%(method,syst)][0][0])
        sensitivity_cmp.SetBinError(n,0.0001)
        # sensitivity_cmp.SetBinError(n,results['%s_%s'%(method,syst)][0][1])
        n+=1


    sensitivity_cmp.SetLineColor(1)    
    sensitivity_cmp.GetXaxis().SetTitle('Systs')
    sensitivity_cmp.GetYaxis().SetTitle('Sensitivity')

    sensitivity_cmp.GetYaxis().SetRangeUser(-0.1,0.3)
    sensitivity_cmp.GetXaxis().SetRangeUser(0,4)
    # print ('labelSize = ',sensitivity_cmp.GetXaxis().GetLabelSize())
    sensitivity_cmp.GetXaxis().SetLabelSize(0.05)
    sensitivity_cmp.SetStats(0)

    sensitivity_cmp.SetMarkerStyle(8)
    sensitivity_cmp.SetMarkerSize(0.8)
    sensitivity_cmp.SetLineWidth(1)


    sensitivity_cmp.Draw('same')
    c.Draw()
    c.SaveAs('%s/%s_%smethod_sensitivity.png'%(saveDir,dataset,method))

def CmpSensitivityX():
    nam_map = {
        'gain_A' : 'Gain Amp.',
        'gain_T' : 'Gain #tau',
        'stdp_A' : 'STDP Amp.',
        'stdp_T' : 'STDP #tau',
    }

    c = R.TCanvas()
    colors = [R.kBlue,R.kRed]
    leg = R.TLegend(0.6,0.7,0.9,0.9)
    k = 0
    hs = []
    for method in ['A','T']:
        
        sensitivity_cmp = R.TH1D('senesitivity','%s %s-method sensitivity'%(dataset,method),4,0,4)
        hs.append(sensitivity_cmp)

        n=1
        for syst in ['gain_A','gain_T','stdp_A','stdp_T']:
            sensitivity_cmp.GetXaxis().SetBinLabel(n,nam_map[syst])
            sensitivity_cmp.SetBinContent(n,results['%s_%s'%(method,syst)][0][0])
            sensitivity_cmp.SetBinError(n,0.0001)
            # sensitivity_cmp.SetBinError(n,results['%s_%s'%(method,syst)][0][1])
            n+=1

        leg.AddEntry(sensitivity_cmp,'%s-method'%(method),'p')
        sensitivity_cmp.SetLineColor(1)    
        sensitivity_cmp.SetMarkerColor(colors[k])

        sensitivity_cmp.GetXaxis().SetTitle('Systs')
        sensitivity_cmp.GetYaxis().SetTitle('Sensitivity')

        sensitivity_cmp.GetYaxis().SetRangeUser(-0.1,0.3)
        sensitivity_cmp.GetXaxis().SetRangeUser(0,4)
        # print ('labelSize = ',sensitivity_cmp.GetXaxis().GetLabelSize())
        sensitivity_cmp.GetXaxis().SetLabelSize(0.05)
        sensitivity_cmp.SetStats(0)

        sensitivity_cmp.SetMarkerStyle(22+k)
        # sensitivity_cmp.SetMarkerStyle(8)


        sensitivity_cmp.SetMarkerSize(1.5)
        sensitivity_cmp.SetLineWidth(1)


        sensitivity_cmp.Draw('same')
        k+=1
    leg.Draw()
    c.Draw()
    c.SaveAs('%s/%s_sensitivity.png'%(saveDir,dataset,method))    

def CmpSensitivityDataset(version,data,syst):
    nam_map = {
        'gain_A' : 'Gain Amp.',
        'gain_T' : 'Gain #tau',
        'stdp_A' : 'STDP Amp.',
        'stdp_T' : 'STDP #tau',
    }

    c = R.TCanvas()
    colors = [R.kBlue,R.kRed]
    leg2 = R.TLegend(0.57,0.7,0.87,0.87)
    leg = R.TLegend(0.15,0.7,0.45,0.87)
    leg.SetBorderSize(0)
    leg2.SetBorderSize(0)
    k = 0
    hs = []
    lines = []
    for method in ['A','T']:
        res_all = data['All']['%s_%s'%(method,syst)][0][0]
        line = R.TLine(0,res_all,7,res_all)
        # print (res_all)
        line.SetLineColor(colors[k])
        line.SetLineWidth(2)
        lines.append(line)
        line.SetLineStyle(2)
        leg2.AddEntry(line,'Full Run2 (%s)'%(method),'l')
        sensitivity_cmp = R.TH1D('senesitivity%s'%(method),'%s sensitivities'%(nam_map[syst]),7,0,7)
        hs.append(sensitivity_cmp)


        n=1
        for p in ['B','C','D','E','F','G','H']:
            sensitivity_cmp.GetXaxis().SetBinLabel(n,p)
            sensitivity_cmp.SetBinContent(n,data[p]['%s_%s'%(method,syst)][0][0])
            sensitivity_cmp.SetBinError(n,0.0001)
            # sensitivity_cmp.SetBinError(n,results['%s_%s'%(method,syst)][0][1])
            n+=1
        

        
        leg.AddEntry(sensitivity_cmp,'%s-method'%(method),'p')
        
        sensitivity_cmp.SetLineColor(1)    
        sensitivity_cmp.SetMarkerColor(colors[k])

        sensitivity_cmp.GetXaxis().SetTitle('Dataset')
        sensitivity_cmp.GetYaxis().SetTitle('Sensitivity')

        sensitivity_cmp.GetYaxis().SetRangeUser(res_all-0.2,res_all+0.2)
        sensitivity_cmp.GetXaxis().SetRangeUser(0,7)
        # print ('labelSize = ',sensitivity_cmp.GetXaxis().GetLabelSize())
        sensitivity_cmp.GetXaxis().SetLabelSize(0.05)
        sensitivity_cmp.SetStats(0)

        sensitivity_cmp.SetMarkerStyle(22+k)
        # sensitivity_cmp.SetMarkerStyle(8)


        sensitivity_cmp.SetMarkerSize(1.5)
        sensitivity_cmp.SetLineWidth(1)


        sensitivity_cmp.Draw('same')
        k+=1
        

    leg.Draw()
    leg2.Draw()
    lines[0].Draw()
    lines[1].Draw()
    c.Draw()
    c.SaveAs('./plots/Cmp_%s_%s_sensitivities.png'%(version,syst))    
    return c,leg,hs,lines,leg2


def DrawSensitivity(method,syst,range_x):

    nameMap = {
    'gain_A':'IFG amp.',
    'gain_T':'IFG #tau',
    'stdp_A':'STDP amp.',
    'stdp_T':'STDP #tau',
    }
    try:
        fitRes = R.TFile('../output/%s_%smethod_%s_Scan_%s.root'%(dataset,method,syst,version))
    except:
        fitRes = R.TFile('./output/%s_%smethod_%s_Scan_%s.root'%(dataset,method,syst,version))


    R_list = []
    chi2_list = []
    for n in range(20):
        func_name = 'func_28paras_run23_sjtu_%s_%smethod_%s_%s'%(dataset,method,syst,n)
        func = fitRes.Get(func_name)
        R_ = func.GetParameter(3)
        eR_ = func.GetParError(3)
        R_list.append([R_,eR_])
        chi2 = func.GetChisquare()
        ndf = func.GetNDF()
        chi2_list.append(chi2/ndf)


    c = R.TCanvas()

    fit_func = R.TF1('fit_func','[0]+[1]*x',range_x[0],range_x[1]-0.1)
    fit_func.SetParNames('Y-intercept','Sensitivity')
    fit_func.SetLineColor(2)
    fit_func.SetNpx(5000)



    R_graph = R.TGraphErrors()
    range_x_n = [int(range_x[0]/0.1),int(range_x[1]/0.1)]
    for n in range(*range_x_n):
        np = R_graph.GetN()
        # print (np,n*0.1)
        R_graph.SetPoint(np,n*0.1,R_list[n][0])
        R_graph.SetPointError(np,0,R_list[n][1])

    


    R_graph.Fit('fit_func','REMQ')
    r_mean = fit_func.GetParameter(0)
    
    R_graph.SetTitle('%s, %s-method, %s scan;Multiplier;R [ppm]'%(dataset,method,nameMap[syst]))
    R_graph.Draw('AP')
    R_graph.GetYaxis().SetRangeUser(r_mean-4,r_mean+5)
    # print (range_x)
    R_graph.GetXaxis().SetRangeUser(range_x[0]-0.1,range_x[1])
    R_graph.SetMarkerStyle(8)
    R_graph.SetMarkerSize(0.8)
    R_graph.SetLineWidth(1)
    c.Draw()
    if isSave:
        os.system('mkdir -p %s'%(saveDir))
        c.SaveAs('%s/%s_%smethod_%s_sensitivity.png'%(saveDir,dataset,method,syst))

    c2=R.TCanvas()
    chi2_graph = R.TGraph()

    for n in range(*range_x_n):
        chi2_graph.SetPoint(chi2_graph.GetN(),n*0.1,chi2_list[n])
    chi2_graph.SetTitle('%s, %s-method, %s scan;Multiplier;Chi2/NDF'%(dataset,method,nameMap[syst]))
    chi2_graph.Draw('ALP')

    chi2_graph.GetXaxis().SetRangeUser(range_x[0]-0.1,range_x[1])
    chi2_graph.SetMarkerStyle(8)
    chi2_graph.SetMarkerSize(0.8)
    chi2_graph.SetLineWidth(1)


    s = fit_func.GetParameter(1)
    se = fit_func.GetParError(1)


    scan_chi2 = [0.01*n + 0.5 for n in range(100)]
    min_x = 0.5
    min_y = 100
    for x in scan_chi2:
        y = chi2_graph.Eval(x)
        if y < min_y:
            min_y = y
            min_x = x

    chi2_res = 'Chi2 = %s at %s'%(min_y,min_x)
    sen_res  = 'Sensitivity = %s +- %s'%(s,se)
    # print (chi2_res)
    # print (sen_res)    
    c2.Draw()
    if isSave:
        os.system('mkdir -p %s'%(saveDir))
        c2.SaveAs('%s/%s_%smethod_%s_Chi2.png'%(saveDir,dataset,method,syst))

    return [[s,se],[min_y,min_x]],[c,c2],[chi2_graph,R_graph,fit_func,fitRes]