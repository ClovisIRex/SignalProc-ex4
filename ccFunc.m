function [resCC] = ccFunc(vecA, vecB)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
resCC = [];
for m = (length(vecA))-1:-1:(-length(vecB))
    sumM = 0;
    for n = 1:length(vecA)
        if n+m >= 1
            if n+m <= length(vecB)
                
                sumM = sumM + vecA(n) * vecB(n+m);
            end
        end
    end
    resCC = [resCC sumM];
end
resCC(1) = [];
end