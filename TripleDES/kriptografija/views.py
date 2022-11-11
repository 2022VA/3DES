from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def encrypt(request):
    text = request.POST['text']
    key1 = request.POST['key1']
    # TODO šeit jāraksta kods
    res = "Here is the encrypted block, with inputs text:" + text + " and key1:" + key1
    return render(request, 'result.html', {"result": res})

def decrypt(request):
    crtext = request.POST['crtext']
    key1 = request.POST['key1']
    # TODO šeit jāraksta kods
    res = "Here is the decrypted block, with crypted text:" + crtext + " and key1:" + key1
    return render(request, 'result.html', {"result": res})
