def __call__(self, ax):
    stack = [] |\label{line:nnc-stack}|
    while self._cs.clusters_number > 1:
        if not stack:
            arbitrary_cluster = next(iter(self._cs.clusters)) |\label{line:nnc-next}|
            stack.append(arbitrary_cluster)
        top = stack[-1]
        nearest, dist = self._find_nearest(top)
        if nearest is None: |\label{line:nnc-break}|
            break
        if nearest in stack:
            merged = self._cs.merge(top, nearest)
            self._merge_array.append([top, nearest, merged, dist])
            stack.remove(top)
            stack.remove(nearest)
        else:
            stack.append(nearest)
    # sort merge_array by distance
    self._merge_array.sort(key=lambda elem: elem[-1]) |\label{line:nnc-sort}|
    return self._merge_array
