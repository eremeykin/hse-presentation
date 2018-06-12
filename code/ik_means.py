import numpy as np


class IKMeans:
    _MAX_LOOPS = 500

    def __init__(self, cluster_structure):
        self._cs = cluster_structure
        self._data = cluster_structure.data

    @property
    def cluster_structure(self):
        return self._cs

    def __call__(self):
        for loop in range(IKMeans._MAX_LOOPS):
            clusters = self._cs.clusters
            cluster_points = {cluster: [] for cluster in clusters}
            for index, point in enumerate(self._data):
                nearest_cluster = min(clusters, key= |\label{line:nearest-cluster}|  
                lambda c: self._cs.dist_point_to_cluster(point, c))
                cluster_points[nearest_cluster].append(index)
            new_clusters = self._cs.release_new_batch( |\label{line:new-clusters}|  
                [np.array(x) for x in cluster_points.values()])
            if set(new_clusters) == set(clusters):  # stop condition
                break
            self._cs.clear()
            self._cs.add_all_clusters(set(new_clusters))
        return self.cluster_structure.current_labels()
