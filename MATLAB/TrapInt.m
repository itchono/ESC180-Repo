% MATLAB Lab 1 Activity 2
% Mingde Yin
% November 1, 2019

% actual answer should be 14/3 = around 4.667

function result = TrapInt(n)
    % splits interval from 0 to 3 into n equal partitions and returns
    % integral found by midpoint approximation

    % declare x0 and x1; the lower and upper bound of each partition
    % respectively
    dx = 3/n;
    
    x0 = 0:dx:3-dx; % produces array of lower bounds
    x1 = x0+dx; % add dx to each lower bound to get an upper bound
    
    f0 = sqrt(x0+1);
    f1 = sqrt(x1+1);
    % compute function values at upper and lower bounds
    
    s = (f0+f1)/2.*dx;
    
    result = sum(s);
end