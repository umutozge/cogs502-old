def connected(baseset,relation):
	if baseset == []:
		return False 
	else:
		first = baseset[0]
		for x in baseset[1:]:
			if not ([first,x] in relation or [x,first] in relation):
				return False
		return connected(baseset,relation)
