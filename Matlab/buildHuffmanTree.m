function root = buildHuffmanTree(symbols, values, base)
    nodes = cell(1, numel(symbols));

    for x = 1:numel(symbols)
        nodes{x} = Node(values(x), symbols{x}, {});
    end

    while numel(nodes) > 1
        [~, idx] = sort(cellfun(@(n) n.Value, nodes), 'ascend');
        children = nodes(idx(1:min(base, numel(nodes))));

        mergedSymbol = '';
        for i = 1:numel(children)
            mergedSymbol = strcat(mergedSymbol, children{i}.Symbol);
        end

        mergedNode = Node(sum(cellfun(@(n) n.Value, children)), mergedSymbol, children);
        nodes(idx(1:min(base, numel(nodes)))) = [];
        nodes{end+1} = mergedNode;
    end

    root = nodes{1};
end
