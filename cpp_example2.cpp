#include "TApplication.h"
#include "TROOT.h"
#include "TH2F.h"
#include "TCanvas.h"
#include "TRandom3.h"
#include "TStyle.h"
#include <iostream>

using namespace std;

void cpp_example2(int samples=10000){

    auto tr = new TRandom3();

    // Panel 1: Original 2D Gaussian
    auto hist1 = new TH2F("hist1","2D Gaussian;x;y",100,50,150,100,50,150);
    for(int i=0;i<samples;i++){
        hist1->Fill(tr->Gaus(100,6), tr->Gaus(100,6));
    }

    // Panel 2: Gaussian + Uniform
    auto hist2 = (TH2F*) hist1->Clone("hist2");
    hist2->SetTitle("2D Gaussian + Uniform;x;y");
    for(int i=0;i<samples/3;i++){
        hist2->Fill(tr->Uniform(50,150), tr->Uniform(50,150));
    }

    // Panel 3: Gaussian + 1/(x*y)^2 baseline
    auto hist3 = (TH2F*) hist1->Clone("hist3");
    hist3->SetTitle("2D Gaussian + 1/(x*y)^2;x;y");
    for(int i=0;i<samples*30;i++){
        double x = 40 + 10/tr->Uniform(0.0001,1.0); // avoid divide by zero
        double y = 40 + 10/tr->Uniform(0.0001,1.0);
        hist3->Fill(x,y);
    }

    // Panel 4: Double Gaussian
    auto hist4 = (TH2F*) hist1->Clone("hist4");
    hist4->SetTitle("Double 2D Gaussian;x;y");
    for(int i=0;i<samples/2;i++){
        hist4->Fill(tr->Gaus(100,20), tr->Gaus(100,20));
    }

    // Create canvas with 2x2 pads
    auto c2 = new TCanvas("c2","Canvas2D",1200,1000);
    c2->Divide(2,2);

    c2->cd(1); hist1->Draw("COLZ");
    c2->cd(2); hist2->Draw("COLZ");
    c2->cd(3); hist3->Draw("COLZ"); gPad->SetLogz();
    c2->cd(4); hist4->Draw("COLZ");

    c2->Update();
    c2->SaveAs("canvas2d_cpp.png");
}

int main(int argc, char **argv){
    TApplication theApp("App",&argc,argv);
    cpp_example2();
    theApp.Run();
    return 0;
}

