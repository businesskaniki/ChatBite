def get_redirect_if_exist(request):
	redirect = None
	if request.GET:
		if request.GET.get('next'):
			destination_string = request.GET.get('next')
			redirect = str(destination_string)
	return redirect