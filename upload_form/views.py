from django.shortcuts import render

def create(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save()

            messages.add_message(request, messages.SUCCESS, "You Upload was added")

            return HttpResponseRedirect('/upload_form/all')
    else:
        form = UploadForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_upload_form.html', args)
