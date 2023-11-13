<?php

$nombre = $_POST["nombre"]; 
$correo = $_POST["correo"]; 
$usuario = $_POST["usuario"]; 
$contrasena = $_POST["contrasena"];

// Datos para enviar a la API
$data = array(
    'nombre' => $nombre,
    'correo' => $correo,
    'usuario' => $usuario,
    'contrasena' => $contrasena
);

// URL de tu API
$api_url = 'http://core_api:8000/api/Client/CreateClient';

// Inicializar cURL
$ch = curl_init($api_url);

// Configurar la solicitud cURL para ser de tipo POST y enviar datos JSON
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

// Configurar para recibir la respuesta de la API
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Ejecutar la solicitud cURL y obtener la respuesta
$response = curl_exec($ch);

// Cerrar la sesión cURL
curl_close($ch);

// Decodificar la respuesta JSON
$result = json_decode($response, true);

// Verificar la respuesta de la API
if ($result['success']) {
    echo "
        <script>
            alert('Usuario almacenado');
            window.location = '../login.php';
        </script>
    ";
} else {
    echo "
        <script>
            alert('Error al almacenar usuario: " . $result['message'] . "');
            window.location = '../login.php';
        </script>
    ";
}
?>
