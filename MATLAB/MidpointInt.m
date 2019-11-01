% MATLAB Lab 1 Act. 1
% Mingde Yin
% November 1, 2019

% actual answer should be 14/3 = around 4.667

function result = MidpointInt(n)
    dx = 3/n;
    
    result = 0;
    
    for i = 1:n
        % use midpoint approximation
        result = result + sqrt((dx*(i-1) + dx*i)/2 + 1)*dx;
    end
end