#include<iostream>
using namespace std;

double slope(int n,double x[],double y[],double xbar){
    double numr=0,denr=0;
    for(int i=0;i<n;i++){
        numr+=(x[i]-xbar)*y[i];
        denr+=(x[i]-xbar)*(x[i]-xbar);
    }
    return(numr/denr);
}

int main(){
    int n;
    cout<<"n = ";
    cin>>n;
    double x[n],y[n],xsum=0,ysum=0,xbar,ybar,m,c;
    cout<<"\nx values : ";
    for(int i=0;i<n;i++){ cin>>x[i]; xsum+=x[i];}
    cout<<"\ny values : ";
    for(int i=0;i<n;i++){ cin>>y[i]; ysum+=y[i];}
    xbar=xsum/n;
    ybar=ysum/n;
    m=slope(n,x,y,xbar);
    c=ybar-xbar*m;
    cout<<"\n\nm = "<<m<<endl;
    cout<<"c = "<<c;

    cout<<"\ny at x=0.12 is = "<<m*0.12+c;
}
