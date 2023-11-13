<?php
$baseURL = "static/src/img/";

// Consulta para obtener los productos
$apiURL = "http://core_api:8000/api/Product/GetProduct";
$apiResponse = file_get_contents($apiURL);

// Verifica la respuesta antes de decodificarla
$productos = json_decode($apiResponse, true);

// Verifica si hay productos y si `hasProduct` es verdadero
if ($productos['hasProduct']) {
    // Muestra los productos
    foreach ($productos['productList'] as $producto) {
        ?>
        <div class="card m-4" style="width: 18rem;">
            <form id="formulario" name="formulario" method="post" action="cart.php">
                <?php if (isset($producto['precio'])) { ?>
                    <input name="precio" type="hidden" id="precio" value="<?php echo $producto['precio']; ?>" />
                <?php } ?>
                <?php if (isset($producto['nombre'])) { ?>
                    <input name="titulo" type="hidden" id="titulo" value="<?php echo $producto['nombre']; ?>" />
                <?php } ?>
                <input name="cantidad" type="hidden" id="cantidad" value="1" class="pl-2" />
                <?php if (isset($producto['imagen'])) { ?>
                    <img src="<?php echo $baseURL . $producto['imagen']; ?>" class="card-img-top pt-3" alt="...">
                <?php } ?>
                <div class="card-body d-flex flex-column align-items-center justify-content-center">
                    <?php if (isset($producto['nombre'])) { ?>
                        <h5 class="card-title text-center"><?php echo $producto['nombre']; ?></h5>
                    <?php } ?>
                    <?php if (isset($producto['descripcion'])) { ?>
                        <p class="card-text"><?php echo $producto['descripcion']; ?></p>
                    <?php } ?>
                    <?php if (isset($producto['precio'])) { ?>
                        <p class="card-text">S/<?php echo $producto['precio']; ?></p>
                    <?php } ?>
                    <div class="boton-container">
                        <button class="btn btn-primary" type="submit"><i class="fas fa-shopping-cart"></i> Añadir al carrito</button>
                    </div>
                </div>
            </form>
        </div>
        <?php
    }
} else {
    echo "No hay productos disponibles en este momento.";
}

// Cierra la conexión
mysqli_close($conexion);
?>