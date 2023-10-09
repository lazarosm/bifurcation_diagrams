clear
%initial condition
x(1)=0.111; 
% parameter interval
k_min=3;
k_max=4;
%iteration step
t=0.001;
k_interval=k_min:t:k_max;
pos=0; %internal variable for position counting
%iteration parameters
N=1.5*10^4+150;
m=1.5*10^4;
%Number of intervals and bars
B=1000;
S_low=0;
S_up=1;
spaces=linspace(S_low,S_up,B);
%Set colormap range
F=(5/B)*100;

for k=k_interval
    pos=pos+1;
    for i=2:N
        x(i)=k*x(i-1)*(1-x(i-1));
    end
    %Compute frequency for each interval
    freq(:,pos)=hist(x(end-m+1:end),spaces);
end

%plot the diagram
hold all
[X,Y]=meshgrid(k_interval,spaces);
freq_per=100*freq/m; %frequency percentage
surf(X,Y,freq_per,'EdgeColor','interp','FaceColor','none');
view(0,90)
%define colormap
mymap = [0,0,0;parula(B-1)];
colormap(mymap)
cbh=colorbar;
caxis([0,F])
set(cbh,'XTick',0:0.1:F)
cbh.XTickLabel{end}=['\geq ' num2str(F) '%'];
xlabel('k')
ylabel('x')
set(gca,'fontsize',12)
set(gca,'fontweight','bold')