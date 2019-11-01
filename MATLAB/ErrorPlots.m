v = 10:100;

i = zeros(91,1);

i_actual = 14/3 .* ones(91, 1);

for j = 10:100
    i(j-9) = MidpointInt(j);
end
    
hold on

plot(v, i)
plot(v, i_actual)

e = abs(i - i_actual);

% K = -0.0313

eb = zeros(91,1)

for j = 10:100
    eb(j-9) = 27*0.0313/(24*j^2);
end

% TBD ERROR WRONG
hold off
plot(v, e)
hold on
plot(v, eb)

% now for error



