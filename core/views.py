# Create your views here.
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from sgps import GPSFile
from sgps.export.kml import TracksDocument


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            gps = GPSFile.from_file(request.FILES['file'])
            trackskml = TracksDocument(gps.tracks)
            trackskml_src = trackskml.render_xml()
            response = HttpResponse(mimetype='application/vnd.google-earth.kml+xml')
            response['Content-Disposition'] = 'attachment; filename=tracks.kml'
            response.write(trackskml_src)
            return response
    else:
        form = UploadFileForm()
    context['form'] = form
    return render_to_response('upload.html', RequestContext(request, context))