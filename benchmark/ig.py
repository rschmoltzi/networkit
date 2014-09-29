try:
	import igraph
except ImportError:
	error("igraph not available")
	

class Algo:
	""" runner for an algorithm"""
	def run(self, G):
		raise Exception("Not implemented")

	def loadGraph(key, basePath):
		raise NotImplementedError("TODO")

class bConnectedComponents(Algo):
	name = "ConnectedComponents"

	def run(self, G):
		c = igraph.Graph.components(G)

# - k-core decomposition (properties.CoreDecomposition)

class bCoreDecomposition(Algo):
name = "CoreDecomposition"

def run(self, G):
	igraph.Graph.coreness(G)

# - degree distribution power-law estimation (properties.powerLawExponent)

class bPowerLaw(Algo):
name = "PowerLaw"

def run(self, G):
	raise NotImplementedError("TODO")

# - degree assortativity (properties.degreeAssortativity)

class bDegreeAssortativity(Algo):
name = "DegreeAssortativity"

def run(self, G):
	raise NotImplementedError("TODO")


# - BFS & Dijkstra (graph.BFS, graph.Dijkstra)
class bBFS(Algo):
name = "BFS"

def run(self, G):
	raise NotImplementedError("TODO")


# - community detection (community.PLM, community.PLP)

class bCommunityDetection(Algo):
name = "CommunityDetection"

def run(self, G):
	raise NotImplementedError("TODO")

# - diameter, exact (properties.Diameter.exactDiameter) and estimate (properties.Diameter.estimatedDiameterRange)

class bDiameter(Algo):
name = "Diameter"

def run(self, G):
	raise NotImplementedError("TODO")


class bDiameterEstimate(Algo):
name = "Diameter"

def run(self, G):
	raise NotImplementedError("TODO")

# - clustering coefficients (average local), exact (properties.ClusteringCoefficient.avgLocal) and approximated (properties.ClusteringCoefficient.approxAvgLocal)

class bClusteringCoefficient(Algo):
name = "ClusteringCoefficient"

def run(self, G):
	raise NotImplementedError("TODO")

class bApproxClusteringCoefficient(Algo):
name = "ApproxClusteringCoefficient"

def run(self, G):
	# TODO: specify number of trials
	raise NotImplementedError("TODO")



# - centrality

# 	- PageRank (centrality.PageRank, centrality.SciPyPageRank)

class bPageRank(Algo):
name = "PageRank"

def run(self, G):
	raise NotImplementedError("TODO")

# 	- Eigenvector centrality (centrality.EigenvectorCentrality, centrality.SciPyEVZ)


# 	- betweenness,  exact (centrality.Betweenness) and approximated (centrality.ApproxBetweenness, centrality.ApproxBetweenness2)

class bBetweenness(Algo):
name = "Betweenness"

def run(self, G):
	raise NotImplementedError("TODO")

class bApproxBetweenness(Algo):
name = "ApproxBetweenness"

def run(self, G):
	raise NotImplementedError("TODO")
