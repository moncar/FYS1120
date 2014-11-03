h = linspace(0, 0.1, 11); %M
a = 4*10^-2; %M
t = 9.78*10^-3; %M
I = 5 % A
B = [2.8, 2.0, 1.5, 1.1, 0.9, 0.6, 0.4, 0.3, 0.2, 0.1, 0.0]*10^-3;
L = 275*10^-3 %M
N = 244; %Antall viklinger

p = polyfit(h,B,6);

x1 = linspace(0,0.1, 100);
y1 = polyval(p,x1);

j = N*I/L;
my0 = 4*pi*10^-7; %Tm/A
my0*j
Bx = j*my0/2*((h + t)./(sqrt((h + t).^2 + a^2)) - h./sqrt(h.^2 + a^2));

B./Bx



plot(h,B,'o')
hold on
plot(x1,y1)
plot(h, Bx, 'x')
title('Sylindrisk elektromagnet')
xlabel('h-verdier [m]')
ylabel('B-verdier [T]')
legend('Maalepunkter', 'Tilpasset kurve', 'Teoretisk kurve')
print('-dpdf', 'Oppgave3')
hold off
