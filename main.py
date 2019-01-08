import  subprocess
# import atexit


def run_continouesly(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        yield line

# def exit_handler():
#     print("Exiting...stopping scan..")


if __name__ == "__main__":
    # atexit.register(exit_handler)

    routerIP = "192.168.5.36"
    routerInterface = "wlan1"
    address = "C0:CC:F8:6D:45:8D"

    newParag = False
    prgStr = ""
    for line in run_continouesly('ssh admin@'+ routerIP +' "interface wireless snooper flat-snoop '+ routerInterface +'"'):
        if (len(line) == 0):
            if (prgStr.find("address="+address)!=-1):
                start = prgStr.find("signal-strength=")+len("signal-strength=")
                stop = prgStr.find("dB",start)
                print(prgStr[start:stop] +" =======> "+ prgStr)
                # print(prgStr)
                print("######")
            prgStr = ""
        else:
            prgStr += line
            