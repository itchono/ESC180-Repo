v = 10:100;

i = zeros(91,1);

i_actual = 14/3 .* ones(91, 1);

for j = 10:100
    i(j-9) = NumericIntegration(j);
end
    
hold on

plot(v, i)
plot(v, i_actual)

% now for error



