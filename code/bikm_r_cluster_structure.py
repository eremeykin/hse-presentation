    def find_best_cluster(self):
        best = None
        max_eps_k = 0
        for cluster in self._clusters:
            if cluster in self.forbid_split:
                continue
            directions = 
                cluster.gen_directions(self._directions_num, 
                                       self._mean, self._cov)
            dirs_with_min = self._count_directions_with_min(directions)
            eps_k = dirs_with_min / self._directions_num
            if eps_k < self._epsilon and not self._second_chance:
                self.forbid_split.append(cluster)
            elif eps_k >= max_eps_k:
                best = cluster
                max_eps_k = eps_k
        return best

    def split(self, cluster):
        self.del_cluster(cluster)
        first, second = 
            self._run_bisecting_ap_clustering(cluster.cluster_points)
        index = np.arange(cluster.power, dtype=int)
        left = cluster.points_indices[first]
        right = cluster.points_indices[second]
        left_cluster = 
            BiKMeansRClusterStructure.release_new_cluster(self, left)
        right_cluster = 
            BiKMeansRClusterStructure.release_new_cluster(self, right)
        self.add_cluster(left_cluster)
        self.add_cluster(right_cluster)
        return left_cluster, right_cluster