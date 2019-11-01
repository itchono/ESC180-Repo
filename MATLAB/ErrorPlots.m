% MATLAB Lab 1 Activity 1 and 2 Plots
% Mingde Yin
% November 1, 2019

n = 10:100; % values of n

im = arrayfun(@MidpointInt, n); % computed integral values

i_actual = ones(1, 91) .* 14/3; % actual integral values

figure('Name', 'Midpoint')
% plot integral vs actual

plot(n, im, 'b--', n, i_actual, 'b');
title('$$ \textup{Midpoint Approximation of}\  \int_{0}^{3}\sqrt{x+1} \ dx $$', 'Interpreter', 'latex');
xlabel('Number of subdivisions (n)')
ylabel('Approximation')
legend('approximate value', 'exact value')
axis([0 100 0 inf])
axis 'auto y'

% second plot
figure('Name', 'Error for Midpoint')
% compute error function based on definition
err = abs(14/3 - im);

% based on second derivative, least upper bound of abs(f''(x)) over [0,3]
% is 1/4

errbound = 27./(24*n.^2) .* 1/4;
% must be positive? not sure

plot(n, err, 'b', n, errbound, 'b--');
title('$$ \textup{Error Bound vs Actual Error} $$', 'Interpreter', 'latex');
xlabel('Number of subdivisions (n)')
ylabel('Error')
legend('actual error', 'error bound')
axis([0 100 0 inf])
axis 'auto y'

% next, trapezoid
it = arrayfun(@TrapInt, n); % computed integral values

figure('Name', 'Trapezoidal')
% plot integral vs actual

plot(n, it, 'b--', n, i_actual, 'b');
title('$$ \textup{Trapezoidal Approximation of}\  \int_{0}^{3}\sqrt{x+1} \ dx $$', 'Interpreter', 'latex');
xlabel('Number of subdivisions (n)')
ylabel('Approximation')
legend('approximate value', 'exact value')
axis([0 100 0 inf])
axis 'auto y'

err = abs(14/3 - it);
% change error bound
errbound = 27./(12*n.^2) .* 1/4;

figure('Name', 'Error for Trapezoidal')

plot(n, err, 'b', n, errbound, 'b--');
title('$$ \textup{Error Bound vs Actual Error} $$', 'Interpreter', 'latex');
xlabel('Number of subdivisions (n)')
ylabel('Error')
legend('actual error', 'error bound')
axis([0 100 0 inf])
axis 'auto y'


