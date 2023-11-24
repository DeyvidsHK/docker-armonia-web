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
$api_url = 'http://core_api:8000/api/Client/Login';

try {
    $response = file_get_contents($api_url, false, $context);
    
    if ($response === FALSE) {
        die('Error al conectarse a la API');
    }

    $result = json_decode($response, true);

    if ($result['success']) {
        $_SESSION["usuario"] = $correo;
        
        if (isset($result['id_cliente'])) {
            $_SESSION["id_cliente"] = $result['id_cliente'];
        }
        
        if (isset($result['nombre'])) {
            $_SESSION["nombre_usuario"] = $result['nombre'];
        }

        // Establece la clave "correo_usuario" en la variable de sesión
        $_SESSION["correo_usuario"] = $correo;

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
    die('Error: ' . $e->getMessage());
}
?>
