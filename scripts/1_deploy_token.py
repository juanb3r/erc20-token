# Realizamos las importaciones necesarias para hacer el despligue del token
from brownie import accounts, config, TokenERC20

# Creamos nuestras variables que son necesarias para la inicialización
# del contrato, esto lo vemos dentro del constructor del archivo solidity
# TokenERC20.sol, que está en la carpeta contrato.

# ? TokenERC20 corresponde al archivo generado por el compile que se guarda
# ? en la carpeta build del proyecto.


initial_supply = 100e18  # Cantidad 100
token_name = "JELTEX"
token_symbol = "JEX"


def main():
    account = accounts[0] #  Usamos la cuenta 0 de nuestra blockchain
    # Inicializamos nuestro contrato por medio de la cuenta 0
    erc20 = TokenERC20.deploy(
        initial_supply,
        token_name,
        token_symbol,
        {"from": account})
