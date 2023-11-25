<!doctype html>
<html lang="es">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Agregar Productos</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
        integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
</head>
<!-- el diseño esta hecho con boostrap  -->
<!-- el styleLista.css es solo para el banner -->

<body style="background-color:#EAE6CA;">
    <!-- Configuración del navbar user y lista -->

    <!-- Configuración del navbar user y lista -->
    <nav class="navbar navbar-expand-lg bg-body-tertiary" style="background-color:#f9cb9c;">
        <div class="container-fluid">
            <a class="navbar-brand"
                style="font-family:var;color:#783f04;margin-left:1em;font-weight:600;font-size:22px;">Armonia 10</a>

        </div>
    </nav>


    <style>
        #bar a {
            border-style: none;
            background-color: ;
            border-radius: 10px;
        }
    </style>

    <!-- Formulario de agregar Productos -->
    <br>
    <div class="container">
        <h1 class="text-center" style=" background-color:black;color:white; font-family:var;">Agregar productos</h1>
        <form style="font-family:var;" action="insertarProducto.php" method="POST" enctype="multipart/form-data">

            <!-- esta dentro del formulario  -->
            <div class="mb-3">
                <label class="form-label" style="margin-left:1em;font-style:italic;font-size:20px;">Nombre Producto :
                </label>
                <input type="text" class="form-control" style="background-color:#EAE6CA;border-color:black;"
                    name="nombreP" required>

            </div>
            <div class="mb-3">
                <label class="form-label" style="margin-left:1em;font-style:italic;font-size:20px;">Descripción :
                </label>
                <input type="text" class="form-control" style="background-color:#EAE6CA;border-color:black;"
                    name="descripcionP" required>

            </div>
            <div class="mb-3">
                <label class="form-label" style="margin-left:1em;font-style:italic;font-size:20px;">Precio : </label>
                <input type="text" class="form-control" style="background-color:#EAE6CA;border-color:black;"
                    name="precioP">

            </div>
            <div class="mb-3">
                <label class="form-label" style="margin-left:1em;font-style:italic;font-size:20px;">Stock : </label>
                <input type="text" class="form-control" style="background-color:#EAE6CA;border-color:black;"
                    name="stockP" required>

            </div>

            <div class="mb-3">
                <label for="imagen" class="form-label" style="margin-left:1em;font-style:italic;font-size:20px;"> Imagen
                    del producto :</label>
                <input type="file" name="imagenP" id="imagen" style="background-color:#EAE6CA;border-color:black;"
                    class="form-control" required>
            </div>

            <label for="" style="margin-left:1em;font-style:italic;font-size:20px; ">Categoría :</label>
            <select class="form-select mb-3 " style="background-color:#EAE6CA;border-color:black;" name="CategoriaP" required>
                <option selected disabled>-- Selecciona la categoría del producto --</option>

                <?php
                // Obtener la lista de categorías
                $categoriaURL = "http://core_api:8000/api/Category/GetCategory";
                $categoriaResponse = file_get_contents($categoriaURL);
                $categoriaData = json_decode($categoriaResponse, true);

                if ($categoriaData['hasCategory']) {
                    foreach ($categoriaData['categoryList'] as $categoria) {
                        $idCategoria = $categoria['id_categoria'];
                        $nombreCategoria = $categoria['nombre'];
                        ?>
                        <option value="<?php echo $idCategoria; ?>">
                            <?php echo $nombreCategoria; ?>
                        </option>
                        <?php
                    }
                }
                ?>
            </select>

            <div class="text-center" style="margin-bottom:1em;">
                <button type="submit" class="btn btn-danger" name="agregarProducto">Agregar</button>
                <a href="listadoProductos.php" class="btn btn-dark">Volver</a>
            </div>

        </form>
    </div>
    <!-- esto son script de boostrap  -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>
</body>

</html>
