% MATLAB Lab 1 Activity 1
% Mingde Yin
% November 1, 2019

% actual answer should be 14/3 = around 4.667

function result = MidpointInt(n)
    % splits interval from 0 to 3 into n equal partitions and returns
    % integral found by midpoint approximation

    % declare x0 and x1; the lower and upper bound of each partition
    % respectively
    dx = 3/n;
    
    x0 = 0:dx:3-dx; % produces array of lower bounds
    x1 = x0+dx; % add dx to each lower bound to get an upper bound
    
    xbar = (x0+x1)/2; % find midpoints of partitions
    
    s = (sqrt(xbar + 1)).*dx;
    
    result = sum(s);
    
end