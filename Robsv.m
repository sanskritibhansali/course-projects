clc
clear

tf = 150;
h = 0.001;
t = linspace(0,tf,tf/h)';
N = length(t);

kp = 1;
ki = 0.1;

freq = 1; 
afreq = 2*pi*freq;
th = sin(afreq*t);
th_d = afreq*cos(afreq*t);
ax = [1;0;0];

eta = 5*pi/180*2*(rand(3,length(th))-0.5);
I3 = eye(3);

R = zeros(3,3,N); omg = zeros(3,N);
R(:,:,1) = I3;
Rm = R; omgm = omg;
R_est = R; omg_est = omg; omgb_est = omg;
omgb = [0.03; 0.01; 0.02];
eul_est = zeros(3,N);
eul_m = eul_est;
eul = eul_est;

for i = 2:N
    R(:,:,i) = I3 + hat(ax)*sin(th(i)) + hat(ax)*hat(ax)*(1-cos(th(i)));
    omg(:,i) = ax*th_d(i);
    Rm(:,:,i) = R(:,:,i)*expm(hat(eta(:,i)));
    omgm(:,i) = omg(:,i) + omgb;
    
    Rm1 = Rm(:,:,i);
    
    Re = Rm1'*R_est(:,:,i-1);
    eR = vee((Re - Re')/2);
    
    omgb_est(:,i) = omgb_est(:,i-1) - h*ki*eR;
    omg_est(:,i) = omgm(:,i) + omgb_est(:,i);
    R_est(:,:,i) = R_est(:,:,i-1)*expm(h*hat(omg_est(:,i) - kp*eR));
    
    eul_est(:,i) = rotm2eul(R_est(:,:,i));
    eul_m(:,i) = rotm2eul(Rm(:,:,i));
    eul(:,i) = rotm2eul(R(:,:,i));
    
end


figure; plot(t,eul_m); hold on; plot(t,eul_est,'LineWidth',2); grid on;
figure; plot(t,omg); hold on; plot(t,omg_est,'LineWidth',2); grid on;