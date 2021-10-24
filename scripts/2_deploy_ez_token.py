# Realizamos las importaciones necesarias para hacer el despligue del token
from brownie import accounts, config, EJXToken

# Creamos nuestras variables que son necesarias para la inicialización
# del contrato, esto lo vemos dentro del constructor del archivo solidity
# TokenERC20.sol, que está en la carpeta contrato.

initial_supply = 100e18 # Cantidad 100
token_name = "EJELTEX"
token_symbol = "EJX"


def main():
    account = accounts[1] # Usamos la cuenta 0 de nuestra blockchain
    # Inicializamos nuestro contrato por medio de la cuenta 0
    erc20 = EJXToken.deploy(
        initial_supply,
        {"from": account})
