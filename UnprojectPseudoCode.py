UVL: CHW (UVL)
I: CHW (RGB)
OUT: LC,OH,OW


# IH, IW = (input height, input width)
# OH, OW = (output height, output width)
# NL = (number of labels aka number of textures)

#Assume the image's values and UVL values range between 0 and 1.
IH,IW=256,256 #During training, the algorithm is fed 256x256 croppings
OH,OW=128,128 #Make the output height smaller so the bins are more contiguous
NL=4 #In the main diagram, we use four textures and therefore four labels

def unproject(UVL,I,L:int):
	#L is a particular label, this function only calculates it for that label?
	assert UVL.shape==IH,IW,3
	assert   I.shape==IH,IW,NC

	OUT=[[[] for x in range(OW)] for y in range(OH)]

	for iy in range(IH):
		for ix in range(IW):
			u,v,l=UVL[iy][ix]
			if l==L:
				ox=floor(u*OH)
				oy=floor(v*OW)
				OUT[ox][oy].append(I[ix][iy])

	OUT=[[mean(OUT[x][y]) for x in range(OW)] for y in range(OH)]
