from django.shortcuts import render, redirect
from .Blockchain import *
from .models import CoinUser
from ellipticcurve.privateKey import PrivateKey

signatureArray = []
messageArray = []

def createUser(request):
    context = {
        "isUserCreated": False,
        "privateKey": 0,
        "publicKey": 0
    }
    if request.method=="POST":
        username = request.POST.get('username')
        message = request.POST.get('message')
        privateKey = CreatePrivateKey()
        publicKey = privateKey.publicKey().toCompressed()

        user = CoinUser(username=username, message=message, privateKey=privateKey.toString(), publicKey=publicKey)
        user.save()

        context['privateKey']=privateKey.toString()
        context['publicKey']=publicKey
        context['isUserCreated']=True

    return render(request, 'home/createUser.html', context)

info = []
def transfer(request):
    global info
    info.clear()

    if request.method=="POST":
        info.append(request.POST.get('amount'))
        info.append(request.POST.get('recpAddress'))
        return redirect('key')

    return render(request, 'home/transfer.html')

def key(request):
    global info
    if request.method=="POST":
        info.append(request.POST.get('privateKey'))

        # print(info)
        if (info[0].isnumeric()):
            sender = CoinUser.objects.get(privateKey=info[2])
            if sender is not None:
                receiver_public_key = info[1]
                messageArray.append(getMessage(sender=sender.username, receiver=receiver_public_key, amount=info[0]))
                signature = getSignature(messageArray[-1], PrivateKey.fromString(info[2]))
                print(signature)
                signatureArray.append(signature)

            return redirect('validate', sender.id)
        return redirect("home")

    return render(request, 'home/key.html')

def validate(request, userID):
    context = {
        'isValidated': False,
        'senderID': userID
    }
    if request.method=="POST":
        
        sender = CoinUser.objects.get(pk=userID)

        if sender is None:
            return redirect('home')

        signature = signatureArray[-1]
        message = messageArray[-1]
        senderPublicKey = PrivateKey.fromString(sender.privateKey).publicKey()
        if (verifyTransaction(message=message, signature=signature, publicKey=senderPublicKey)):
            message = json.loads(message)
            context['isValidated']=True
            receiver = CoinUser.objects.get(publicKey=message['receiver'])
            print(CoinUser.objects.get(username="Bhavye"))
            if receiver is None:
                return redirect('home')
            receiver.amount += int(message['amount'])
            receiver.save()
            sender.amount -= int(message['amount'])
            sender.save()
        else:
            print("Validation failed")
        # print(message)

        signatureArray.clear()
        messageArray.clear()
    
    return render(request, 'home/validate.html', context)