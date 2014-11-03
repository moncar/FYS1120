h = linspace(0, 0.1, 11);
a = 34.77/2*10^-3;
t = 9.78*10^-3;

B = [278, 111.6, 50.9, 24.9, 14.6, 10, 7.1, 5.2, 4, 3.1, 2.7]*10^-3;


p = polyfit(h,B,6);

x1 = linspace(0,0.1, 100);
y1 = polyval(p,x1);

my0j = 278*10^-3*2/(t/(sqrt(t^2 + a^2)));
%my0 = 4*pi*10^-7; %Tm/A
Bx = my0j/2*((h + t)./(sqrt((h + t).^2 + a^2)) - h./sqrt(h.^2 + a^2));



plot(h,B,'o')

hold on
plot(x1,y1)
plot(h, Bx, 'x')
title('Permanent magnet')
xlabel('h-verdier [m]')
ylabel('B-verdier [T]')
legend('Maalepunkter', 'Tilpasset kurve', 'Teoretisk kurve')
print('-dpdf', 'Oppgave21')
hold off
