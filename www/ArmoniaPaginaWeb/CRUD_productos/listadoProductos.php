<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!--busqueda de productos-->

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
    crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />

</head>
<title>Lista productos</title>
</head>

<body style="background-color:#FFFFFF; padding-bottom: 50px">

  <!-- Configuración del navbar user y lista -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" style="font-family:var;color:#FFFFFF;margin-left:1em;font-weight:600;font-size:22px;">Armonía 10</a>
        </div>
    </nav>

  <style>
    #bar a {
      border-style: none;
      background-color: ;
      border-radius: 10px;
    }
  </style>


  <!-- Tabla de  lista de  producto  titulo -->
  <br>
  <div class="container">
    <h1 class="text-center"
      style=" background-color:black;color:white; height: 80px; font-family:var; padding-top: 12px;"> Lista de productos
    </h1>
  </div>



  <!-- Tabla de lista de productos  -->

  <div class="container">

    <div class="container ">
      <a href="agregarProducto.php" class="btn btn-success">Agregar producto</a>
    </div>

    <div class="table-responsive">
    <table class="table table-striped" style="background-color:#f9cb9c; font-family:var; text-align:justify;">
      <tbody>
        <?php
        include('mostrarProductos.php');
        ?>
      </tbody>
    </table>
    </div>

  </div>

  <style>
    .container {
      font-family: monospace;
      margin-top: 1em;
      margin-bottom: 1em;
      border-radius: 1em;
    }

    .container a {
      letter-spacing: 3px
    }
  </style>

  <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
  <script>
    AOS.init();
  </script>


  <!-- Incluir Bootstrap JS y jQuery (opcional) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
</body>

</html>