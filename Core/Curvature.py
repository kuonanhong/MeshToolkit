# -*- coding:utf-8 -*- 

# ***************************************************************************
#                                Curvature.py
#                             -------------------
#    update               : 2013-11-20
#    copyright            : (C) 2013 by Michaël Roy
#    email                : microygh@gmail.com
# ***************************************************************************

# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************


#--
#
# Based on :
#
# Discrete Differential-Geometry Operators for Triangulated 2-Manifolds
# Mark Meyer, Mathieu Desbrun, Peter Schröder, Alan H. Barr
# VisMath '02, Berlin (Germany)
#
#--





#-
#
# External dependencies
#
#-
from .Neighbor import IsBorderVertex
from math import sqrt
from numpy import dot, cross, zeros
from numpy.linalg import norm





#--
#
# ComputeNormalCurvature
#
#--
#
# Compute the normal curvature vectors of the mesh
# for every vertex
#
def ComputeNormalCurvature( mesh ) :

	# Initialise normal curvature array
	normal_curvature = zeros( (len(mesh.vertices),3 ) )

	# Loop through the vertices
	for v1 in range( len(mesh.vertices) ) :

		# Check border
		if IsBorderVertex( mesh, v1 ) : continue

		# Get the 1-ring neighborhood
		for v2 in mesh.neighbor_vertices[v1] :

			coef = 0.0

			# Find an edge
			for v3 in mesh.neighbor_vertices[v2] :
#				if edge( v2, v3 ) :
				u = mesh.vertices[v1] - mesh.vertices[v3]
				v = mesh.vertices[v2] - mesh.vertices[v3]
				coef += Cotangent( u, v )
#
#			normal_curvature[v1] += (coef * (mesh.vertices[v1] - mesh.vertices[v2]))


	# Return the normal curvature vector array
	return normal_curvature




#--
#
# Cotangent
#
#--
#
# Cotangent between two vector in nD
# Discrete Differential-Geometry Operators for Triangulated 2-Manifolds
# Mark Meyer, Mathieu Desbrun, Peter Schroder, Alan H. Barr
# VisMath '02, Berlin (Germany)
#
def Cotangent( v1, v2 ) :

	# Compute square length
	l1 = dot( v1, v1 )
	l2 = dot( v2, v2 )

	# Compute scalar product
	dot_prod = dot( v1, v2 )

	# Compute denomination
	denom = l1 * l2 - dot_prod * dot_prod;

	# Return cotangent between v1 and v2
	return dot_prod / sqrt( denom )



