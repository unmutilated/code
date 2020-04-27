import base64
Examples = ["Cat", "Mouse", "Monitor"]
print("Word\t", "ACII\t\t\t\t", "Base64")
for ex in Examples:
    exEnc = ""
    for byte in ex.encode():
        exEnc += format(byte,'08b') + " "
    print(ex,"\t",exEnc,"\t",base64.b64encode(ex.encode()))
