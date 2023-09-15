classdef Node < handle
    properties
        Value     % Value can be any base (e.g., 2, 3, 4, ...)
        Symbol    % Symbol name (character)
        Children  % List of node children
        Huff      % Tree direction (0, 1, 2, ...)
    end

    methods
        function obj = Node(value, symbol, children)
            obj.Value = value;
            obj.Symbol = symbol;
            obj.Children = children;
            obj.Huff = '';
        end

        function result = lt(obj, nxt)
            result = obj.Value < nxt.Value;
        end
    end
end
