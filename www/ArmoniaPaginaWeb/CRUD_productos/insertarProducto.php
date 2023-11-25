<?php
if (isset($_POST['agregarProducto'])) {
    try {
        // Recuperar los datos del formulario
        $nombreProducto = $_POST['nombreP'];
        $descripcionProducto = $_POST['descripcionP'];
        $precioProducto = $_POST['precioP'];
        $stockProducto = $_POST['stockP'];
        $categoriaProducto = $_POST['CategoriaP'];

        // Verificar si la imagen se cargó correctamente
        if (isset($_FILES['imagenP']) && $_FILES['imagenP']['error'] == UPLOAD_ERR_OK) {
            // Procesar la imagen
            $imagenNombre = $_FILES['imagenP']['name']; // Obtener el nombre original de la imagen
            $imagenTmp = $_FILES['imagenP']['tmp_name']; // Obtener la ubicación temporal de la imagen

            // Asignar un nombre único a la imagen para evitar conflictos
            $nombreUnico = uniqid() . '_' . $imagenNombre;

            // Ruta de la carpeta donde se guardará la imagen
            $baseURL = "../static/src/img/";
            $rutaCarpeta = $baseURL;

            // Ruta completa del archivo de imagen
            $rutaImagen = $rutaCarpeta . $nombreUnico;

            // Mover la imagen a la carpeta de destino
            if (!move_uploaded_file($imagenTmp, $rutaImagen)) {
                throw new Exception("Error al mover la imagen a la carpeta de destino.");
            }
        } else {
            throw new Exception("Error al cargar la imagen.");
        }

        // Crear la solicitud para agregar el producto
        $productoData = array(
            'nombre' => $nombreProducto,
            'descripcion' => $descripcionProducto,
            'precio' => $precioProducto,
            'stock' => $stockProducto,
            'imagen' => $nombreUnico, // Guardar el nombre único en la base de datos
            'id_categoria' => $categoriaProducto
        );

        $apiURL = "http://core_api:8000/api/Product/CreateProduct";
        $jsonData = json_encode($productoData);

        $options = array(
            'http' => array(
                'header' => "Content-type: application/json\r\n",
                'method' => 'POST',
                'content' => $jsonData
            )
        );

        $context = stream_context_create($options);
        $result = file_get_contents($apiURL, false, $context);

        // Verificar la respuesta de la API y realizar acciones adicionales si es necesario
        // Por ejemplo, podrías redirigir al usuario a una página de éxito o mostrar un mensaje.
        $response = json_decode($result, true);
        if ($response['success']) {
            echo '<script>alert("Producto agregado con éxito."); window.location.href = "listadoProductos.php";</script>';
        } else {
            throw new Exception($response['message']);
        }
    } catch (Exception $e) {
        // Manejo de excepciones
        echo "Error: " . $e->getMessage();
    }
}
?>
