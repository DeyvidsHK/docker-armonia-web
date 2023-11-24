<?php

session_start();

$correo = $_POST['correo'];
$contrasena = $_POST['contrasena'];

// Datos para enviar a la API
$data = array(
    "correo" => $correo,
    "contrasena" => $contrasena
);

$options = array(
    'http' => array(
        'header' => "Content-type: application/json\r\n",
        'method' => 'POST',
        'content' => json_encode($data),
    ),
);

$context = stream_context_create($options);
$api_url = 'http://core_api:8000/api/Client/Login'; // Reemplaza con la URL correcta de tu API

// Usa file_get_contents dentro de un bloque try-catch
try {
    $response = file_get_contents($api_url, false, $context);
    
    // Verifica la respuesta de la API
    if ($response === FALSE) {
        // Error al hacer la solicitud a la API
        die('Error al conectarse a la API');
    }

    // Decodifica la respuesta JSON
    $result = json_decode($response, true);

    // Verifica si la autenticación fue exitosa según la respuesta de la API
    if ($result['success']) {
        $_SESSION["usuario"] = $correo;
        // Verifica si 'id_cliente' está presente en $result antes de intentar asignarlo a $_SESSION["id_cliente"]
        if (isset($result['id_cliente'])) {
            $_SESSION["id_cliente"] = $result['id_cliente'];
        }
        header("location: ../tienda.php");
        exit();
    } else {
        echo "
            <script>
                alert('Usuario no registrado');
                window.location = '../login.php';
            </script>
        ";
        exit();
    }
} catch (Exception $e) {
    // Manejo de excepciones
    die('Error: ' . $e->getMessage());
}
?>
