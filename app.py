import os

from bottle import static_file, route, run, view, template, post, get, request

# Storing the current wavelength information per channel
wavelen = {}

@route('/')
def main():
    return template('main')

@route('/static/<path:path>')
def callback(path):
    return static_file(path,  root='./static/')


####################
# API implementation
####################

@get('/api/wavelength')
@get('/api/wavelength/')
@get('/api/wavelength/<channel>')
def getwavelength(channel=None):
    if channel is None:
        channel = wavelen.keys()
    chdata = []
    for ch in channel:
        if ch in wavelen:
            chdata += [{'channel': ch, "wavelength": wavelen[ch]}]
    count = len(chdata)
    if count > 0:
        if count == len(channel):
            status = 'okay'
        else:
            status = 'partial data'
    else:
        status = 'no data to display'
    return {'status': status, 'count': count, 'channels': chdata}

@post('/api/wavelength/<channel>')
def setwavelength(channel=None):
    value = request.forms.get('wavelength', None)
    if channel is None:
        status = "error, no channel set"
    elif value is None:
        status = "error, no value set"
    else:
        wavelen[channel] = value
        status = "okay, data set"
    return {'status': status}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(host='0.0.0.0', port=port)
