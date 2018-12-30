from pywallet import wallet

seed = wallet.generate_mnemonic()

w = wallet.create_wallet(network="BTC", seed=seed, children=1)

print(w)
