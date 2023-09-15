function printNodes(node, val)
    newVal = strcat(val, num2str(node.Huff));

    if ~isempty(node.Children)
        for i = 1:numel(node.Children)
            node.Children{i}.Huff = i - 1;
            printNodes(node.Children{i}, newVal);
        end
    else
        fprintf('%s -> %s\n', node.Symbol, newVal);
    end
end