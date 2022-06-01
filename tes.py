import aiml
# membuat kernel dan mempelajari berkas AIML
kernel = aiml.Kernel()
kernel.learn("utama.xml")
kernel.respond("aiml a")
while True:
    #print(kernel.respond(input("User: >> ")))

    reply = kernel.respond(input("User > "))
    if reply:
        print("bot > ", reply)
    else:
        print("bot >stop", )
