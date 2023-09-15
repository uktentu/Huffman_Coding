clc
clear

% Base is for selecting between binary and Terenary
% Example Binary -> 2 & For Terenary -> 3 & for Quternary -> 4 & So.on
base = 2;  % Change to any desired base


% Symbols
symbols = {'a', 'b', 'c', 'd', 'e', 'f'};
values = [0.05, 0.09, 0.12, 0.13, 0.16, 0.45];  % probabilities

% Huffman Tree
root = buildHuffmanTree(symbols, values, base);

% printing final output
fprintf('Symbol\tHuffman Code\n');
printNodes(root, '');