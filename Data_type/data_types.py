
def data_type(data):
	if data is None:
		return 'no value'
	elif type(data) == list:
		if len(data) >= 3:
			return data[2]
		else:
			return None
	else:
		pass