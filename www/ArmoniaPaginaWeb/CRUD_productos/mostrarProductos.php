<?php
$baseURL = "../static/src/img/";

// Consulta para obtener los productos
$apiURL = "http://core_api:8000/api/Product/GetProduct";
$apiResponse = file_get_contents($apiURL);

// Verifica la respuesta antes de decodificarla
$productos = json_decode($apiResponse, true);

// Verifica si hay productos y si `hasProduct` es verdadero
if ($productos['hasProduct']) {
    ?>
    <div class="table-responsive">
    <table class="table table-striped">
        <thead>
            <tr>
                <th scope="col">ID</th>
                <th scope="col">NOMBRE</th>
                <th scope="col">DESCRIPCIÓN</th>
                <th scope="col">PRECIO</th>
                <th scope="col">STOCK</th>
                <th scope="col">IMAGEN</th>
                <th scope="col">CATEGORÍA</th>
                <th scope="col">ACCIONES</th>
            </tr>
        </thead>
        <tbody>
            <?php
            foreach ($productos['productList'] as $producto) {
                // Obtener los valores del producto
                $idProducto = $producto['id_producto'];
                $nombre = $producto['nombre'];
                $descripcion = $producto['descripcion'];
                $precio = $producto['precio'];
                $stock = $producto['stock'];
                $imagen = $producto['imagen'];
                $idCategoria = $producto['id_categoria'];

                // Obtener el nombre de la categoría
                $categoriaURL = "http://core_api:8000/api/Category/GetCategory";
                $categoriaResponse = file_get_contents($categoriaURL);
                $categoriaData = json_decode($categoriaResponse, true);

                $nombreCategoria = ''; // Inicializar el nombre de la categoría
        
                if ($categoriaData['hasCategory']) {
                    foreach ($categoriaData['categoryList'] as $categoria) {
                        if ($categoria['id_categoria'] == $idCategoria) {
                            $nombreCategoria = $categoria['nombre'];
                            break;
                        }
                    }
                }

                // Imprime las filas de la tabla con las columnas específicas
                echo "<tr>";
                echo "<th scope='row'>$idProducto</th>";
                echo "<td>$nombre</td>";
                echo "<td>$descripcion</td>";
                echo "<td>S/ $precio</td>";
                echo "<td>$stock</td>";
                echo "<td><img style='width: 120px; border-radius: 30px;' src='$baseURL$imagen'></td>";
                echo "<td>$nombreCategoria</td>";
                echo "<th>
                <a href='editarProducto.php?id=$idProducto' class=\"btn btn-warning\">Editar</a>
                <br>
                <br>
                <a href='eliminarProducto.php?ID_PRODUCTO=$idProducto' class=\"btn btn-danger\">Eliminar</a>
                </th>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
    </div>
    <?php
} else {
    echo "No hay productos disponibles en este momento.";
}
?>