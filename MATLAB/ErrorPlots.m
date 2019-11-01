% MATLAB Lab 1 Activity 1 and 2 Plots
% Mingde Yin
% November 1, 2019

n = 10:100; % values of n

i = arrayfun(@MidpointInt, n); % computed integral values

i_actual = ones(1, 91) .* 14/3; % actual integral values

hold on
% plot integral vs actual

plot(n, i, 'b--', n, i_actual, 'b');
title('$$ \textup{Midpoint Approximation of}\  \int_{0}^{3}\sqrt{x+1} \ dx $$', 'Interpreter', 'latex');
xlabel('Number of subdivisions (n)')
ylabel('Approximation')
legend('approximate value', 'exact value')
axis([0 100 0 inf])
axis 'auto y'

% second plot
hold off

% compute error function based on definition
err = abs(14/3 - i);

% based on second derivative, least upper bound over [0,3] is -1/32

errbound = 1./n.^2 .* 27/32;
% must be positive? not sure

plot(n, err, 'b', n, errbound, 'b--');
title('$$ \textup{Error Bound vs Actual Error} $$', 'Interpreter', 'latex');
xlabel('Number of subdivisions (n)')
ylabel('Error')
legend('actual error', 'error bound')
axis([0 100 0 inf])
axis 'auto y'



