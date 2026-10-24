import base64
import hmac

key = bytes.fromhex("0ed043c08c0ec4b19a2e20fabfe271ad")
vin = ""
swid = bytes.fromhex("")

data = swid + vin.encode() + b" "
hash = hmac.new(key, data, "ripemd160").digest()
code = base64.b32encode(hash).decode()[-6:]

print(code)