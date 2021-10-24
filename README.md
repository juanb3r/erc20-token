# ERC Token
Creación de un token por medio de solidity y brownie que cumpla con el estándar ERC20.


-   [Instalación](#installation)
-   [Compilación](#compilation)
-   [Despligue](#deploy)
-   [Configuración Kovan](#kovan)

## <span id="installation">Instalación</span> 
 
Antes que todo debemos tener instalado python dentro de nuestro equipo.

-   Creación del entorno de desarrollo

    ``` 
    $ python3 -m venv venv 
    ```

-   Activación del entorno de desarrollo

    Ubuntu/MacOs:

    ```
    $ . venv/bin/activate
    ```

    Windows:

    ```
    $ venv/scripts/activate
    ```

-   Instalación de dependencias

    Instalamos brownie:

    ```
    $ pip install eth-brownie
    ```

    Inicializamos el proyecto (* Necesita estar la carpeta vacía)

    ```
    $ brownie init
    ```

    Nos crea la estructura del proyecto y dentro de la carpeta contract creamos nuestros contratos.

## <span id="compilation">Compilación</span>

Con la ayuda de brownie compilamos.

-   Compilando el archivo de solitidy (Dentro de la carpeta contract):
    
    ```
    $ brownie compile
    ```
    

Dentro de la carpeta build de nuestro se crea el json que contiene la información de la abi del contrato.


## <span id="deploy">Despliegue</span>

Para el despliegue usaremos ganache-cli como blockchain local.

```
$ ganache-cli
```

Ahora creamos los scripts para el despliegue. Creamos un archivo python dentro de la carpeta Script

- Desplegar en ganache-cli

    ```
    $ brownie run script/1_deploy_token.py
    ```

## <span id="kovan">Configuración Kovan</span>

Para realizar el despliegue en la red de Kovan necesitamos de nuestra cuenta en Metamask y la llave de nuestra cuenta, este atributo lo exportamos como variable de entorno **PRIVATE_KEY** en un archivo .env, y luego es leído cuando se corra el script por medio de nuestro archivo de configuración de brownie.

- Desplegar en la red de kovan

    ```
    $ brownie run scripts/3_deploy_tk_kovan.py --network kovan
    ```



