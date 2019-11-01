% MATLAB Lab 1 Act. 2
% Mingde Yin
% November 1, 2019

% actual answer should be 14/3 = around 4.667

function result = TrapInt(n)
    dx = 3/n;
    
    result = 0;
    
    for i = 1:n
        % use trapezoid approximation
        result = result + (sqrt(dx*(i-1) + 1)+sqrt(dx*(i) + 1))/2*dx;
    end
end